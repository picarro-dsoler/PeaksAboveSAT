from locallib.picarrodb import *
import sqlite3
import uuid
from datetime import date, datetime, time
import pandas as pd


# SQL Server-style datatypes -> SQLite column types.
# geometry is stored as WKT text (from Shape.STAsText() / shapely .wkt).
SQLITE_TYPE_MAP = {
    'geometry': 'TEXT',
}


def _connect(db_path):
    """SQLite connection used by KPITable (same pragmas as KPIHubConnection)."""
    try:
        from lib.KPIHubConnection import connect_sqlite
        return connect_sqlite(db_path)
    except ImportError:
        try:
            from KPIHubConnection import connect_sqlite
            return connect_sqlite(db_path)
        except ImportError:
            conn = sqlite3.connect(db_path, timeout=30, check_same_thread=False)
            conn.execute("PRAGMA busy_timeout = 30000")
            conn.execute("PRAGMA journal_mode = WAL")
            conn.text_factory = str
            return conn


class KPITable(DBTable):
    def __init__(self, name, columns = None):
        super().__init__(name, columns)
        self.sql_list = {}

    @staticmethod
    def sqlite_column_type(datatype):
        if datatype is None:
            return 'TEXT'
        return SQLITE_TYPE_MAP.get(datatype, datatype)
    
    def delete_table(self, arguments = None):
        if arguments is None:
            raise ValueError("Arguments are required")
        if 'db_path' not in arguments:
            raise ValueError("db_path is required")
        conn = _connect(arguments['db_path'])
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {self.name}")
        conn.commit()
        conn.close()


    def create_table(self, arguments = None, commit = True):
        if arguments is None:
            raise ValueError("Arguments are required")
        if 'db_path' not in arguments:
            raise ValueError("db_path is required")
        conn = _connect(arguments['db_path'])
        cursor = conn.cursor()
        col_defs_list = []
        primary_keys = []
        for column in self.columns:
            sqlite_type = self.sqlite_column_type(column.datatype)
            col_def = f"{column.name} {sqlite_type}"
            if getattr(column, "key", None) == "primary":
                primary_keys.append(column.name)
            col_defs_list.append(col_def)
        col_defs = ", ".join(col_defs_list)
        if primary_keys:
            pk_str = ", PRIMARY KEY (" + ", ".join(primary_keys) + ")"
            col_defs += pk_str
        if 'pair_key' in arguments and arguments['pair_key'] is not None:
            col_defs += f" , PRIMARY KEY ({', '.join(arguments['pair_key'])})"
        sql = f"CREATE TABLE IF NOT EXISTS {self.name} ({col_defs})"
        if commit:
            cursor.execute(sql)
            if 'extra_sql' in arguments and arguments['extra_sql'] is not None:
                cursor.execute(arguments['extra_sql'])
            conn.commit()
            conn.close()
        return sql

    def reinit_table(self, arguments = None, extra_sql = None):
        if arguments is None:
            raise ValueError("Arguments are required")
        if 'db_path' not in arguments:
            raise ValueError("db_path is required")
        arguments_db_path = arguments['db_path']
        self.delete_table(arguments = {'db_path': arguments_db_path})
        self.create_table(arguments = arguments)

    def query_table(self, arguments = None):
        if arguments is None:
            raise ValueError("Arguments are required")
        if 'db_path' not in arguments:
            raise ValueError("db_path is required")
        conn = _connect(arguments['db_path'])
        df = pd.read_sql_query(f"SELECT * FROM {self.name}", conn)
        conn.close()
        return df

    def sql(self, query = 'create', db_type= 'postgres'):
        if db_type == 'postgres':
            return self.sql_list[query]
        else:
            return self.sql_list[query]

    def update_table(self, arguments = None):
        # Load the content of the df into a temp table
        # Bulk update
        df = arguments['DataFrame']
        primary_key = arguments['PrimaryKey']
        if isinstance(primary_key, list):
            pk_cols = set(primary_key)
            primary_key_str = ','.join(primary_key)
        elif isinstance(primary_key, str):
            pk_cols = {primary_key}
            primary_key_str = primary_key
        else:
            raise ValueError("PrimaryKey must be a list of strings or a single string")

        conn = _connect(arguments['db_path'])
        cursor = conn.cursor()

        cols = df.columns.tolist()
        columns = ", ".join(cols)
        placeholders = ", ".join(["?"] * len(cols))
        updates = ", ".join([f"{col}=excluded.{col}" for col in cols if col not in pk_cols])

        insert_sql = f"""
            INSERT INTO {self.name} ({columns})
            VALUES ({placeholders})
            ON CONFLICT({primary_key_str}) DO UPDATE SET
            {updates};
        """

        # To avoid the InterfaceError, convert unsupported types to sqlite-bindable values.
        def clean_value(val):
            if pd.isna(val):
                return None
            if isinstance(val, pd.Timestamp):
                return val.to_pydatetime()
            if isinstance(val, datetime):
                return val
            if isinstance(val, time):
                return val.isoformat()
            if isinstance(val, date):
                return val.isoformat()
            if isinstance(val, uuid.UUID):
                return str(val)
            # Shapely / geo geometries -> WKT text for SQLite geometry columns
            if hasattr(val, "wkt") and not isinstance(val, (str, bytes, bytearray)):
                return val.wkt
            if isinstance(val, (bytes, bytearray)):
                return bytes(val)
            if hasattr(val, "item"):  # handles numpy scalars
                return val.item()
            return val

        data = [tuple(clean_value(row[col]) for col in cols) for _, row in df.iterrows()]
        cursor.executemany(insert_sql, data)  # use executemany for efficiency

        conn.commit()
        conn.close()

    def delete_data(self, arguments = None):
        """
        Deletes rows from the table where the primary key(s) match the provided value(s).
        arguments must contain:
            - 'db_path' (str): path to the sqlite DB
            - 'PrimaryKey' (str or list): column(s) to match
            - 'KeyValues' (list of dict): each dict has {primary_key_col: value, ...} or a DataFrame of keys
        """
        if arguments is None:
            raise ValueError("Arguments are required")
        if 'db_path' not in arguments:
            raise ValueError("db_path is required")
        if 'PrimaryKey' not in arguments:
            raise ValueError("PrimaryKey is required")
        if 'KeyValues' not in arguments:
            raise ValueError("KeyValues is required (list of dicts or DataFrame)")
        
        db_path = arguments['db_path']
        primary_key = arguments['PrimaryKey']
        key_values = arguments['KeyValues']

        if isinstance(primary_key, list):
            pk_cols = primary_key
        elif isinstance(primary_key, str):
            pk_cols = [primary_key]
        else:
            raise ValueError("PrimaryKey must be a list of strings or a single string")

        # Accept KeyValues either as a DataFrame OR a list of dicts
        if isinstance(key_values, pd.DataFrame):
            keys_list = key_values[pk_cols].to_dict(orient='records')
        elif isinstance(key_values, list):
            keys_list = key_values
        else:
            raise ValueError("KeyValues must be a DataFrame or list of dicts")

        conn = _connect(db_path)
        cursor = conn.cursor()

        where_clause = " AND ".join([f"{col} = ?" for col in pk_cols])
        sql = f"DELETE FROM {self.name} WHERE {where_clause}"

        # Prepare tuples of key values for each row to delete
        values_list = []
        for key_dict in keys_list:
            values = tuple(key_dict.get(col) for col in pk_cols)
            values_list.append(values)

        cursor.executemany(sql, values_list)
        conn.commit()
        conn.close()