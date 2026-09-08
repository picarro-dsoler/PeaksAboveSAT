from locallib.picarrodb import *
from locallib.query import *

import os
import sys


# Get the absolute path of the current file's directory
directory = os.path.abspath(os.path.dirname(__file__))

# Just add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(directory, "..")))

from tables.IngesterTables import *
from config import *
from lib.KPIHubConnection import *
import pandas as pd
from datetime import datetime

def add_customer(customer_name, Conn, active = True, country = None, XchangeLocation = None):
    result = Query(query = f"SELECT C.Id, C.Name FROM Customer C WHERE LOWER(C.Name) = LOWER('{customer_name}')").execute(Conn)
    xchange_location = XchangeLocation if XchangeLocation is not None else 'Unknown'
    if result.empty:
        raise ValueError(f"Customer {customer_name} not found")
    else:
        if Conn.database == 'EU-SurveyorProduction':
            DBLocation = 'EU1'
        elif Conn.database == 'EU-SurveyorProduction2':
            DBLocation = 'EU2'
        else:
            DBLocation = 'Unknown'
        short_name = result.iloc[0]['Name'].replace(" ", "")
        data = pd.DataFrame({
            'CustomerId': [result.iloc[0]['Id']],
            'Name': [result.iloc[0]['Name']],
            'ShortName': [short_name],
            'DBLocation': [DBLocation],
            'Active': [active],
            'XchangeLocation': [xchange_location],
            'LastUpdated': [datetime.now()]
        })
        if country is not None:
            data['Country'] = country
        PeakAboveSATCustomer.update_table(arguments={'DataFrame': data, 'db_path': DB_PATH, 'PrimaryKey': ['CustomerId']})