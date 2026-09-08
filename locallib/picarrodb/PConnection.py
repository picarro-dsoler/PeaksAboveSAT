import os
import warnings
import pandas as pd
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import Tuple
import uuid
import numpy as np
load_dotenv(override=True)

# Suppress pandas warnings about DBAPI connections
warnings.filterwarnings("ignore", 
                       message=".*pandas only supports SQLAlchemy connectable.*",
                       category=UserWarning)


class PConnection:
    def __init__(self, host: str, database: str, user: str, password: str, dbtype: str = ''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.dbtype = dbtype
        self.engine = self.set_engine()
        if self.engine is not None:
            self.session = Session(bind=self.engine, future=True)
        else:
            raise Exception("Engine not implemented set")
        self.Session = self.get_session()

    def set_engine(self):
        return None

    def get_session(self):
        return Session(bind=self.engine, future=True)
    
class EUConnection(PConnection):
    def __init__(self, host: str, database: str, user: str, password: str):
        super().__init__(host, database, user, password, dbtype = 'mssql')
            
    def set_engine(self):
        user = quote_plus(self.user or "")
        password = quote_plus(self.password or "")
        database = quote_plus(self.database or "")
        return create_engine(
            f"mssql+pyodbc://{user}:{password}@{self.host}:1433/{database}?"
            "driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes")
    
class DataHubConnection(PConnection):
    def __init__(self, host: str, database: str, user: str, password: str):
        super().__init__(host, database, user, password, dbtype = 'postgresql')
            
    def set_engine(self):
        return create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:5432/{self.database}")


# EU1 credentials
EU1_USER = os.getenv("EUDBUSER")
EU1_PASSWORD = os.getenv("EUDBPW")

#EU2 credentials
EU2_USER = os.getenv("EU2DBUSER")
EU2_PASSWORD = os.getenv("EU2DBPW")

#EU1 PROD credentials
EU1_PROD_USER = os.getenv("EUPRODDBUSER")
EU1_PROD_PASSWORD = os.getenv("EUPRODDBPW")

#EU2 PROD credentials
EU2_PROD_USER = os.getenv("EU2PRODDBUSER")
EU2_PROD_PASSWORD = os.getenv("EU2PRODDBPW")

#US credentials
US_USER = os.getenv("USDBUSER")
US_PASSWORD = os.getenv("USDBPW")

#DataHub credentials
DATAHUB_USER = os.getenv("DATAHUBUSER")
DATAHUB_PASSWORD = os.getenv("DATAHUBPW")
DATAHUB_DATABASE = os.getenv("DATAHUBDATABASE")

try:
    EU1_Conn = EUConnection(host="eu-prd-sqlsrv-ee-db01.czz1yneu9gmr.eu-central-1.rds.amazonaws.com", user=EU1_USER, password=EU1_PASSWORD, database="EU-SurveyorProduction")
    print("EU1_Conn created successfully")
except Exception as e:
    print(f"Error creating EU1_Conn: {e}")
    EU1_Cinn = None

try:
    EU2_Conn = EUConnection(host="eu-prd2-sqlsrv-ee-db01.czz1yneu9gmr.eu-central-1.rds.amazonaws.com", user=EU2_USER, password=EU2_PASSWORD, database="EU-SurveyorProduction2")
    print("EU2_Conn created successfully")
except Exception as e:
    print(f"Error creating EU2_Conn: {e}")
    EU2_Conn = None

try:
    DATAHUB_Conn = DataHubConnection(host="eu-sensebird-migrated-rds-pg1-r4-prd.czz1yneu9gmr.eu-central-1.rds.amazonaws.com", user=DATAHUB_USER, password=DATAHUB_PASSWORD, database=DATAHUB_DATABASE)
    print("DataHub_Conn created successfully")
except Exception as e:
    print(f"Error creating DATAHUB_Conn: {e}")
    DATAHUB_Conn = None

try:
    US_Conn = EUConnection(host="30.30.240.170", user=US_USER, password=US_PASSWORD, database="SurveyorProduction")
    print("US_Conn created successfully")
except Exception as e:
    print(f"Error creating US_Conn: {e}")
    US_Conn = None

try:
    EU1_PROD_Conn = EUConnection(host="eu-prodstg-sqlsrv-ee-db01.czz1yneu9gmr.eu-central-1.rds.amazonaws.com", user=EU1_PROD_USER, password=EU1_PROD_PASSWORD, database="EU-SurveyorProdstg")
    print("EU1_PROD_Conn created successfully")
except Exception as e:
    print(f"Error creating EU1_PROD_Conn: {e}")
    EU1_PROD_Conn = None

try:
    EU2_PROD_Conn = EUConnection(host="eu-prodstg-sqlsrv-ee-db01.czz1yneu9gmr.eu-central-1.rds.amazonaws.com", user=EU2_PROD_USER, password=EU2_PROD_PASSWORD, database="EU-SurveyorProdstg2")
    print("EU2_PROD_Conn created successfully")
except Exception as e:
    print(f"Error creating EU2_PROD_Conn: {e}")
    EU2_PROD_Conn = None
