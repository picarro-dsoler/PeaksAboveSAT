"""
locallib - Local library package for Picarro data processing and analysis

This package provides utilities for:
- Database connections and operations (picarrodb)
- Data analytics and emission rate calculations (analytics)  
- Query building and execution (query)
- Box.com file operations (box)
- Slack integrations (slack)
- Pandas extensions and utilities (pandas)
- ETL operations and logging (etl)
"""

__version__ = "0.1.5"

# Box.com file operations
from .box import (
    BoxFile,        # Main Box file handler
    BoxFile_old,    # Legacy Box file handler
    BoxFolder       # Box folder operations
)

# Analytics and data processing
from .analytics import (
    BinnedRER,                  # Binned Representative Emission Rate calculations
    CustomBinnedRER,            # Custom binned RER with user-defined parameters
    BinnedDistribution,         # Statistical distribution analysis
    System_Matrix,              # System matrix operations
    SymmetricSystem_Matrix      # Symmetric system matrix operations
)

# Database query utilities
from .query import (
    Query
)

# Picarro database connections and operations
from .picarrodb import (
    # Connection classes
    PConnection,        # Base Picarro database connection
    EUConnection,       # European database connection
    DataHubConnection,  # DataHub connection
    EU1_Conn,          # EU1 server connection instance
    EU2_Conn,          # EU2 server connection instance
    EU1_PROD_Conn,    # EU1 PROD server connection instance
    EU2_PROD_Conn,    # EU2 PROD server connection instance
    DATAHUB_Conn,      # DataHub connection instance
    US_Conn,           # US server connection instance
    
    # Database object classes
    DBTable,           # Database table representation
    DBColumn,          # Database column representation
    DBConstructor,     # Database constructor utilities
    Condition,         # SQL condition builder
    SQLQuery,          # SQL query builder
    
    # Production database table definitions
    ProdDB             # Module containing all production database table definitions
)
from .picarrodb.ProdDB import *  # Import all 172 production database tables for direct access

# Slack integration
from .slack import (
    SlackWriter        # Slack message and file operations
)

# Pandas extensions and utilities
from .pandas import (
    TimezoneAccessor,           # Pandas timezone handling extension
    COMMON_TIMEZONE_MAPPINGS,   # Common timezone mapping constants
    SCFH_TO_G_PER_HOUR,        # Standard cubic feet per hour to grams per hour conversion
    SCFH_TO_SLPM_FACTOR,       # SCFH to standard liters per minute conversion factor
    PandasDBAccessor,          # Pandas database accessor extension
    EmissionRateAccessor,       # Pandas emission rate conversion extension
    NOPAccessor,               # Pandas NOP accessor extension
)

# ETL (Extract, Transform, Load) utilities
from .etl import (
    ConfigParameters,   # Configuration parameter management
    Loggers            # Logging utilities and setup
)

# Define all publicly available classes and functions
__all__ = [
    # Box.com file operations
    'BoxFile',          # Main Box file handler
    'BoxFile_old',      # Legacy Box file handler  
    'BoxFolder',        # Box folder operations
    
    # Analytics and data processing
    'BinnedRER',                # Binned Representative Emission Rate calculations
    'CustomBinnedRER',          # Custom binned RER with user-defined parameters
    'BinnedDistribution',       # Statistical distribution analysis
    'System_Matrix',            # System matrix operations
    'SymmetricSystem_Matrix',   # Symmetric system matrix operations
    
    # Database query utilities
    'Query'                                        # Main query builder class

    
    # Picarro database connections and operations
    'PConnection',      # Base Picarro database connection
    'EUConnection',     # European database connection
    'DataHubConnection', # DataHub connection
    'EU1_Conn',         # EU1 server connection instance
    'EU2_Conn',         # EU2 server connection instance
    'EU1_PROD_Conn',    # EU1 PROD server connection instance
    'EU2_PROD_Conn',    # EU2 PROD server connection instance
    'DATAHUB_Conn',     # DataHub connection instance
    'US_Conn',          # US server connection instance
    'DBTable',          # Database table representation
    'DBColumn',         # Database column representation
    'DBConstructor',    # Database constructor utilities
    'Condition',        # SQL condition builder
    'SQLQuery',         # SQL query builder
    'ProdDB',           # Production database table definitions module
    
    # Slack integration
    'SlackWriter',      # Slack message and file operations
    
    # Pandas extensions and utilities
    'TimezoneAccessor',         # Pandas timezone handling extension
    'COMMON_TIMEZONE_MAPPINGS', # Common timezone mapping constants
    'SCFH_TO_G_PER_HOUR',      # SCFH to grams per hour conversion
    'SCFH_TO_SLPM_FACTOR',     # SCFH to SLPM conversion factor
    'PandasDBAccessor',        # Pandas database accessor extension
    'EmissionRateAccessor',    # Pandas emission rate conversion extension
    'NOPAccessor',             # Pandas NOP accessor extension

    # ETL utilities
    'ConfigParameters', # Configuration parameter management
    'Loggers'          # Logging utilities and setup
]

# Add all production database table definitions to __all__
from .picarrodb.ProdDB import __all__ as _proddb_tables
__all__.extend(_proddb_tables)