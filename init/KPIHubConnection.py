from locallib.picarrodb import *
import sqlite3

import os
import sys

# Get the absolute path of the current file's directory
directory = os.path.abspath(os.path.dirname(__file__))

# Just add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(directory, "..")))
sys.path.append(os.path.abspath(os.path.join(directory)))


def connect_sqlite(db_path):
    """Open a SQLite connection used by KPIHub.

    Geometry columns (datatype='geometry' in table defs) are stored as WKT TEXT.
    Values should be written as WKT strings (e.g. from SQL Server Shape.STAsText()
    or shapely .wkt); SpatiaLite is not required.
    """
    conn = sqlite3.connect(db_path, timeout=30, check_same_thread=False)
    conn.execute("PRAGMA busy_timeout = 30000")
    conn.execute("PRAGMA journal_mode = WAL")
    # Text factory keeps WKT geometry values as str when reading back.
    conn.text_factory = str
    return conn


class SQLiteConnection(PConnection):
    def __init__(self, host):
        self.host = host
        self.dbtype = 'sqlite'
        self.engine = connect_sqlite(host)

# Ensure path to DB is relative to this file's directory
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","KPIHub","SQLite","database","KPIHub.db"))
KPIHub_Conn = SQLiteConnection(db_path)
        
