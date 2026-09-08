import os
import sys
import pandas as pd

directory = os.path.abspath(os.path.dirname(__file__))
_root = os.path.abspath(os.path.join(directory, ".."))

# Add KPIHub root to sys.path so `lib.*` imports resolve regardless of cwd.
sys.path.insert(0, _root)
os.chdir(_root)

import sqlite3

from locallib.picarrodb import *
from locallib.query import *

from lib.tables.IngesterTables import *
from lib.config import *
from lib.KPIHubConnection import *


#Create DB
db_path = os.path.abspath(os.path.join(directory, "..", DB_PATH))

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

conn.commit()

#Create Tables
#KPI Defintion table
PeakAboveSATCustomer.reinit_table(arguments={'db_path': DB_PATH})
PeakAboveSATRecipients.reinit_table(arguments = {'db_path': DB_PATH, 'pair_key': ['CustomerId', 'Email']})
PeakAboveSAT.reinit_table(arguments={'db_path': DB_PATH})
