import os
import sqlite3
import warnings
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import Tuple
import uuid
import numpy as np

from locallib.query import Query

# Register as pandas accessor
@pd.api.extensions.register_dataframe_accessor("db")
class DBAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
        self.parent = None
        self.child = None
        self.query = None
        self.conn = None
    
    def set_connection(self, conn):
        self.conn = conn
        return self._obj
    
    def set_query(self, query):
        if isinstance(query, Query):
            self.query = query.query
        else:
            self.query = query
        return self._obj

    def execute(self, Conn, source_col: str, temp_table_name: str = "#tmp_single_col", sql_col_name:  None = None, varchar_len: int = 4000, chunksize: int = 10000, erase_table: bool = True, append: bool = False, fillna: bool = False):
        df = None
        if isinstance(Conn, list):
            for conn in Conn:
                if df is None:
                    temp_conn, df = self.execute_sql(conn, source_col, temp_table_name, sql_col_name, varchar_len, chunksize, erase_table, fillna)
                else:
                    temp_conn, temp_df = self.execute_sql(conn, source_col, temp_table_name, sql_col_name, varchar_len, chunksize, erase_table, fillna)
                    df = pd.concat([df, temp_df])
        else:
            temp_conn, df = self.execute_sql(Conn, source_col, temp_table_name, sql_col_name, varchar_len, chunksize, erase_table, fillna)
        if (append == True):
            self._obj = pd.merge(self._obj, df, on=source_col, how='left')
            temp_conn.close()
            return self._obj
        else:
            temp_conn.close()
            return df

    def execute_sql(self, Conn, source_col: str, temp_table_name: str = "#tmp_single_col", sql_col_name:  None = None, varchar_len: int = 4000, chunksize: int = 10000, erase_table: bool = True, fillna: bool = False):
        if Conn.dbtype == 'mssql':
            temp_name, temp_conn = self.upload_single_column_to_temp_sqlserver(self._obj,Conn=Conn, source_col=source_col, temp_table_name=temp_table_name, sql_col_name=sql_col_name, varchar_len=varchar_len, chunksize=chunksize, erase_table=erase_table)
        elif Conn.dbtype == 'postgresql':
            temp_name, temp_conn = self.upload_single_column_to_temp_postgresql(self._obj,Conn=Conn, source_col=source_col, temp_table_name=temp_table_name, sql_col_name=sql_col_name, varchar_len=varchar_len, chunksize=chunksize, erase_table=erase_table)
        elif Conn.dbtype == 'sqlite':
            temp_name, temp_conn = self.upload_single_column_to_temp_sqlite(self._obj,Conn=Conn, source_col=source_col, temp_table_name=temp_table_name, sql_col_name=sql_col_name, varchar_len=varchar_len, chunksize=chunksize, erase_table=erase_table)
        else:
            raise ValueError(f"Unsupported database type: {Conn.dbtype}")
        
        # Suppress pandas UserWarning about DBAPI connections while keeping temp_conn alive
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", 
                                  message=".*pandas only supports SQLAlchemy connectable.*",
                                  category=UserWarning)
            if isinstance(self.query, list):
                df = None
                for query in self.query:
                    if df is None:
                        df = pd.read_sql(query, temp_conn)
                    else:
                        df = pd.merge(df, pd.read_sql(query, temp_conn), on=source_col, how='left')
            else:
                df = pd.read_sql(self.query, temp_conn)

        if 'id' in source_col.lower() or 'Id' in source_col:
            df[source_col] = df[source_col].astype(str).str.upper()
        return temp_conn, df


    def upload_single_column_to_temp_sqlserver(self,
        df: pd.DataFrame,
        Conn,
        source_col: str,
        temp_table_name: str = "#tmp_single_col",
        sql_col_name:  None = None,
        varchar_len: int = 4000,
        chunksize: int = 10000,
        erase_table: bool = True
    ) -> Tuple[str, object]:
        """
        Create a one-column #temp table in SQL Server and upload that column from df.

        Returns
        -------
        (temp_table_name, dbapi_conn)
        - temp table name (str)
        - the open DBAPI connection (pyodbc) that owns the #temp session
        """
        if source_col not in df.columns:
            raise KeyError(f"Column '{source_col}' not found in DataFrame.")
        if not temp_table_name.startswith("#"):
            temp_table_name = f"#{temp_table_name}"
        if sql_col_name is None:
            sql_col_name = source_col

        s = df[source_col]

        # Detect UUID-like series (UUID objects or UUID-parsable strings)
        def looks_like_uuid_series(series: pd.Series) -> bool:
            sample = series.dropna().head(50)
            if sample.empty:
                return False

            def is_uuid_like(v):
                if isinstance(v, uuid.UUID):
                    return True
                if isinstance(v, str):
                    try:
                        uuid.UUID(v.strip())
                        return True
                    except Exception:
                        return False
                return False

            valid = sum(is_uuid_like(v) for v in sample)
            return valid >= max(3, int(0.8 * len(sample)))  # heuristic

        # Choose SQL type
        dtype = str(s.dtype)
        if looks_like_uuid_series(s):
            sql_type = "UNIQUEIDENTIFIER"
        elif dtype.startswith("int") and s.isna().any():
            sql_type = "BIGINT"            # safe for NA-containing integer series
        elif dtype.startswith("int"):
            sql_type = "BIGINT" if dtype == "int64" else "INT"
        elif dtype.startswith("float") or np.issubdtype(s.dtype, np.floating):
            sql_type = "FLOAT"
        elif dtype == "bool":
            sql_type = "BIT"
        elif "datetime64" in dtype:
            sql_type = "DATETIME2"
        else:
            sql_type = f"NVARCHAR({varchar_len})"

        create_sql = f"CREATE TABLE {temp_table_name} ([{sql_col_name}] {sql_type});"
        insert_sql = f"INSERT INTO {temp_table_name} ([{sql_col_name}]) VALUES (?);"

        # Coercion for DB insert
        def coerce(v):
            if pd.isna(v):
                return None
            if isinstance(v, uuid.UUID):
                return str(v).lower() # UNIQUEIDENTIFIER accepts canonical string
            if isinstance(v, pd.Timestamp):
                return v.to_pydatetime()
            if isinstance(v, pd.Timedelta):
                return str(v)
            if isinstance(v, np.integer):
                return int(v)
            if isinstance(v, np.floating):
                return float(v)
            if isinstance(v, np.bool_):
                return bool(v)
            if isinstance(v, str):
                return v.lower() if sql_type == "UNIQUEIDENTIFIER" else v
            return str(v)

        rows = [(coerce(v),) for v in s.tolist()]

        # Use DBAPI connection to keep session (and #temp) alive
        conn = Conn.engine.raw_connection()  # pyodbc connection
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT COUNT(*) FROM tempdb.sys.tables WHERE name = '{temp_table_name.replace('#', '')}'")
                table_exists = cur.fetchone()[0] > 0
                if erase_table:
                    # DROP TABLE IF EXISTS needs SQL Server 2016+ / compat 130+.
                    # US/legacy servers often fail with "Incorrect syntax near 'IF'"; use OBJECT_ID instead.
                    t_esc = temp_table_name.replace("'", "''")
                    cur.execute(
                        f"IF OBJECT_ID(N'tempdb..{t_esc}', N'U') IS NOT NULL "
                        f"DROP TABLE {temp_table_name};"
                    )
                    cur.execute(create_sql)
                else:
                    cur.execute(create_sql)
                cur.fast_executemany = True
                if chunksize and len(rows) > chunksize:
                    for i in range(0, len(rows), chunksize):
                        cur.executemany(insert_sql, rows[i:i+chunksize])
                else:
                    cur.executemany(insert_sql, rows)
            conn.commit()
        finally:
            # Intentionally do NOT close conn; caller should close when done with #temp.
            pass

        return temp_table_name, conn

    def upload_single_column_to_temp_sqlite(self,
        df: pd.DataFrame,
        Conn,
        source_col: str,
        temp_table_name: str = "tmp_single_col",
        sql_col_name: str = None,
        varchar_len: int = 4000,
        chunksize: int = 10000,
        erase_table: bool = True
    ) -> Tuple[str, object]:
        """
        Create a one-column TEMP table in SQLite and upload that column from df.

        Returns
        -------
        (temp_table_name, dbapi_conn)
        - temp table name (str)
        - the open sqlite3 connection that owns the temp session
        """
        if source_col not in df.columns:
            raise KeyError(f"Column '{source_col}' not found in DataFrame.")

        temp_table_name = temp_table_name.lstrip("#")
        if not temp_table_name.startswith("temp_"):
            temp_table_name = f"temp_{temp_table_name}"

        if sql_col_name is None:
            sql_col_name = source_col

        s = df[source_col]

        def looks_like_uuid_series(series: pd.Series) -> bool:
            sample = series.dropna().head(50)
            if sample.empty:
                return False

            def is_uuid_like(v):
                if isinstance(v, uuid.UUID):
                    return True
                if isinstance(v, str):
                    try:
                        uuid.UUID(v.strip())
                        return True
                    except Exception:
                        return False
                return False

            valid = sum(is_uuid_like(v) for v in sample)
            return valid >= max(3, int(0.8 * len(sample)))

        dtype = str(s.dtype)
        if looks_like_uuid_series(s):
            sql_type = "TEXT"
        elif dtype.startswith("int") or dtype == "bool":
            sql_type = "INTEGER"
        elif dtype.startswith("float") or np.issubdtype(s.dtype, np.floating):
            sql_type = "REAL"
        elif "datetime64" in dtype:
            sql_type = "TEXT"
        else:
            sql_type = "TEXT"

        create_sql = f"CREATE TEMP TABLE {temp_table_name} ({sql_col_name} {sql_type});"
        insert_sql = f"INSERT INTO {temp_table_name} ({sql_col_name}) VALUES (?);"

        def coerce(v):
            if pd.isna(v):
                return None
            if isinstance(v, uuid.UUID):
                return str(v)
            if isinstance(v, pd.Timestamp):
                return v.isoformat()
            if isinstance(v, pd.Timedelta):
                return str(v)
            if isinstance(v, np.integer):
                return int(v)
            if isinstance(v, np.floating):
                return float(v)
            if isinstance(v, np.bool_):
                return int(v)
            return v

        rows = [(coerce(v),) for v in s.tolist()]

        db_path = Conn.host
        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            if erase_table:
                cur.execute(f"DROP TABLE IF EXISTS {temp_table_name};")
            cur.execute(create_sql)
            if chunksize and len(rows) > chunksize:
                for i in range(0, len(rows), chunksize):
                    cur.executemany(insert_sql, rows[i:i + chunksize])
            else:
                cur.executemany(insert_sql, rows)
            conn.commit()
        except Exception:
            conn.rollback()
            conn.close()
            raise

        return temp_table_name, conn

    def upload_single_column_to_temp_postgresql(self,
        df: pd.DataFrame,
        Conn,
        source_col: str,
        temp_table_name: str = "tmp_single_col",
        sql_col_name: str = None,
        varchar_len: int = 4000,
        chunksize: int = 10000,
        erase_table: bool = True
    ) -> Tuple[str, object]:
        """
        Create a one-column temporary table in PostgreSQL and upload that column from df.
        
        PostgreSQL temporary tables are session-scoped and automatically dropped when the session ends.
        
        Returns
        -------
        (temp_table_name, dbapi_conn)
        - temp table name (str) - will be prefixed with temp_ if not already
        - the open DBAPI connection (psycopg2) that owns the temp session
        """
        if source_col not in df.columns:
            raise KeyError(f"Column '{source_col}' not found in DataFrame.")
        
        # PostgreSQL temp tables don't need # prefix, but we'll use temp_ prefix for clarity
        if not temp_table_name.startswith("temp_"):
            temp_table_name = f"temp_{temp_table_name}"
            
        if sql_col_name is None:
            sql_col_name = source_col

        s = df[source_col]

        # Detect UUID-like series (UUID objects or UUID-parsable strings)
        def looks_like_uuid_series(series: pd.Series) -> bool:
            sample = series.dropna().head(50)
            if sample.empty:
                return False

            def is_uuid_like(v):
                if isinstance(v, uuid.UUID):
                    return True
                if isinstance(v, str):
                    try:
                        uuid.UUID(v.strip())
                        return True
                    except Exception:
                        return False
                return False

            valid = sum(is_uuid_like(v) for v in sample)
            return valid >= max(3, int(0.8 * len(sample)))  # heuristic

        # Choose PostgreSQL SQL type
        dtype = str(s.dtype)
        if looks_like_uuid_series(s):
            sql_type = "UUID"
        elif dtype.startswith("int") and s.isna().any():
            sql_type = "BIGINT"            # safe for NA-containing integer series
        elif dtype.startswith("int"):
            sql_type = "BIGINT" if dtype == "int64" else "INTEGER"
        elif dtype.startswith("float") or np.issubdtype(s.dtype, np.floating):
            sql_type = "DOUBLE PRECISION"
        elif dtype == "bool":
            sql_type = "BOOLEAN"
        elif "datetime64" in dtype:
            sql_type = "TIMESTAMP"
        else:
            sql_type = f"VARCHAR({varchar_len})"

        # PostgreSQL uses CREATE TEMPORARY TABLE or CREATE TEMP TABLE
        create_sql = f"CREATE TEMPORARY TABLE {temp_table_name} ({sql_col_name} {sql_type});"
        insert_sql = f"INSERT INTO {temp_table_name} ({sql_col_name}) VALUES (%s);"

        # Coercion for DB insert
        def coerce(v):
            if pd.isna(v):
                return None
            if isinstance(v, uuid.UUID):
                return str(v)  # PostgreSQL UUID accepts canonical string
            if isinstance(v, pd.Timestamp):
                return v.to_pydatetime()
            if isinstance(v, pd.Timedelta):
                return str(v)
            if isinstance(v, np.integer):
                return int(v)
            if isinstance(v, np.floating):
                return float(v)
            if isinstance(v, np.bool_):
                return bool(v)
            return v

        rows = [(coerce(v),) for v in s.tolist()]

        # Use DBAPI connection to keep session (and temp table) alive
        conn = Conn.engine.raw_connection()  # psycopg2 connection
        try:
            with conn.cursor() as cur:
                # Check if temp table exists (PostgreSQL temp tables are in pg_temp schema)
                cur.execute("""
                    SELECT COUNT(*) FROM information_schema.tables 
                    WHERE table_name = %s AND table_schema LIKE 'pg_temp%%'
                """, (temp_table_name,))
                table_exists = cur.fetchone()[0] > 0
                
                if erase_table and table_exists:
                    cur.execute(f"DROP TABLE IF EXISTS {temp_table_name};")
                    
                if not table_exists or erase_table:
                    cur.execute(create_sql)
                    
                # PostgreSQL uses execute_values for better performance with large datasets
                if chunksize and len(rows) > chunksize:
                    for i in range(0, len(rows), chunksize):
                        chunk_rows = rows[i:i+chunksize]
                        cur.executemany(insert_sql, chunk_rows)
                else:
                    cur.executemany(insert_sql, rows)
                    
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            # Intentionally do NOT close conn; caller should close when done with temp table.
            pass

        return temp_table_name, conn
