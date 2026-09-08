import sqlite3
from locallib.picarrodb import *
from datetime import date
import os
from pathlib import Path
project_root = Path(__file__).parent.parent
DB_NAME = 'PeakAboveSAT.db'
INGESTER_LOG_PATH = 'logs/'

#Refreshing configuration
STARTING_YEAR = 2026
STARTING_DATE = date(STARTING_YEAR, 1, 1)
#Connection Configuration
CONN_DICT = {'EU1':EU1_Conn, 'EU2': EU2_Conn}

#Excel Output Configuration
SUFFIX = 'PeaksAboveSAT'

DB_PATH = os.path.join(project_root, 'database', DB_NAME)