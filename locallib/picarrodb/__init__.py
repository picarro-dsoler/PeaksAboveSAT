"""
picarrodb - Picarro database connection and data handling utilities
"""

from .PConnection import (
    PConnection, 
    EUConnection, 
    DataHubConnection, 
    EU1_Conn, 
    EU2_Conn, 
    EU1_PROD_Conn,
    EU2_PROD_Conn,
    DATAHUB_Conn,
    US_Conn
)
from .PicarroDBClass import DBTable, DBColumn, DBConstructor, Condition, SQLQuery
from . import ProdDB  # Import the entire ProdDB module containing all table definitions
from .ProdDB import *  # Import all table definitions directly for easy access

__all__ = [ 
    'PConnection', 
    'EUConnection',
    'DataHubConnection',
    'EU1_Conn', 
    'EU2_Conn',
    'EU1_PROD_Conn',
    'EU2_PROD_Conn',
    'DATAHUB_Conn',
    'US_Conn',
    'DBTable',
    'DBColumn', 
    'DBConstructor',
    'Condition',
    'SQLQuery',
    'ProdDB'  # Production database table definitions module
] + ProdDB.__all__  # Add all table definitions to the exports