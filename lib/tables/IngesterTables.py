from locallib.picarrodb import *
import sqlite3

from .KPITable import KPITable

PeakAboveSATCustomer = KPITable('PeakAboveSATCustomer')
PeakAboveSATCustomer.add_column(DBColumn('CustomerId', datatype='uniqueidentifier', key='primary'))
PeakAboveSATCustomer.add_column(DBColumn('Name', datatype='nvarchar'))
PeakAboveSATCustomer.add_column(DBColumn('ShortName', datatype='nvarchar'))
PeakAboveSATCustomer.add_column(DBColumn('Active', datatype='bit'))
PeakAboveSATCustomer.add_column(DBColumn('DBLocation', datatype='nvarchar'))
PeakAboveSATCustomer.add_column(DBColumn('XchangeLocation', datatype='nvarchar'))
PeakAboveSATCustomer.add_column(DBColumn('BoxFolderId', datatype='int'))
PeakAboveSATCustomer.add_column(DBColumn('ThresholdSCFH', datatype='float'))
PeakAboveSATCustomer.add_column(DBColumn('LastUpdated', datatype='datetime'))


#Peak Above SAT Recipients
PeakAboveSATRecipients = KPITable('PeakAboveSATRecipients')
PeakAboveSATRecipients.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
PeakAboveSATRecipients.add_column(DBColumn('Email', datatype='nvarchar'))
PeakAboveSATRecipients.add_column(DBColumn('Active', datatype='bit'))
PeakAboveSATRecipients.add_column(DBColumn('LastUpdated', datatype='datetime'))

# Peak Above SAT Table
PeakAboveSAT = KPITable('PeakAboveSAT') 
PeakAboveSAT.add_column(DBColumn('CustomerId', datatype='uniqueidentifier', key='foreign'))
PeakAboveSAT.add_column(DBColumn('PeakName', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('PeakId', datatype='uniqueidentifier', key='primary'))
PeakAboveSAT.add_column(DBColumn('Date', datatype='date'))
PeakAboveSAT.add_column(DBColumn('WeekNumber', datatype='int'))
PeakAboveSAT.add_column(DBColumn('Disposition', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('LocalTime', datatype='datetime'))
PeakAboveSAT.add_column(DBColumn('BoundaryName', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('Region', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('SubRegion', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('Plant', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('EmissionRate', datatype='float'))
PeakAboveSAT.add_column(DBColumn('PeakGpsLatitude', datatype='float'))
PeakAboveSAT.add_column(DBColumn('PeakGpsLongitude', datatype='float'))
PeakAboveSAT.add_column(DBColumn('Easting', datatype='float'))
PeakAboveSAT.add_column(DBColumn('Northing', datatype='float'))
PeakAboveSAT.add_column(DBColumn('UserName', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('SurveyorUnit', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('AnalyzerSerialNumber', datatype='nvarchar'))
PeakAboveSAT.add_column(DBColumn('Hyperlink', datatype='nvarchar')) 
PeakAboveSAT.add_column(DBColumn('LastUpdated', datatype='datetime'))
