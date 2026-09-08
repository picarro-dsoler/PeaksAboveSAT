from .PicarroDBClass import DBColumn, DBTable
#Table 1/172: __MigrationHistory
__MigrationHistory = DBTable('__MigrationHistory')
__MigrationHistory.add_column(DBColumn('MigrationId', datatype='nvarchar'))
__MigrationHistory.add_column(DBColumn('ContextKey', datatype='nvarchar'))
__MigrationHistory.add_column(DBColumn('Model', datatype='varbinary'))
__MigrationHistory.add_column(DBColumn('ProductVersion', datatype='nvarchar'))

#Table 2/172: AnalyticsPeakArchive
AnalyticsPeakArchive = DBTable('AnalyticsPeakArchive')
AnalyticsPeakArchive.add_column(DBColumn('ReportPeakId', datatype='uniqueidentifier'))
AnalyticsPeakArchive.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
AnalyticsPeakArchive.add_column(DBColumn('EmissionRate', datatype='float'))
AnalyticsPeakArchive.add_column(DBColumn('EmissionRateUncertainty', datatype='float'))
AnalyticsPeakArchive.add_column(DBColumn('NumberOfPeaks', datatype='int'))
AnalyticsPeakArchive.add_column(DBColumn('NumberOfPasses', datatype='int'))
AnalyticsPeakArchive.add_column(DBColumn('DetectionProbability', datatype='float'))
AnalyticsPeakArchive.add_column(DBColumn('MedianPairwiseDistance', datatype='float'))
AnalyticsPeakArchive.add_column(DBColumn('PriorityScore', datatype='float'))
AnalyticsPeakArchive.add_column(DBColumn('RankingGroup', datatype='int'))
AnalyticsPeakArchive.add_column(DBColumn('IsFiltered', datatype='bit'))

#Table 3/172: Analyzer
Analyzer = DBTable('Analyzer')
Analyzer.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Analyzer.add_column(DBColumn('SurveyorUnitId', datatype='uniqueidentifier'))
Analyzer.add_column(DBColumn('SerialNumber', datatype='nvarchar'))
Analyzer.add_column(DBColumn('SharedKey', datatype='nvarchar'))
Analyzer.add_column(DBColumn('HostVersion', datatype='nvarchar'))

#Table 4/172: AnalyzerAlarmLog
AnalyzerAlarmLog = DBTable('AnalyzerAlarmLog')
AnalyzerAlarmLog.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AnalyzerAlarmLog.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnalyzerAlarmLog.add_column(DBColumn('Message', datatype='nvarchar'))
AnalyzerAlarmLog.add_column(DBColumn('MessageDate', datatype='datetime'))
AnalyzerAlarmLog.add_column(DBColumn('CreateDate', datatype='datetime'))

#Table 5/172: AnalyzerHardwareCapabilityType
AnalyzerHardwareCapabilityType = DBTable('AnalyzerHardwareCapabilityType')
AnalyzerHardwareCapabilityType.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnalyzerHardwareCapabilityType.add_column(DBColumn('HardwareCapabilityTypeId', datatype='int'))

#Table 6/172: AnalyzerHeartbeat
AnalyzerHeartbeat = DBTable('AnalyzerHeartbeat')
AnalyzerHeartbeat.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnalyzerHeartbeat.add_column(DBColumn('GpsLatitude', datatype='float'))
AnalyzerHeartbeat.add_column(DBColumn('GpsLongitude', datatype='float'))
AnalyzerHeartbeat.add_column(DBColumn('IpAddress', datatype='nvarchar'))
AnalyzerHeartbeat.add_column(DBColumn('GpsValid', datatype='bit'))
AnalyzerHeartbeat.add_column(DBColumn('BuildNumber', datatype='nvarchar'))
AnalyzerHeartbeat.add_column(DBColumn('EventDateTime', datatype='datetime'))
AnalyzerHeartbeat.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
AnalyzerHeartbeat.add_column(DBColumn('GpsBearing', datatype='float'))

#Table 7/172: AnalyzerLog
AnalyzerLog = DBTable('AnalyzerLog')
AnalyzerLog.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AnalyzerLog.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnalyzerLog.add_column(DBColumn('Message', datatype='nvarchar'))
AnalyzerLog.add_column(DBColumn('MessageDate', datatype='datetime'))

#Table 8/172: AnalyzerUpdateJob
AnalyzerUpdateJob = DBTable('AnalyzerUpdateJob')
AnalyzerUpdateJob.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AnalyzerUpdateJob.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnalyzerUpdateJob.add_column(DBColumn('EventDateTime', datatype='datetime'))
AnalyzerUpdateJob.add_column(DBColumn('UpgradeStatus', datatype='int'))
AnalyzerUpdateJob.add_column(DBColumn('AnalyzerVersion', datatype='nvarchar'))

#Table 9/172: AnemometerRaw
AnemometerRaw = DBTable('AnemometerRaw')
AnemometerRaw.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
AnemometerRaw.add_column(DBColumn('EpochTime', datatype='float'))
AnemometerRaw.add_column(DBColumn('WindSpeedLateral', datatype='float'))
AnemometerRaw.add_column(DBColumn('WindSpeedLongitudinal', datatype='float'))
AnemometerRaw.add_column(DBColumn('Status', datatype='float'))

#Table 10/172: AssetBoxMetadata
AssetBoxMetadata = DBTable('AssetBoxMetadata')
AssetBoxMetadata.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AssetBoxMetadata.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
AssetBoxMetadata.add_column(DBColumn('Material', datatype='varchar'))
AssetBoxMetadata.add_column(DBColumn('OperatingPressure', datatype='varchar'))
AssetBoxMetadata.add_column(DBColumn('MeasuredLength', datatype='float'))

#Table 11/172: AssetFovMetadata
AssetFovMetadata = DBTable('AssetFovMetadata')
AssetFovMetadata.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AssetFovMetadata.add_column(DBColumn('FovId', datatype='uniqueidentifier'))
AssetFovMetadata.add_column(DBColumn('Material', datatype='varchar'))
AssetFovMetadata.add_column(DBColumn('OperatingPressure', datatype='varchar'))
AssetFovMetadata.add_column(DBColumn('MeasuredLength', datatype='float'))

#Table 12/172: AssetHighlightingTypes
AssetHighlightingTypes = DBTable('AssetHighlightingTypes')
AssetHighlightingTypes.add_column(DBColumn('Id', datatype='int'))
AssetHighlightingTypes.add_column(DBColumn('Name', datatype='nvarchar'))
AssetHighlightingTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 13/172: AssetType
AssetType = DBTable('AssetType')
AssetType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AssetType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 14/172: AuditLog
AuditLog = DBTable('AuditLog')
AuditLog.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AuditLog.add_column(DBColumn('TableId', datatype='nvarchar'))
AuditLog.add_column(DBColumn('InstanceId', datatype='nvarchar'))
AuditLog.add_column(DBColumn('ChangeDescription', datatype='nvarchar'))
AuditLog.add_column(DBColumn('ChangeBy', datatype='nvarchar'))
AuditLog.add_column(DBColumn('ChangeDate', datatype='datetime'))

#Table 15/172: AutomatedEmissionSource
AutomatedEmissionSource = DBTable('AutomatedEmissionSource')
AutomatedEmissionSource.add_column(DBColumn('Id', datatype='uniqueidentifier'))
AutomatedEmissionSource.add_column(DBColumn('CH4', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('DetectionProbability', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRate', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateAMean', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateAStd', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateGMean', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateGStd', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateLowerBound', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EmissionRateUpperBound', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EthaneRatio', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('EthaneRatioUncertainty', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('GeocodeAddress', datatype='nvarchar'))
AutomatedEmissionSource.add_column(DBColumn('GpsLatitude', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('GpsLongitude', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('Lisa', datatype='geometry'))
AutomatedEmissionSource.add_column(DBColumn('MaxAmplitude', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('MaxCarSpeed', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('MaxWindSpeed', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('MinWindSpeed', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('NumberOfPasses', datatype='int'))
AutomatedEmissionSource.add_column(DBColumn('NumberOfPeaks', datatype='int'))
AutomatedEmissionSource.add_column(DBColumn('PriorityScore', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('ProbMassCompressedArray', datatype='varbinary'))
AutomatedEmissionSource.add_column(DBColumn('ProbMassScale', datatype='int'))
AutomatedEmissionSource.add_column(DBColumn('RepresentativePeakId', datatype='uniqueidentifier'))
AutomatedEmissionSource.add_column(DBColumn('MostRecentSurveyTime', datatype='datetime'))
AutomatedEmissionSource.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
AutomatedEmissionSource.add_column(DBColumn('PeakFirstEpoch', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('PeakLastEpoch', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('SurveyModeTypeId', datatype='uniqueidentifier'))
AutomatedEmissionSource.add_column(DBColumn('Disposition', datatype='smallint'))
AutomatedEmissionSource.add_column(DBColumn('ClassificationConfidence', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('RepresentativeEmissionRate', datatype='float'))
AutomatedEmissionSource.add_column(DBColumn('RepresentativeBinLabel', datatype='nvarchar'))
AutomatedEmissionSource.add_column(DBColumn('IsBelowThresholdRandomlySelected', datatype='bit'))

#Table 16/172: AutomatedInvalidPeak
AutomatedInvalidPeak = DBTable('AutomatedInvalidPeak')
AutomatedInvalidPeak.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))
AutomatedInvalidPeak.add_column(DBColumn('QAFlag', datatype='int'))

#Table 17/172: Backup_InvestigationTemplateItem_Table
Backup_InvestigationTemplateItem_Table = DBTable('Backup_InvestigationTemplateItem_Table')
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('Id', datatype='int'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('InvestigationTemplateId', datatype='int'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('MasterInvestigationItemId', datatype='int'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('CustomLabel', datatype='nvarchar'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('CustomPlaceholder', datatype='nvarchar'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('Sequence', datatype='int'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('Required', datatype='bit'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('CreatedDate', datatype='datetime'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
Backup_InvestigationTemplateItem_Table.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 18/172: Backup_MasterInvestigationItem_Table
Backup_MasterInvestigationItem_Table = DBTable('Backup_MasterInvestigationItem_Table')
Backup_MasterInvestigationItem_Table.add_column(DBColumn('Id', datatype='int'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('Label', datatype='nvarchar'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('InvestigationDataTypeId', datatype='int'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('ValueOptions', datatype='nvarchar'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('PlaceHolder', datatype='nvarchar'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('CreatedDate', datatype='datetime'))
Backup_MasterInvestigationItem_Table.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 19/172: BaseMapType
BaseMapType = DBTable('BaseMapType')
BaseMapType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
BaseMapType.add_column(DBColumn('Description', datatype='nvarchar'))
BaseMapType.add_column(DBColumn('ResourceName', datatype='varchar'))

#Table 20/172: Box
Box = DBTable('Box')
Box.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Box.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
Box.add_column(DBColumn('BoxNumber', datatype='nvarchar'))
Box.add_column(DBColumn('BoxTypeId', datatype='int'))
Box.add_column(DBColumn('BoxShape', datatype='geometry'))
Box.add_column(DBColumn('AssetShape', datatype='geometry'))
Box.add_column(DBColumn('InvestigationDateTime', datatype='datetime'))
Box.add_column(DBColumn('InvestigationCompleteDateTime', datatype='datetime'))
Box.add_column(DBColumn('InvestigationStatusTypeId', datatype='int'))
Box.add_column(DBColumn('CantGetIn', datatype='nvarchar'))
Box.add_column(DBColumn('ReportPeakId', datatype='uniqueidentifier'))
Box.add_column(DBColumn('EmissionSourceId', datatype='uniqueidentifier'))
Box.add_column(DBColumn('UniqueIdentifier', datatype='nvarchar'))
Box.add_column(DBColumn('SyncTime', datatype='datetime'))

#Table 21/172: BoxTransferStatus
BoxTransferStatus = DBTable('BoxTransferStatus')
BoxTransferStatus.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
BoxTransferStatus.add_column(DBColumn('ExternalSystemId', datatype='uniqueidentifier'))
BoxTransferStatus.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
BoxTransferStatus.add_column(DBColumn('CreatedDate', datatype='datetime'))
BoxTransferStatus.add_column(DBColumn('UpdatedDate', datatype='datetime'))
BoxTransferStatus.add_column(DBColumn('OTAStatusTypeId', datatype='int'))

#Table 22/172: BoxTypes
BoxTypes = DBTable('BoxTypes')
BoxTypes.add_column(DBColumn('Id', datatype='int'))
BoxTypes.add_column(DBColumn('Name', datatype='nvarchar'))
BoxTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 23/172: CaptureAnalysisDispositionTypes
CaptureAnalysisDispositionTypes = DBTable('CaptureAnalysisDispositionTypes')
CaptureAnalysisDispositionTypes.add_column(DBColumn('Id', datatype='int'))
CaptureAnalysisDispositionTypes.add_column(DBColumn('Name', datatype='nvarchar'))
CaptureAnalysisDispositionTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 24/172: CaptureEvent
CaptureEvent = DBTable('CaptureEvent')
CaptureEvent.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CaptureEvent.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
CaptureEvent.add_column(DBColumn('EpochTime', datatype='float'))
CaptureEvent.add_column(DBColumn('DateTime', datatype='datetime'))
CaptureEvent.add_column(DBColumn('GpsLatitude', datatype='float'))
CaptureEvent.add_column(DBColumn('GpsLongitude', datatype='float'))
CaptureEvent.add_column(DBColumn('Shape', datatype='geometry'))
CaptureEvent.add_column(DBColumn('Disposition', datatype='int'))
CaptureEvent.add_column(DBColumn('Delta', datatype='float'))
CaptureEvent.add_column(DBColumn('Concentration', datatype='float'))
CaptureEvent.add_column(DBColumn('Uncertainty', datatype='float'))
CaptureEvent.add_column(DBColumn('CaptureType', datatype='bit'))
CaptureEvent.add_column(DBColumn('Distance', datatype='float'))
CaptureEvent.add_column(DBColumn('ReplayMax', datatype='float'))
CaptureEvent.add_column(DBColumn('ReplayLMin', datatype='float'))
CaptureEvent.add_column(DBColumn('ReplayRMin', datatype='float'))
CaptureEvent.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
CaptureEvent.add_column(DBColumn('EthaneRatio', datatype='float'))
CaptureEvent.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
CaptureEvent.add_column(DBColumn('ClassificationConfidence', datatype='float'))

#Table 25/172: ClientJSLog
ClientJSLog = DBTable('ClientJSLog')
ClientJSLog.add_column(DBColumn('Id', datatype='bigint'))
ClientJSLog.add_column(DBColumn('EpochTime', datatype='float'))
ClientJSLog.add_column(DBColumn('SerialNumber', datatype='nvarchar'))
ClientJSLog.add_column(DBColumn('Type', datatype='nvarchar'))
ClientJSLog.add_column(DBColumn('Level', datatype='nvarchar'))
ClientJSLog.add_column(DBColumn('Message', datatype='nvarchar'))
ClientJSLog.add_column(DBColumn('UserName', datatype='nvarchar'))
ClientJSLog.add_column(DBColumn('ClientGuid', datatype='nvarchar'))

#Table 26/172: ClusteringTypes
ClusteringTypes = DBTable('ClusteringTypes')
ClusteringTypes.add_column(DBColumn('Id', datatype='int'))
ClusteringTypes.add_column(DBColumn('Name', datatype='nvarchar'))
ClusteringTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 27/172: Culture
Culture = DBTable('Culture')
Culture.add_column(DBColumn('Id', datatype='varchar'))
Culture.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 28/172: Customer
Customer = DBTable('Customer')
Customer.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Customer.add_column(DBColumn('Name', datatype='nvarchar'))
Customer.add_column(DBColumn('Eula', datatype='nvarchar'))
Customer.add_column(DBColumn('Active', datatype='bit'))
Customer.add_column(DBColumn('NumberOfPreviousPasswordsToSave', datatype='int'))
Customer.add_column(DBColumn('PasswordRotationDuration', datatype='int'))
Customer.add_column(DBColumn('ValidDomainNames', datatype='nvarchar'))
Customer.add_column(DBColumn('IdentityProviderAlias', datatype='nvarchar'))
Customer.add_column(DBColumn('UnitMeasurementDistanceId', datatype='uniqueidentifier'))
Customer.add_column(DBColumn('UnitMeasurementFlowId', datatype='uniqueidentifier'))
Customer.add_column(DBColumn('UnitMeasurementSpeedId', datatype='uniqueidentifier'))
Customer.add_column(DBColumn('ExpectedDrivingShiftRangeStart', datatype='varchar'))
Customer.add_column(DBColumn('ExpectedDrivingShiftRangeEnd', datatype='varchar'))
Customer.add_column(DBColumn('DrivingDaysInWeek', datatype='int'))
Customer.add_column(DBColumn('ExpectedMainCoverage', datatype='float'))
Customer.add_column(DBColumn('DefaultSurveyType', datatype='varchar'))
Customer.add_column(DBColumn('DateFormat', datatype='varchar'))
Customer.add_column(DBColumn('TimeFormat', datatype='varchar'))

#Table 29/172: CUSTOMER_20231221
CUSTOMER_20231221 = DBTable('CUSTOMER_20231221')
CUSTOMER_20231221.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CUSTOMER_20231221.add_column(DBColumn('Name', datatype='nvarchar'))
CUSTOMER_20231221.add_column(DBColumn('Eula', datatype='nvarchar'))
CUSTOMER_20231221.add_column(DBColumn('Active', datatype='bit'))
CUSTOMER_20231221.add_column(DBColumn('NumberOfPreviousPasswordsToSave', datatype='int'))
CUSTOMER_20231221.add_column(DBColumn('PasswordRotationDuration', datatype='int'))
CUSTOMER_20231221.add_column(DBColumn('ValidDomainNames', datatype='nvarchar'))
CUSTOMER_20231221.add_column(DBColumn('IdentityProviderAlias', datatype='nvarchar'))
CUSTOMER_20231221.add_column(DBColumn('UnitMeasurementDistanceId', datatype='uniqueidentifier'))
CUSTOMER_20231221.add_column(DBColumn('UnitMeasurementFlowId', datatype='uniqueidentifier'))
CUSTOMER_20231221.add_column(DBColumn('UnitMeasurementSpeedId', datatype='uniqueidentifier'))

#Table 30/172: CustomerBoundaryType_20231013
CustomerBoundaryType_20231013 = DBTable('CustomerBoundaryType_20231013')
CustomerBoundaryType_20231013.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerBoundaryType_20231013.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerBoundaryType_20231013.add_column(DBColumn('FeatureClassDescription', datatype='nvarchar'))
CustomerBoundaryType_20231013.add_column(DBColumn('Color', datatype='nvarchar'))
CustomerBoundaryType_20231013.add_column(DBColumn('LineWeight', datatype='smallint'))
CustomerBoundaryType_20231013.add_column(DBColumn('IsDotted', datatype='bit'))
CustomerBoundaryType_20231013.add_column(DBColumn('Zoomlevel', datatype='smallint'))
CustomerBoundaryType_20231013.add_column(DBColumn('IsReportable', datatype='bit'))

#Table 31/172: CustomerDashboard
CustomerDashboard = DBTable('CustomerDashboard')
CustomerDashboard.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerDashboard.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerDashboard.add_column(DBColumn('Name', datatype='nvarchar'))
CustomerDashboard.add_column(DBColumn('URL', datatype='nvarchar'))
CustomerDashboard.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerDashboard.add_column(DBColumn('SecretKey', datatype='nvarchar'))
CustomerDashboard.add_column(DBColumn('IsActive', datatype='bit'))
CustomerDashboard.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerDashboard.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
CustomerDashboard.add_column(DBColumn('ImageURL', datatype='nvarchar'))
CustomerDashboard.add_column(DBColumn('Sequence', datatype='int'))

#Table 32/172: CustomerDashboard_20250630
CustomerDashboard_20250630 = DBTable('CustomerDashboard_20250630')
CustomerDashboard_20250630.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerDashboard_20250630.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerDashboard_20250630.add_column(DBColumn('Name', datatype='nvarchar'))
CustomerDashboard_20250630.add_column(DBColumn('URL', datatype='nvarchar'))
CustomerDashboard_20250630.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerDashboard_20250630.add_column(DBColumn('SecretKey', datatype='nvarchar'))
CustomerDashboard_20250630.add_column(DBColumn('IsActive', datatype='bit'))
CustomerDashboard_20250630.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerDashboard_20250630.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
CustomerDashboard_20250630.add_column(DBColumn('ImageURL', datatype='nvarchar'))
CustomerDashboard_20250630.add_column(DBColumn('Sequence', datatype='int'))

#Table 33/172: CustomerDashBoard_DEVOPS_6332
CustomerDashBoard_DEVOPS_6332 = DBTable('CustomerDashBoard_DEVOPS_6332')
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('Name', datatype='nvarchar'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('URL', datatype='nvarchar'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('SecretKey', datatype='nvarchar'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('IsActive', datatype='bit'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('ImageURL', datatype='nvarchar'))
CustomerDashBoard_DEVOPS_6332.add_column(DBColumn('Sequence', datatype='int'))

#Table 34/172: CustomerDashboard_DEVOPS_6448
CustomerDashboard_DEVOPS_6448 = DBTable('CustomerDashboard_DEVOPS_6448')
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('Name', datatype='nvarchar'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('URL', datatype='nvarchar'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('SecretKey', datatype='nvarchar'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('IsActive', datatype='bit'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('ImageURL', datatype='nvarchar'))
CustomerDashboard_DEVOPS_6448.add_column(DBColumn('Sequence', datatype='int'))

#Table 35/172: CustomerIdentityProvider
CustomerIdentityProvider = DBTable('CustomerIdentityProvider')
CustomerIdentityProvider.add_column(DBColumn('Id', datatype='int'))
CustomerIdentityProvider.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerIdentityProvider.add_column(DBColumn('Name', datatype='nvarchar'))
CustomerIdentityProvider.add_column(DBColumn('IDPName', datatype='nvarchar'))
CustomerIdentityProvider.add_column(DBColumn('Active', datatype='bit'))
CustomerIdentityProvider.add_column(DBColumn('LogoutUrl', datatype='nvarchar'))
CustomerIdentityProvider.add_column(DBColumn('CreatedDate', datatype='datetime'))

#Table 36/172: CustomerLicensedFeatureOptions
CustomerLicensedFeatureOptions = DBTable('CustomerLicensedFeatureOptions')
CustomerLicensedFeatureOptions.add_column(DBColumn('LicensedFeatureOptionId', datatype='uniqueidentifier'))
CustomerLicensedFeatureOptions.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))

#Table 37/172: CustomerLicensedFeatureOptions_20240327
CustomerLicensedFeatureOptions_20240327 = DBTable('CustomerLicensedFeatureOptions_20240327')
CustomerLicensedFeatureOptions_20240327.add_column(DBColumn('LicensedFeatureOptionId', datatype='uniqueidentifier'))
CustomerLicensedFeatureOptions_20240327.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))

#Table 38/172: CustomerMaterialType_20231013
CustomerMaterialType_20231013 = DBTable('CustomerMaterialType_20231013')
CustomerMaterialType_20231013.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerMaterialType_20231013.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerMaterialType_20231013.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerMaterialType_20231013.add_column(DBColumn('Color', datatype='nvarchar'))
CustomerMaterialType_20231013.add_column(DBColumn('LineWeight', datatype='smallint'))
CustomerMaterialType_20231013.add_column(DBColumn('IsDotted', datatype='bit'))

#Table 39/172: CustomerSurveyorMapping
CustomerSurveyorMapping = DBTable('CustomerSurveyorMapping')
CustomerSurveyorMapping.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMapping.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerSurveyorMapping.add_column(DBColumn('SurveyorUnitId', datatype='uniqueidentifier'))
CustomerSurveyorMapping.add_column(DBColumn('Description', datatype='nvarchar'))
CustomerSurveyorMapping.add_column(DBColumn('Active', datatype='bit'))
CustomerSurveyorMapping.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerSurveyorMapping.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
CustomerSurveyorMapping.add_column(DBColumn('ParameterTypeId', datatype='int'))

#Table 40/172: CustomerSurveyorMasterParameterMapping
CustomerSurveyorMasterParameterMapping = DBTable('CustomerSurveyorMasterParameterMapping')
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('CustomerSurveyorMappingId', datatype='int'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('MasterParameterId', datatype='int'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('Value1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('Value2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('UpdatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMapping.add_column(DBColumn('UpdatedBy', datatype='uniqueidentifier'))

#Table 41/172: CustomerSurveyorMasterParameterMapping_20240327
CustomerSurveyorMasterParameterMapping_20240327 = DBTable('CustomerSurveyorMasterParameterMapping_20240327')
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('CustomerSurveyorMappingId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('MasterParameterId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('Value1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('Value2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('UpdatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMapping_20240327.add_column(DBColumn('UpdatedBy', datatype='uniqueidentifier'))

#Table 42/172: CustomerSurveyorMasterParameterMapping_20240327_RRA
CustomerSurveyorMasterParameterMapping_20240327_RRA = DBTable('CustomerSurveyorMasterParameterMapping_20240327_RRA')
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('CustomerSurveyorMappingId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('MasterParameterId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('Value1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('Value2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('UpdatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMapping_20240327_RRA.add_column(DBColumn('UpdatedBy', datatype='uniqueidentifier'))

#Table 43/172: CustomerSurveyorMasterParameterMapping_20250425
CustomerSurveyorMasterParameterMapping_20250425 = DBTable('CustomerSurveyorMasterParameterMapping_20250425')
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('CustomerSurveyorMappingId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('MasterParameterId', datatype='int'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('Value1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('Value2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('UpdatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMapping_20250425.add_column(DBColumn('UpdatedBy', datatype='uniqueidentifier'))

#Table 44/172: CustomerSurveyorMasterParameterMappingHistory
CustomerSurveyorMasterParameterMappingHistory = DBTable('CustomerSurveyorMasterParameterMappingHistory')
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('CustomerSurveyorMasterParameterMappingId', datatype='int'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('OldValue1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('OldValue2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('NewValue1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('NewValue2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMappingHistory.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))

#Table 45/172: CustomerSurveyorMasterParameterMappingHistory_20240327
CustomerSurveyorMasterParameterMappingHistory_20240327 = DBTable('CustomerSurveyorMasterParameterMappingHistory_20240327')
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('Id', datatype='int'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('CustomerSurveyorMasterParameterMappingId', datatype='int'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('OldValue1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('OldValue2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('NewValue1', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('NewValue2', datatype='nvarchar'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('CreatedDate', datatype='datetime'))
CustomerSurveyorMasterParameterMappingHistory_20240327.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))

#Table 46/172: CustomerViewConfiguration
CustomerViewConfiguration = DBTable('CustomerViewConfiguration')
CustomerViewConfiguration.add_column(DBColumn('Id', datatype='uniqueidentifier'))
CustomerViewConfiguration.add_column(DBColumn('ViewConfigId', datatype='uniqueidentifier'))
CustomerViewConfiguration.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
CustomerViewConfiguration.add_column(DBColumn('Value', datatype='decimal'))

#Table 47/172: EmissionSource
EmissionSource = DBTable('EmissionSource')
EmissionSource.add_column(DBColumn('Id', datatype='uniqueidentifier'))
EmissionSource.add_column(DBColumn('CH4', datatype='float'))
EmissionSource.add_column(DBColumn('ClassificationConfidence', datatype='float'))
EmissionSource.add_column(DBColumn('Disposition', datatype='int'))
EmissionSource.add_column(DBColumn('DetectionProbability', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRate', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateAMean', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateAStd', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateGMean', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateGStd', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateLowerBound', datatype='float'))
EmissionSource.add_column(DBColumn('EmissionRateUpperBound', datatype='float'))
EmissionSource.add_column(DBColumn('EthaneRatio', datatype='float'))
EmissionSource.add_column(DBColumn('EthaneRatioUncertainty', datatype='float'))
EmissionSource.add_column(DBColumn('GeocodeAddress', datatype='nvarchar'))
EmissionSource.add_column(DBColumn('GpsLatitude', datatype='float'))
EmissionSource.add_column(DBColumn('GpsLongitude', datatype='float'))
EmissionSource.add_column(DBColumn('IsFiltered', datatype='bit'))
EmissionSource.add_column(DBColumn('Lisa', datatype='geometry'))
EmissionSource.add_column(DBColumn('MaxAmplitude', datatype='float'))
EmissionSource.add_column(DBColumn('MaxCarSpeed', datatype='float'))
EmissionSource.add_column(DBColumn('MaxWindSpeed', datatype='float'))
EmissionSource.add_column(DBColumn('MinWindSpeed', datatype='float'))
EmissionSource.add_column(DBColumn('NumberOfPasses', datatype='int'))
EmissionSource.add_column(DBColumn('NumberOfPeaks', datatype='int'))
EmissionSource.add_column(DBColumn('PeakNumber', datatype='int'))
EmissionSource.add_column(DBColumn('PriorityScore', datatype='float'))
EmissionSource.add_column(DBColumn('RankingGroup', datatype='int'))
EmissionSource.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
EmissionSource.add_column(DBColumn('RepresentativePeakId', datatype='uniqueidentifier'))
EmissionSource.add_column(DBColumn('ProbMassCompressedArray', datatype='varbinary'))
EmissionSource.add_column(DBColumn('ProbMassScale', datatype='int'))
EmissionSource.add_column(DBColumn('RepresentativeEmissionRate', datatype='float'))
EmissionSource.add_column(DBColumn('RepresentativeBinLabel', datatype='nvarchar'))
EmissionSource.add_column(DBColumn('IsBelowThresholdRandomlySelected', datatype='bit'))
EmissionSource.add_column(DBColumn('UniqueIdentifier', datatype='nvarchar'))
EmissionSource.add_column(DBColumn('PriorityScore2', datatype='float'))

#Table 48/172: EmissionSourceRiskScoreMeta
EmissionSourceRiskScoreMeta = DBTable('EmissionSourceRiskScoreMeta')
EmissionSourceRiskScoreMeta.add_column(DBColumn('EmissionSourceId', datatype='uniqueidentifier'))
EmissionSourceRiskScoreMeta.add_column(DBColumn('Metadata', datatype='nvarchar'))
EmissionSourceRiskScoreMeta.add_column(DBColumn('HtmlOutput', datatype='nvarchar'))

#Table 49/172: EQConfidenceGroup
EQConfidenceGroup = DBTable('EQConfidenceGroup')
EQConfidenceGroup.add_column(DBColumn('ConfidenceGroup', datatype='int'))
EQConfidenceGroup.add_column(DBColumn('Description', datatype='nvarchar'))
EQConfidenceGroup.add_column(DBColumn('Color', datatype='nvarchar'))

#Table 50/172: EQInvalidPeakArchive
EQInvalidPeakArchive = DBTable('EQInvalidPeakArchive')
EQInvalidPeakArchive.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
EQInvalidPeakArchive.add_column(DBColumn('EQPeakSurveyId', datatype='uniqueidentifier'))
EQInvalidPeakArchive.add_column(DBColumn('EQPeakEpochTime', datatype='float'))
EQInvalidPeakArchive.add_column(DBColumn('QAFlag', datatype='int'))

#Table 51/172: EQPeakArchive
EQPeakArchive = DBTable('EQPeakArchive')
EQPeakArchive.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
EQPeakArchive.add_column(DBColumn('EpochTime', datatype='float'))
EQPeakArchive.add_column(DBColumn('MeasurementType', datatype='smallint'))
EQPeakArchive.add_column(DBColumn('Latitude', datatype='float'))
EQPeakArchive.add_column(DBColumn('Longitude', datatype='float'))
EQPeakArchive.add_column(DBColumn('MaxCH4', datatype='float'))
EQPeakArchive.add_column(DBColumn('Amplitude', datatype='float'))
EQPeakArchive.add_column(DBColumn('Width', datatype='float'))
EQPeakArchive.add_column(DBColumn('Variation', datatype='float'))
EQPeakArchive.add_column(DBColumn('Duration', datatype='float'))
EQPeakArchive.add_column(DBColumn('LineIntegral', datatype='float'))
EQPeakArchive.add_column(DBColumn('EmissionRate', datatype='float'))
EQPeakArchive.add_column(DBColumn('EmissionRateUncertainty', datatype='float'))
EQPeakArchive.add_column(DBColumn('ProbA', datatype='float'))
EQPeakArchive.add_column(DBColumn('ProbX0', datatype='float'))
EQPeakArchive.add_column(DBColumn('ProbThreshold', datatype='float'))
EQPeakArchive.add_column(DBColumn('EpochPlumeStart', datatype='float'))
EQPeakArchive.add_column(DBColumn('EpochPlumeEnd', datatype='float'))
EQPeakArchive.add_column(DBColumn('MedianCarSpeed', datatype='float'))
EQPeakArchive.add_column(DBColumn('StdDevCarSpeed', datatype='float'))
EQPeakArchive.add_column(DBColumn('MinimumCarSpeed', datatype='float'))
EQPeakArchive.add_column(DBColumn('MaximumCarSpeed', datatype='float'))
EQPeakArchive.add_column(DBColumn('Shape', datatype='geometry'))
EQPeakArchive.add_column(DBColumn('EthaneRatio', datatype='float'))
EQPeakArchive.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
EQPeakArchive.add_column(DBColumn('EthyleneRatio', datatype='float'))
EQPeakArchive.add_column(DBColumn('EthyleneRatioSdev', datatype='float'))
EQPeakArchive.add_column(DBColumn('Disposition', datatype='int'))
EQPeakArchive.add_column(DBColumn('ClassificationConfidence', datatype='float'))

#Table 52/172: EQPeakWindMetricArchive
EQPeakWindMetricArchive = DBTable('EQPeakWindMetricArchive')
EQPeakWindMetricArchive.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
EQPeakWindMetricArchive.add_column(DBColumn('EpochTime', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MedianWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('StdDevWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MeanWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MinimumWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MaximumWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MeanLateralWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MedianLateralWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('StdDevLateralWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MinimumLateralWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MaximumLateralWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MedianWindDir', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MedianCarWindAngle', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('StdDevCarWindAngle', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MedianLongWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('StdDevLongWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MeanLongWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MinLongWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MaxLongWindSpeed', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('StdDevWindDir', datatype='float'))
EQPeakWindMetricArchive.add_column(DBColumn('MeanWindDir', datatype='float'))

#Table 53/172: EQSourceArchive
EQSourceArchive = DBTable('EQSourceArchive')
EQSourceArchive.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
EQSourceArchive.add_column(DBColumn('EmissionRank', datatype='int'))
EQSourceArchive.add_column(DBColumn('EmissionRate', datatype='float'))
EQSourceArchive.add_column(DBColumn('Latitude', datatype='float'))
EQSourceArchive.add_column(DBColumn('Longitude', datatype='float'))
EQSourceArchive.add_column(DBColumn('EmissionRateAMean', datatype='float'))
EQSourceArchive.add_column(DBColumn('EmissionRateAStd', datatype='float'))
EQSourceArchive.add_column(DBColumn('EmissionRateGMean', datatype='float'))
EQSourceArchive.add_column(DBColumn('EmissionRateGStd', datatype='float'))
EQSourceArchive.add_column(DBColumn('PriorScale', datatype='float'))
EQSourceArchive.add_column(DBColumn('PriorScaleWeight', datatype='float'))
EQSourceArchive.add_column(DBColumn('WindDirection', datatype='float'))
EQSourceArchive.add_column(DBColumn('WindDirectionStdDev', datatype='float'))
EQSourceArchive.add_column(DBColumn('CarSpeed', datatype='float'))
EQSourceArchive.add_column(DBColumn('WindSpeed', datatype='float'))
EQSourceArchive.add_column(DBColumn('AggregatedEthaneRatio', datatype='float'))
EQSourceArchive.add_column(DBColumn('AggregatedEthaneRatioSdev', datatype='float'))
EQSourceArchive.add_column(DBColumn('AggregatedDisposition', datatype='int'))
EQSourceArchive.add_column(DBColumn('AggregatedClassificationConfidence', datatype='float'))
EQSourceArchive.add_column(DBColumn('Address', datatype='nvarchar'))
EQSourceArchive.add_column(DBColumn('NumberOfPeaks', datatype='int'))
EQSourceArchive.add_column(DBColumn('NumberOfPasses', datatype='int'))
EQSourceArchive.add_column(DBColumn('EmissionRateLowerBound', datatype='float'))
EQSourceArchive.add_column(DBColumn('EmissionRateUpperBound', datatype='float'))

#Table 54/172: EQSourceComparisonArchive
EQSourceComparisonArchive = DBTable('EQSourceComparisonArchive')
EQSourceComparisonArchive.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
EQSourceComparisonArchive.add_column(DBColumn('LeftRank', datatype='int'))
EQSourceComparisonArchive.add_column(DBColumn('RightRank', datatype='int'))
EQSourceComparisonArchive.add_column(DBColumn('Probability', datatype='float'))

#Table 55/172: EQSourceEQPeakArchive
EQSourceEQPeakArchive = DBTable('EQSourceEQPeakArchive')
EQSourceEQPeakArchive.add_column(DBColumn('EQSourceReportId', datatype='uniqueidentifier'))
EQSourceEQPeakArchive.add_column(DBColumn('EQSourceEmissionRank', datatype='int'))
EQSourceEQPeakArchive.add_column(DBColumn('EQPeakSurveyId', datatype='uniqueidentifier'))
EQSourceEQPeakArchive.add_column(DBColumn('EQPeakEpochTime', datatype='float'))

#Table 56/172: EthaneAnalysisDispositionTypes
EthaneAnalysisDispositionTypes = DBTable('EthaneAnalysisDispositionTypes')
EthaneAnalysisDispositionTypes.add_column(DBColumn('Id', datatype='int'))
EthaneAnalysisDispositionTypes.add_column(DBColumn('Name', datatype='nvarchar'))
EthaneAnalysisDispositionTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 57/172: ExternalSystem
ExternalSystem = DBTable('ExternalSystem')
ExternalSystem.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ExternalSystem.add_column(DBColumn('Name', datatype='nvarchar'))
ExternalSystem.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 58/172: FieldDataType
FieldDataType = DBTable('FieldDataType')
FieldDataType.add_column(DBColumn('Id', datatype='int'))
FieldDataType.add_column(DBColumn('Name', datatype='nvarchar'))
FieldDataType.add_column(DBColumn('CreatedDate', datatype='datetime'))

#Table 59/172: FTPConfiguration
FTPConfiguration = DBTable('FTPConfiguration')
FTPConfiguration.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
FTPConfiguration.add_column(DBColumn('IpAddress', datatype='nvarchar'))
FTPConfiguration.add_column(DBColumn('UploadDirectory', datatype='nvarchar'))
FTPConfiguration.add_column(DBColumn('Username', datatype='nvarchar'))
FTPConfiguration.add_column(DBColumn('PrivateKey', datatype='nvarchar'))
FTPConfiguration.add_column(DBColumn('AutoUploadEnabled', datatype='bit'))
FTPConfiguration.add_column(DBColumn('DateModified', datatype='datetime'))

#Table 60/172: FTPLog
FTPLog = DBTable('FTPLog')
FTPLog.add_column(DBColumn('IpAddress', datatype='nvarchar'))
FTPLog.add_column(DBColumn('Username', datatype='nvarchar'))
FTPLog.add_column(DBColumn('UploadDirectory', datatype='nvarchar'))
FTPLog.add_column(DBColumn('UploadedOn', datatype='datetime'))
FTPLog.add_column(DBColumn('Id', datatype='uniqueidentifier'))
FTPLog.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))

#Table 61/172: GeoServerConfiguration
GeoServerConfiguration = DBTable('GeoServerConfiguration')
GeoServerConfiguration.add_column(DBColumn('Id', datatype='uniqueidentifier'))
GeoServerConfiguration.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
GeoServerConfiguration.add_column(DBColumn('GeoServerURL', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('WorkSpaceName', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('FeatureClassName', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('Description', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('IsActive', datatype='bit'))
GeoServerConfiguration.add_column(DBColumn('IsCustomerData', datatype='bit'))
GeoServerConfiguration.add_column(DBColumn('DataExtractDate', datatype='datetime'))
GeoServerConfiguration.add_column(DBColumn('APIVersion', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('UserName', datatype='nvarchar'))
GeoServerConfiguration.add_column(DBColumn('Password', datatype='nvarchar'))

#Table 62/172: GeoServerConfiguration_20231013
GeoServerConfiguration_20231013 = DBTable('GeoServerConfiguration_20231013')
GeoServerConfiguration_20231013.add_column(DBColumn('Id', datatype='uniqueidentifier'))
GeoServerConfiguration_20231013.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
GeoServerConfiguration_20231013.add_column(DBColumn('GeoServerURL', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('WorkSpaceName', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('FeatureClassName', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('Description', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('IsActive', datatype='bit'))
GeoServerConfiguration_20231013.add_column(DBColumn('IsCustomerData', datatype='bit'))
GeoServerConfiguration_20231013.add_column(DBColumn('DataExtractDate', datatype='datetime'))
GeoServerConfiguration_20231013.add_column(DBColumn('APIVersion', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('UserName', datatype='nvarchar'))
GeoServerConfiguration_20231013.add_column(DBColumn('Password', datatype='nvarchar'))

#Table 63/172: GPSRaw
GPSRaw = DBTable('GPSRaw')
GPSRaw.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
GPSRaw.add_column(DBColumn('EpochTime', datatype='float'))
GPSRaw.add_column(DBColumn('GpsTime', datatype='float'))
GPSRaw.add_column(DBColumn('GpsLatitude', datatype='float'))
GPSRaw.add_column(DBColumn('GpsLongitude', datatype='float'))
GPSRaw.add_column(DBColumn('GpsFit', datatype='smallint'))
GPSRaw.add_column(DBColumn('GPSLatitudeUncertainty', datatype='float'))
GPSRaw.add_column(DBColumn('GPSLongitudeUncertainty', datatype='float'))

#Table 64/172: HandheldTimeseriesCheckpoint
HandheldTimeseriesCheckpoint = DBTable('HandheldTimeseriesCheckpoint')
HandheldTimeseriesCheckpoint.add_column(DBColumn('Id', datatype='bigint'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('SerialNumber', datatype='varchar'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('SequenceNumber', datatype='bigint'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('Status', datatype='varchar'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('CreatedAt', datatype='datetime'))
HandheldTimeseriesCheckpoint.add_column(DBColumn('UpdatedAt', datatype='datetime'))

#Table 65/172: HardwareCapabilityTypes
HardwareCapabilityTypes = DBTable('HardwareCapabilityTypes')
HardwareCapabilityTypes.add_column(DBColumn('Id', datatype='int'))
HardwareCapabilityTypes.add_column(DBColumn('Name', datatype='nvarchar'))
HardwareCapabilityTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 66/172: Inlet
Inlet = DBTable('Inlet')
Inlet.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Inlet.add_column(DBColumn('SurveyorUnitId', datatype='uniqueidentifier'))
Inlet.add_column(DBColumn('FromDate', datatype='datetime'))
Inlet.add_column(DBColumn('BottomHeight', datatype='float'))
Inlet.add_column(DBColumn('TopHeight', datatype='float'))

#Table 67/172: InvalidPeak
InvalidPeak = DBTable('InvalidPeak')
InvalidPeak.add_column(DBColumn('Id', datatype='uniqueidentifier'))
InvalidPeak.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
InvalidPeak.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))
InvalidPeak.add_column(DBColumn('QAFlag', datatype='int'))

#Table 68/172: InvestigationAssignment
InvestigationAssignment = DBTable('InvestigationAssignment')
InvestigationAssignment.add_column(DBColumn('Id', datatype='uniqueidentifier'))
InvestigationAssignment.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
InvestigationAssignment.add_column(DBColumn('AssignerId', datatype='uniqueidentifier'))
InvestigationAssignment.add_column(DBColumn('AssigneeId', datatype='uniqueidentifier'))
InvestigationAssignment.add_column(DBColumn('AssignmentDateTime', datatype='datetime'))
InvestigationAssignment.add_column(DBColumn('IsActive', datatype='bit'))

#Table 69/172: InvestigationDataType
InvestigationDataType = DBTable('InvestigationDataType')
InvestigationDataType.add_column(DBColumn('Id', datatype='int'))
InvestigationDataType.add_column(DBColumn('DataType', datatype='nvarchar'))
InvestigationDataType.add_column(DBColumn('FieldLength', datatype='int'))
InvestigationDataType.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationDataType.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 70/172: InvestigationSession
InvestigationSession = DBTable('InvestigationSession')
InvestigationSession.add_column(DBColumn('Id', datatype='uniqueidentifier'))
InvestigationSession.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
InvestigationSession.add_column(DBColumn('SessionStart', datatype='datetime'))
InvestigationSession.add_column(DBColumn('SessionEnd', datatype='datetime'))
InvestigationSession.add_column(DBColumn('Breadcrumb', datatype='geometry'))
InvestigationSession.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
InvestigationSession.add_column(DBColumn('InvestigationDeviceSerialNumber', datatype='nvarchar'))
InvestigationSession.add_column(DBColumn('SessionId', datatype='uniqueidentifier'))
InvestigationSession.add_column(DBColumn('SyncTime', datatype='datetime'))

#Table 71/172: InvestigationStatusTypes
InvestigationStatusTypes = DBTable('InvestigationStatusTypes')
InvestigationStatusTypes.add_column(DBColumn('Id', datatype='int'))
InvestigationStatusTypes.add_column(DBColumn('Name', datatype='nvarchar'))
InvestigationStatusTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 72/172: InvestigationTemplate
InvestigationTemplate = DBTable('InvestigationTemplate')
InvestigationTemplate.add_column(DBColumn('Id', datatype='int'))
InvestigationTemplate.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
InvestigationTemplate.add_column(DBColumn('InvestigationTemplateTypeId', datatype='int'))
InvestigationTemplate.add_column(DBColumn('Active', datatype='bit'))
InvestigationTemplate.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationTemplate.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
InvestigationTemplate.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 73/172: InvestigationTemplateItem
InvestigationTemplateItem = DBTable('InvestigationTemplateItem')
InvestigationTemplateItem.add_column(DBColumn('Id', datatype='int'))
InvestigationTemplateItem.add_column(DBColumn('InvestigationTemplateId', datatype='int'))
InvestigationTemplateItem.add_column(DBColumn('MasterInvestigationItemId', datatype='int'))
InvestigationTemplateItem.add_column(DBColumn('CustomLabel', datatype='nvarchar'))
InvestigationTemplateItem.add_column(DBColumn('CustomPlaceholder', datatype='nvarchar'))
InvestigationTemplateItem.add_column(DBColumn('Sequence', datatype='int'))
InvestigationTemplateItem.add_column(DBColumn('Required', datatype='bit'))
InvestigationTemplateItem.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationTemplateItem.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
InvestigationTemplateItem.add_column(DBColumn('UpdatedDate', datatype='datetime'))
InvestigationTemplateItem.add_column(DBColumn('ValueOptions', datatype='nvarchar'))

#Table 74/172: InvestigationTemplateItem_20240910
InvestigationTemplateItem_20240910 = DBTable('InvestigationTemplateItem_20240910')
InvestigationTemplateItem_20240910.add_column(DBColumn('Id', datatype='int'))
InvestigationTemplateItem_20240910.add_column(DBColumn('InvestigationTemplateId', datatype='int'))
InvestigationTemplateItem_20240910.add_column(DBColumn('MasterInvestigationItemId', datatype='int'))
InvestigationTemplateItem_20240910.add_column(DBColumn('CustomLabel', datatype='nvarchar'))
InvestigationTemplateItem_20240910.add_column(DBColumn('CustomPlaceholder', datatype='nvarchar'))
InvestigationTemplateItem_20240910.add_column(DBColumn('Sequence', datatype='int'))
InvestigationTemplateItem_20240910.add_column(DBColumn('Required', datatype='bit'))
InvestigationTemplateItem_20240910.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationTemplateItem_20240910.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
InvestigationTemplateItem_20240910.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 75/172: InvestigationTemplateItem_20240919
InvestigationTemplateItem_20240919 = DBTable('InvestigationTemplateItem_20240919')
InvestigationTemplateItem_20240919.add_column(DBColumn('Id', datatype='int'))
InvestigationTemplateItem_20240919.add_column(DBColumn('InvestigationTemplateId', datatype='int'))
InvestigationTemplateItem_20240919.add_column(DBColumn('MasterInvestigationItemId', datatype='int'))
InvestigationTemplateItem_20240919.add_column(DBColumn('CustomLabel', datatype='nvarchar'))
InvestigationTemplateItem_20240919.add_column(DBColumn('CustomPlaceholder', datatype='nvarchar'))
InvestigationTemplateItem_20240919.add_column(DBColumn('Sequence', datatype='int'))
InvestigationTemplateItem_20240919.add_column(DBColumn('Required', datatype='bit'))
InvestigationTemplateItem_20240919.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationTemplateItem_20240919.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
InvestigationTemplateItem_20240919.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 76/172: InvestigationTemplateType
InvestigationTemplateType = DBTable('InvestigationTemplateType')
InvestigationTemplateType.add_column(DBColumn('Id', datatype='int'))
InvestigationTemplateType.add_column(DBColumn('Name', datatype='nvarchar'))
InvestigationTemplateType.add_column(DBColumn('CreatedDate', datatype='datetime'))
InvestigationTemplateType.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 77/172: IsotopicIdentity
IsotopicIdentity = DBTable('IsotopicIdentity')
IsotopicIdentity.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
IsotopicIdentity.add_column(DBColumn('FromDate', datatype='datetime'))
IsotopicIdentity.add_column(DBColumn('NoLowerBound', datatype='float'))
IsotopicIdentity.add_column(DBColumn('YesLowerBound', datatype='float'))
IsotopicIdentity.add_column(DBColumn('YesUpperBound', datatype='float'))
IsotopicIdentity.add_column(DBColumn('NoUpperBound', datatype='float'))

#Table 78/172: Label
Label = DBTable('Label')
Label.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Label.add_column(DBColumn('Title', datatype='nvarchar'))
Label.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
Label.add_column(DBColumn('Type', datatype='int'))
Label.add_column(DBColumn('CreatedDate', datatype='datetime'))
Label.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
Label.add_column(DBColumn('IsActive', datatype='bit'))

#Table 79/172: LeakLocationTypes
LeakLocationTypes = DBTable('LeakLocationTypes')
LeakLocationTypes.add_column(DBColumn('Id', datatype='int'))
LeakLocationTypes.add_column(DBColumn('Name', datatype='nvarchar'))
LeakLocationTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 80/172: LeakSourceTypes
LeakSourceTypes = DBTable('LeakSourceTypes')
LeakSourceTypes.add_column(DBColumn('Id', datatype='int'))
LeakSourceTypes.add_column(DBColumn('Name', datatype='nvarchar'))
LeakSourceTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 81/172: LeakTypes
LeakTypes = DBTable('LeakTypes')
LeakTypes.add_column(DBColumn('Id', datatype='int'))
LeakTypes.add_column(DBColumn('Name', datatype='nvarchar'))
LeakTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 82/172: LicensedFeature
LicensedFeature = DBTable('LicensedFeature')
LicensedFeature.add_column(DBColumn('Id', datatype='uniqueidentifier'))
LicensedFeature.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 83/172: LicensedFeature_20240327
LicensedFeature_20240327 = DBTable('LicensedFeature_20240327')
LicensedFeature_20240327.add_column(DBColumn('Id', datatype='uniqueidentifier'))
LicensedFeature_20240327.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 84/172: LicensedFeatureOptions
LicensedFeatureOptions = DBTable('LicensedFeatureOptions')
LicensedFeatureOptions.add_column(DBColumn('Id', datatype='uniqueidentifier'))
LicensedFeatureOptions.add_column(DBColumn('LicensedFeatureId', datatype='uniqueidentifier'))
LicensedFeatureOptions.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 85/172: LicensedFeatureOptions_20240327
LicensedFeatureOptions_20240327 = DBTable('LicensedFeatureOptions_20240327')
LicensedFeatureOptions_20240327.add_column(DBColumn('Id', datatype='uniqueidentifier'))
LicensedFeatureOptions_20240327.add_column(DBColumn('LicensedFeatureId', datatype='uniqueidentifier'))
LicensedFeatureOptions_20240327.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 86/172: Location
Location = DBTable('Location')
Location.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Location.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
Location.add_column(DBColumn('Description', datatype='nvarchar'))
Location.add_column(DBColumn('Latitude', datatype='float'))
Location.add_column(DBColumn('Longitude', datatype='float'))

#Table 87/172: LocationAnalyticsParameter
LocationAnalyticsParameter = DBTable('LocationAnalyticsParameter')
LocationAnalyticsParameter.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
LocationAnalyticsParameter.add_column(DBColumn('FromDate', datatype='datetime'))
LocationAnalyticsParameter.add_column(DBColumn('RankingMinAmplitude', datatype='float'))
LocationAnalyticsParameter.add_column(DBColumn('PriorityScoreFilterThreshold', datatype='float'))
LocationAnalyticsParameter.add_column(DBColumn('PriorityScoreFirst', datatype='float'))
LocationAnalyticsParameter.add_column(DBColumn('PriorityScoreSecond', datatype='float'))
LocationAnalyticsParameter.add_column(DBColumn('PriorityScoreThird', datatype='float'))
LocationAnalyticsParameter.add_column(DBColumn('DbScanRadius', datatype='float'))

#Table 88/172: LocationEQParameter
LocationEQParameter = DBTable('LocationEQParameter')
LocationEQParameter.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
LocationEQParameter.add_column(DBColumn('FromDate', datatype='datetime'))
LocationEQParameter.add_column(DBColumn('ShapeCorrelationMin', datatype='float'))
LocationEQParameter.add_column(DBColumn('WidthMin', datatype='float'))
LocationEQParameter.add_column(DBColumn('WidthMax', datatype='float'))
LocationEQParameter.add_column(DBColumn('VariationMax', datatype='float'))
LocationEQParameter.add_column(DBColumn('CarSpeedMin', datatype='float'))
LocationEQParameter.add_column(DBColumn('CarSpeedMax', datatype='float'))
LocationEQParameter.add_column(DBColumn('CarWindAngleMin', datatype='float'))
LocationEQParameter.add_column(DBColumn('CarWindAngleMax', datatype='float'))
LocationEQParameter.add_column(DBColumn('DBScanSpatialScale', datatype='float'))
LocationEQParameter.add_column(DBColumn('AccelerationMax', datatype='float'))
LocationEQParameter.add_column(DBColumn('IsFacilityEQ', datatype='bit'))
LocationEQParameter.add_column(DBColumn('MinAmplitude', datatype='float'))
LocationEQParameter.add_column(DBColumn('MinimumEmissions', datatype='float'))
LocationEQParameter.add_column(DBColumn('SigmaPrior', datatype='float'))
LocationEQParameter.add_column(DBColumn('PriorScaleWeight', datatype='int'))

#Table 89/172: LocationFOV3Parameter
LocationFOV3Parameter = DBTable('LocationFOV3Parameter')
LocationFOV3Parameter.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
LocationFOV3Parameter.add_column(DBColumn('FromDate', datatype='datetime'))
LocationFOV3Parameter.add_column(DBColumn('LeakRate', datatype='float'))
LocationFOV3Parameter.add_column(DBColumn('EdgeProbability', datatype='float'))
LocationFOV3Parameter.add_column(DBColumn('WindAveragingTime', datatype='float'))
LocationFOV3Parameter.add_column(DBColumn('SegmentBuffer', datatype='float'))

#Table 90/172: LocationLisaParameter
LocationLisaParameter = DBTable('LocationLisaParameter')
LocationLisaParameter.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
LocationLisaParameter.add_column(DBColumn('FromDate', datatype='datetime'))
LocationLisaParameter.add_column(DBColumn('Radius', datatype='float'))

#Table 91/172: LocationPipeLineParameter
LocationPipeLineParameter = DBTable('LocationPipeLineParameter')
LocationPipeLineParameter.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
LocationPipeLineParameter.add_column(DBColumn('FromDate', datatype='datetime'))
LocationPipeLineParameter.add_column(DBColumn('Min', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('Max', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneClassifierNotNaturalGasLowerLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneClassifierNotNaturalGasUpperLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneClassifierNaturalGasLowerLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneClassifierNaturalGasUpperLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneClassifierNotNaturalGasPriorProbability', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('ThresholdConfidence', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('Regularization', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('VehicleExhaustClassifierEthyleneSdevFactor', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('VehicleExhaustClassifierEthyleneLowerLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('VehicleExhaustClassifierEthaneSdevFactor', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('VehicleExhaustClassifierEthaneUpperLimit', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneComputationLockMethaneEthaneSdevRatio', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('EthaneComputationLockMethaneEthyleneSdevRatio', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('MinimumEthaneRatioStdDev', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('MinimumEthyleneRatioStdDev', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('MinimumWidth', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('MaximumWidth', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('MinimumFilterLength', datatype='int'))
LocationPipeLineParameter.add_column(DBColumn('BaselineFilterLength', datatype='int'))
LocationPipeLineParameter.add_column(DBColumn('NormalizedWidthLow', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('NormalizedWidthHigh', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('NormalizedAmplitudeLow', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('NormalizedAmplitudeHigh', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('LISA_FOV_a', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('LISA_FOV_b', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('LISA_FOV_c', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('LISA_FOV_beta', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('CarSpeedThresholdMin', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('CarSpeedThresholdMax', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('WindSpeedThresholdMin', datatype='float'))
LocationPipeLineParameter.add_column(DBColumn('WindSpeedThresholdMax', datatype='float'))

#Table 92/172: MasterInvestigationItem
MasterInvestigationItem = DBTable('MasterInvestigationItem')
MasterInvestigationItem.add_column(DBColumn('Id', datatype='int'))
MasterInvestigationItem.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
MasterInvestigationItem.add_column(DBColumn('Label', datatype='nvarchar'))
MasterInvestigationItem.add_column(DBColumn('InvestigationDataTypeId', datatype='int'))
MasterInvestigationItem.add_column(DBColumn('ValueOptions', datatype='nvarchar'))
MasterInvestigationItem.add_column(DBColumn('PlaceHolder', datatype='nvarchar'))
MasterInvestigationItem.add_column(DBColumn('CreatedDate', datatype='datetime'))
MasterInvestigationItem.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 93/172: MasterInvestigationItem_20240910
MasterInvestigationItem_20240910 = DBTable('MasterInvestigationItem_20240910')
MasterInvestigationItem_20240910.add_column(DBColumn('Id', datatype='int'))
MasterInvestigationItem_20240910.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
MasterInvestigationItem_20240910.add_column(DBColumn('Label', datatype='nvarchar'))
MasterInvestigationItem_20240910.add_column(DBColumn('InvestigationDataTypeId', datatype='int'))
MasterInvestigationItem_20240910.add_column(DBColumn('ValueOptions', datatype='nvarchar'))
MasterInvestigationItem_20240910.add_column(DBColumn('PlaceHolder', datatype='nvarchar'))
MasterInvestigationItem_20240910.add_column(DBColumn('CreatedDate', datatype='datetime'))
MasterInvestigationItem_20240910.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 94/172: MasterInvestigationItem_20240919
MasterInvestigationItem_20240919 = DBTable('MasterInvestigationItem_20240919')
MasterInvestigationItem_20240919.add_column(DBColumn('Id', datatype='int'))
MasterInvestigationItem_20240919.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
MasterInvestigationItem_20240919.add_column(DBColumn('Label', datatype='nvarchar'))
MasterInvestigationItem_20240919.add_column(DBColumn('InvestigationDataTypeId', datatype='int'))
MasterInvestigationItem_20240919.add_column(DBColumn('ValueOptions', datatype='nvarchar'))
MasterInvestigationItem_20240919.add_column(DBColumn('PlaceHolder', datatype='nvarchar'))
MasterInvestigationItem_20240919.add_column(DBColumn('CreatedDate', datatype='datetime'))
MasterInvestigationItem_20240919.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 95/172: MasterParameter
MasterParameter = DBTable('MasterParameter')
MasterParameter.add_column(DBColumn('Id', datatype='int'))
MasterParameter.add_column(DBColumn('ParameterGroupId', datatype='int'))
MasterParameter.add_column(DBColumn('Name', datatype='nvarchar'))
MasterParameter.add_column(DBColumn('FieldDataTypeId', datatype='int'))
MasterParameter.add_column(DBColumn('FieldValue', datatype='nvarchar'))
MasterParameter.add_column(DBColumn('DefaultValue1', datatype='nvarchar'))
MasterParameter.add_column(DBColumn('DefaultValue2', datatype='nvarchar'))
MasterParameter.add_column(DBColumn('Required', datatype='bit'))
MasterParameter.add_column(DBColumn('Active', datatype='bit'))
MasterParameter.add_column(DBColumn('CreatedDate', datatype='datetime'))
MasterParameter.add_column(DBColumn('ToolTip', datatype='nvarchar'))

#Table 96/172: MasterParameter_20240327
MasterParameter_20240327 = DBTable('MasterParameter_20240327')
MasterParameter_20240327.add_column(DBColumn('Id', datatype='int'))
MasterParameter_20240327.add_column(DBColumn('ParameterGroupId', datatype='int'))
MasterParameter_20240327.add_column(DBColumn('Name', datatype='nvarchar'))
MasterParameter_20240327.add_column(DBColumn('FieldDataTypeId', datatype='int'))
MasterParameter_20240327.add_column(DBColumn('FieldValue', datatype='nvarchar'))
MasterParameter_20240327.add_column(DBColumn('DefaultValue1', datatype='nvarchar'))
MasterParameter_20240327.add_column(DBColumn('DefaultValue2', datatype='nvarchar'))
MasterParameter_20240327.add_column(DBColumn('Required', datatype='bit'))
MasterParameter_20240327.add_column(DBColumn('Active', datatype='bit'))
MasterParameter_20240327.add_column(DBColumn('CreatedDate', datatype='datetime'))
MasterParameter_20240327.add_column(DBColumn('ToolTip', datatype='nvarchar'))

#Table 97/172: Measurement
Measurement = DBTable('Measurement')
Measurement.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
Measurement.add_column(DBColumn('EpochTime', datatype='float'))
Measurement.add_column(DBColumn('CreateDate', datatype='datetime'))
Measurement.add_column(DBColumn('GpsLatitude', datatype='float'))
Measurement.add_column(DBColumn('GpsLongitude', datatype='float'))
Measurement.add_column(DBColumn('GpsFit', datatype='smallint'))
Measurement.add_column(DBColumn('Shape', datatype='geometry'))
Measurement.add_column(DBColumn('InstrumentStatus', datatype='int'))
Measurement.add_column(DBColumn('ValveMask', datatype='float'))
Measurement.add_column(DBColumn('CarSpeedNorth', datatype='float'))
Measurement.add_column(DBColumn('CarSpeedEast', datatype='float'))
Measurement.add_column(DBColumn('WindSpeedNorth', datatype='float'))
Measurement.add_column(DBColumn('WindSpeedEast', datatype='float'))
Measurement.add_column(DBColumn('WindDirectionStdDev', datatype='float'))
Measurement.add_column(DBColumn('WeatherStationRotation', datatype='float'))
Measurement.add_column(DBColumn('WindSpeedLateral', datatype='float'))
Measurement.add_column(DBColumn('WindSpeedLongitudinal', datatype='float'))
Measurement.add_column(DBColumn('ChemDetect', datatype='bit'))
Measurement.add_column(DBColumn('Species', datatype='smallint'))
Measurement.add_column(DBColumn('CH4', datatype='float'))
Measurement.add_column(DBColumn('CO2', datatype='float'))
Measurement.add_column(DBColumn('H2OPercent', datatype='float'))
Measurement.add_column(DBColumn('DeltaCH4', datatype='float'))
Measurement.add_column(DBColumn('PeripheralStatus', datatype='int'))
Measurement.add_column(DBColumn('AnalyzerStatus', datatype='int'))
Measurement.add_column(DBColumn('CavityPressure', datatype='float'))
Measurement.add_column(DBColumn('WarmBoxTemperature', datatype='float'))
Measurement.add_column(DBColumn('HotBoxTemperature', datatype='float'))
Measurement.add_column(DBColumn('MobileFlowRate', datatype='float'))
Measurement.add_column(DBColumn('AnalyzerMode', datatype='int'))
Measurement.add_column(DBColumn('PeakDetectorState', datatype='int'))
Measurement.add_column(DBColumn('C2H6', datatype='float'))
Measurement.add_column(DBColumn('C2H4', datatype='float'))
Measurement.add_column(DBColumn('AnalyzerEthaneConcentrationUncertainty', datatype='float'))
Measurement.add_column(DBColumn('WindInstNorth', datatype='float'))
Measurement.add_column(DBColumn('WindInstEast', datatype='float'))

#Table 98/172: Note
Note = DBTable('Note')
Note.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Note.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
Note.add_column(DBColumn('Lat', datatype='float'))
Note.add_column(DBColumn('Lon', datatype='float'))
Note.add_column(DBColumn('Text', datatype='nvarchar'))

#Table 99/172: OTAStatusTypes
OTAStatusTypes = DBTable('OTAStatusTypes')
OTAStatusTypes.add_column(DBColumn('Id', datatype='int'))
OTAStatusTypes.add_column(DBColumn('Name', datatype='nvarchar'))
OTAStatusTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 100/172: ParameterGroup
ParameterGroup = DBTable('ParameterGroup')
ParameterGroup.add_column(DBColumn('Id', datatype='int'))
ParameterGroup.add_column(DBColumn('Name', datatype='nvarchar'))
ParameterGroup.add_column(DBColumn('Active', datatype='bit'))
ParameterGroup.add_column(DBColumn('CreatedDate', datatype='datetime'))

#Table 101/172: ParameterGroup_20240327
ParameterGroup_20240327 = DBTable('ParameterGroup_20240327')
ParameterGroup_20240327.add_column(DBColumn('Id', datatype='int'))
ParameterGroup_20240327.add_column(DBColumn('Name', datatype='nvarchar'))
ParameterGroup_20240327.add_column(DBColumn('Active', datatype='bit'))
ParameterGroup_20240327.add_column(DBColumn('CreatedDate', datatype='datetime'))

#Table 102/172: ParameterType
ParameterType = DBTable('ParameterType')
ParameterType.add_column(DBColumn('Id', datatype='int'))
ParameterType.add_column(DBColumn('Name', datatype='nvarchar'))
ParameterType.add_column(DBColumn('Active', datatype='bit'))
ParameterType.add_column(DBColumn('CreatedDate', datatype='datetime'))

#Table 103/172: Peak
Peak = DBTable('Peak')
Peak.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Peak.add_column(DBColumn('Amplitude', datatype='float'))
Peak.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
Peak.add_column(DBColumn('CH4', datatype='float'))
Peak.add_column(DBColumn('CarSpeedEast', datatype='float'))
Peak.add_column(DBColumn('CarSpeedNorth', datatype='float'))
Peak.add_column(DBColumn('ClassificationConfidence', datatype='float'))
Peak.add_column(DBColumn('Disposition', datatype='int'))
Peak.add_column(DBColumn('Distance', datatype='float'))
Peak.add_column(DBColumn('EpochTime', datatype='float'))
Peak.add_column(DBColumn('EthaneConcentrationSdev', datatype='float'))
Peak.add_column(DBColumn('EthaneRatio', datatype='float'))
Peak.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
Peak.add_column(DBColumn('EthaneRatioUncertainty', datatype='float'))
Peak.add_column(DBColumn('EthyleneConcentrationSdev', datatype='float'))
Peak.add_column(DBColumn('EthyleneRatio', datatype='float'))
Peak.add_column(DBColumn('EthyleneRatioSdev', datatype='float'))
Peak.add_column(DBColumn('EthyleneRatioUncertainty', datatype='float'))
Peak.add_column(DBColumn('GpsLatitude', datatype='float'))
Peak.add_column(DBColumn('GpsLongitude', datatype='float'))
Peak.add_column(DBColumn('LineIntegral', datatype='float'))
Peak.add_column(DBColumn('Lisa', datatype='geometry'))
Peak.add_column(DBColumn('MeasurementType', datatype='int'))
Peak.add_column(DBColumn('MethanePeakToPeak', datatype='float'))
Peak.add_column(DBColumn('PipEnergy', datatype='float'))
Peak.add_column(DBColumn('PlumeCarSpeedMaximum', datatype='float'))
Peak.add_column(DBColumn('PlumeCarSpeedMedian', datatype='float'))
Peak.add_column(DBColumn('PlumeCarSpeedMinimum', datatype='float'))
Peak.add_column(DBColumn('PlumeEmissionRate', datatype='float'))
Peak.add_column(DBColumn('PlumeEmissionRateUncertainty', datatype='float'))
Peak.add_column(DBColumn('PlumeEpochStart', datatype='float'))
Peak.add_column(DBColumn('PlumeEpochEnd', datatype='float'))
Peak.add_column(DBColumn('PlumeWindSpeedMaximum', datatype='float'))
Peak.add_column(DBColumn('PlumeWindSpeedMedian', datatype='float'))
Peak.add_column(DBColumn('PlumeWindSpeedMinimum', datatype='float'))
Peak.add_column(DBColumn('PlumeWidth', datatype='float'))
Peak.add_column(DBColumn('ProbA', datatype='float'))
Peak.add_column(DBColumn('ProbX0', datatype='float'))
Peak.add_column(DBColumn('ShapeCorrelation', datatype='float'))
Peak.add_column(DBColumn('Sigma', datatype='float'))
Peak.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
Peak.add_column(DBColumn('SurvivedCollection', datatype='bit'))
Peak.add_column(DBColumn('VariationCoef', datatype='float'))
Peak.add_column(DBColumn('WindDirectionStdDev', datatype='float'))
Peak.add_column(DBColumn('WindSpeedEast', datatype='float'))
Peak.add_column(DBColumn('WindSpeedNorth', datatype='float'))
Peak.add_column(DBColumn('PlumeCarAccelerationMaximum', datatype='float'))
Peak.add_column(DBColumn('PlumeCarAccelerationMedian', datatype='float'))
Peak.add_column(DBColumn('PlumeCarAccelerationMinimum', datatype='float'))

#Table 104/172: PeakArchive
PeakArchive = DBTable('PeakArchive')
PeakArchive.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
PeakArchive.add_column(DBColumn('EpochTime', datatype='float'))
PeakArchive.add_column(DBColumn('Amplitude', datatype='float'))
PeakArchive.add_column(DBColumn('CH4', datatype='float'))
PeakArchive.add_column(DBColumn('Position', datatype='geometry'))
PeakArchive.add_column(DBColumn('Lisa', datatype='geometry'))
PeakArchive.add_column(DBColumn('LisaOpeningAngle', datatype='float'))
PeakArchive.add_column(DBColumn('LisaBearing', datatype='float'))
PeakArchive.add_column(DBColumn('CarBearing', datatype='float'))
PeakArchive.add_column(DBColumn('Major', datatype='float'))
PeakArchive.add_column(DBColumn('Minor', datatype='float'))
PeakArchive.add_column(DBColumn('CarSpeedNorth', datatype='float'))
PeakArchive.add_column(DBColumn('CarSpeedEast', datatype='float'))
PeakArchive.add_column(DBColumn('WindDirectionStdDev', datatype='float'))
PeakArchive.add_column(DBColumn('WindSpeedNorth', datatype='float'))
PeakArchive.add_column(DBColumn('WindSpeedEast', datatype='float'))
PeakArchive.add_column(DBColumn('Sigma', datatype='float'))
PeakArchive.add_column(DBColumn('Distance', datatype='float'))
PeakArchive.add_column(DBColumn('GpsLatitude', datatype='float'))
PeakArchive.add_column(DBColumn('GpsLongitude', datatype='float'))
PeakArchive.add_column(DBColumn('PassedAutoThreshold', datatype='bit'))
PeakArchive.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
PeakArchive.add_column(DBColumn('EthaneRatio', datatype='float'))
PeakArchive.add_column(DBColumn('EthaneRatioSdevRaw', datatype='float'))
PeakArchive.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
PeakArchive.add_column(DBColumn('EthaneConcentrationSdev', datatype='float'))
PeakArchive.add_column(DBColumn('EthyleneRatio', datatype='float'))
PeakArchive.add_column(DBColumn('EthyleneRatioSdevRaw', datatype='float'))
PeakArchive.add_column(DBColumn('EthyleneRatioSdev', datatype='float'))
PeakArchive.add_column(DBColumn('EthyleneConcentrationSdev', datatype='float'))
PeakArchive.add_column(DBColumn('PipEnergy', datatype='float'))
PeakArchive.add_column(DBColumn('MethanePeaktoPeak', datatype='float'))
PeakArchive.add_column(DBColumn('Disposition', datatype='int'))
PeakArchive.add_column(DBColumn('ClassificationConfidence', datatype='float'))
PeakArchive.add_column(DBColumn('SurvivedCollection', datatype='bit'))
PeakArchive.add_column(DBColumn('Id', datatype='uniqueidentifier'))
PeakArchive.add_column(DBColumn('PeakNumber', datatype='int'))

#Table 105/172: PeakAutomatedEmissionSourceMapping
PeakAutomatedEmissionSourceMapping = DBTable('PeakAutomatedEmissionSourceMapping')
PeakAutomatedEmissionSourceMapping.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))
PeakAutomatedEmissionSourceMapping.add_column(DBColumn('AutomatedEmissionSourceId', datatype='uniqueidentifier'))

#Table 106/172: PeakEmissionSourceMapping
PeakEmissionSourceMapping = DBTable('PeakEmissionSourceMapping')
PeakEmissionSourceMapping.add_column(DBColumn('Id', datatype='uniqueidentifier'))
PeakEmissionSourceMapping.add_column(DBColumn('EmissionSourceId', datatype='uniqueidentifier'))
PeakEmissionSourceMapping.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))

#Table 107/172: PreviousUserPassword
PreviousUserPassword = DBTable('PreviousUserPassword')
PreviousUserPassword.add_column(DBColumn('Id', datatype='uniqueidentifier'))
PreviousUserPassword.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
PreviousUserPassword.add_column(DBColumn('PasswordHash', datatype='nvarchar'))
PreviousUserPassword.add_column(DBColumn('PasswordCreationDate', datatype='datetime'))

#Table 108/172: ReadingUnitTypes
ReadingUnitTypes = DBTable('ReadingUnitTypes')
ReadingUnitTypes.add_column(DBColumn('Id', datatype='int'))
ReadingUnitTypes.add_column(DBColumn('Name', datatype='nvarchar'))
ReadingUnitTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 109/172: ReferenceGasBottle
ReferenceGasBottle = DBTable('ReferenceGasBottle')
ReferenceGasBottle.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReferenceGasBottle.add_column(DBColumn('SurveyorUnitId', datatype='uniqueidentifier'))
ReferenceGasBottle.add_column(DBColumn('BatchId', datatype='nvarchar'))
ReferenceGasBottle.add_column(DBColumn('IsotopicValue', datatype='float'))
ReferenceGasBottle.add_column(DBColumn('Date', datatype='datetime'))
ReferenceGasBottle.add_column(DBColumn('EthaneToMethaneRatio', datatype='float'))

#Table 110/172: Report
Report = DBTable('Report')
Report.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Report.add_column(DBColumn('ReportTypeId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('ReportStatusTypeId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('ReportTitle', datatype='nvarchar'))
Report.add_column(DBColumn('MapWidth', datatype='decimal'))
Report.add_column(DBColumn('MapHeight', datatype='decimal'))
Report.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('TimeZoneId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('SelectedCustomerId', datatype='uniqueidentifier'))
Report.add_column(DBColumn('DateStarted', datatype='datetime'))
Report.add_column(DBColumn('BuildNumber', datatype='nvarchar'))
Report.add_column(DBColumn('ProcessingStarted', datatype='datetime'))
Report.add_column(DBColumn('ProcessingCompleted', datatype='datetime'))
Report.add_column(DBColumn('AssetHighlightingTypeId', datatype='int'))
Report.add_column(DBColumn('FovOpacity', datatype='float'))
Report.add_column(DBColumn('FOVVersion', datatype='float'))
Report.add_column(DBColumn('UniqueIdentifier', datatype='nvarchar'))

#Table 111/172: ReportArea
ReportArea = DBTable('ReportArea')
ReportArea.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportArea.add_column(DBColumn('ReportAreaModeTypeId', datatype='uniqueidentifier'))
ReportArea.add_column(DBColumn('StartLat', datatype='float'))
ReportArea.add_column(DBColumn('StartLong', datatype='float'))
ReportArea.add_column(DBColumn('EndLat', datatype='float'))
ReportArea.add_column(DBColumn('EndLong', datatype='float'))
ReportArea.add_column(DBColumn('Shape', datatype='geometry'))
ReportArea.add_column(DBColumn('ExternalId', datatype='nvarchar'))
ReportArea.add_column(DBColumn('BoundaryType', datatype='nvarchar'))

#Table 112/172: ReportAreaCovered
ReportAreaCovered = DBTable('ReportAreaCovered')
ReportAreaCovered.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportAreaCovered.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportAreaCovered.add_column(DBColumn('AssetLengthCoveredKM', datatype='float'))
ReportAreaCovered.add_column(DBColumn('AssetLengthKM', datatype='float'))
ReportAreaCovered.add_column(DBColumn('AreaCoveredKM2', datatype='float'))
ReportAreaCovered.add_column(DBColumn('AreaKM2', datatype='float'))
ReportAreaCovered.add_column(DBColumn('DistributionPipeKm', datatype='float'))
ReportAreaCovered.add_column(DBColumn('DistributionPipeCoveredKm', datatype='float'))
ReportAreaCovered.add_column(DBColumn('DistributionPipePercentCovered', datatype='float'))
ReportAreaCovered.add_column(DBColumn('ServicePipeKm', datatype='float'))
ReportAreaCovered.add_column(DBColumn('ServicePipeCoveredKm', datatype='float'))
ReportAreaCovered.add_column(DBColumn('CountOfServicePipes', datatype='int'))
ReportAreaCovered.add_column(DBColumn('CountOfServicePipesCovered', datatype='int'))
ReportAreaCovered.add_column(DBColumn('ServicePipePercentCovered', datatype='float'))
ReportAreaCovered.add_column(DBColumn('ServicePipeBinaryPercentCovered', datatype='float'))
ReportAreaCovered.add_column(DBColumn('ReportAreaPercentCovered', datatype='float'))

#Table 113/172: ReportAreaModeType
ReportAreaModeType = DBTable('ReportAreaModeType')
ReportAreaModeType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportAreaModeType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 114/172: ReportAsset
ReportAsset = DBTable('ReportAsset')
ReportAsset.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportAsset.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportAsset.add_column(DBColumn('AssetId', datatype='uniqueidentifier'))
ReportAsset.add_column(DBColumn('Shape', datatype='geometry'))
ReportAsset.add_column(DBColumn('IntersectionType', datatype='nchar'))

#Table 115/172: ReportAssetLayer
ReportAssetLayer = DBTable('ReportAssetLayer')
ReportAssetLayer.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportAssetLayer.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportAssetLayer.add_column(DBColumn('CustomerMaterialTypeId', datatype='uniqueidentifier'))
ReportAssetLayer.add_column(DBColumn('CustomerMaterialTypeDescription', datatype='nvarchar'))
ReportAssetLayer.add_column(DBColumn('Checked', datatype='bit'))

#Table 116/172: ReportBoundaryLayer
ReportBoundaryLayer = DBTable('ReportBoundaryLayer')
ReportBoundaryLayer.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportBoundaryLayer.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportBoundaryLayer.add_column(DBColumn('CustomerBoundaryTypeId', datatype='uniqueidentifier'))
ReportBoundaryLayer.add_column(DBColumn('CustomerBoundaryTypeDescription', datatype='nvarchar'))
ReportBoundaryLayer.add_column(DBColumn('Checked', datatype='bit'))

#Table 117/172: ReportBreadCrumbAggregated
ReportBreadCrumbAggregated = DBTable('ReportBreadCrumbAggregated')
ReportBreadCrumbAggregated.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportBreadCrumbAggregated.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportBreadCrumbAggregated.add_column(DBColumn('Shape', datatype='geometry'))
ReportBreadCrumbAggregated.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))

#Table 118/172: ReportCaptureEvent
ReportCaptureEvent = DBTable('ReportCaptureEvent')
ReportCaptureEvent.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportCaptureEvent.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportCaptureEvent.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
ReportCaptureEvent.add_column(DBColumn('EpochTime', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('DateTime', datatype='datetime'))
ReportCaptureEvent.add_column(DBColumn('GpsLatitude', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('GpsLongitude', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('Shape', datatype='geometry'))
ReportCaptureEvent.add_column(DBColumn('Disposition', datatype='int'))
ReportCaptureEvent.add_column(DBColumn('Delta', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('Concentration', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('Uncertainty', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('CaptureType', datatype='bit'))
ReportCaptureEvent.add_column(DBColumn('Distance', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('ReplayMax', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('ReplayLMin', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('ReplayRMin', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('EthaneRatio', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
ReportCaptureEvent.add_column(DBColumn('ClassificationConfidence', datatype='float'))

#Table 119/172: ReportCompliance
ReportCompliance = DBTable('ReportCompliance')
ReportCompliance.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportCompliance.add_column(DBColumn('SurveyModeTypeId', datatype='uniqueidentifier'))
ReportCompliance.add_column(DBColumn('ExclusionRadius', datatype='float'))
ReportCompliance.add_column(DBColumn('IsLisaInvestigationComplete', datatype='bit'))
ReportCompliance.add_column(DBColumn('IsGapSurveyComplete', datatype='bit'))
ReportCompliance.add_column(DBColumn('IsCGIInvestigationComplete', datatype='bit'))
ReportCompliance.add_column(DBColumn('ShowIndications', datatype='bit'))
ReportCompliance.add_column(DBColumn('ShowIsotopicAnalysis', datatype='bit'))
ReportCompliance.add_column(DBColumn('MinimumAmplitude', datatype='float'))
ReportCompliance.add_column(DBColumn('MapBufferArea', datatype='float'))
ReportCompliance.add_column(DBColumn('ShowPercentCoverageAssets', datatype='bit'))
ReportCompliance.add_column(DBColumn('ShowPercentCoverageReportArea', datatype='bit'))
ReportCompliance.add_column(DBColumn('PercentCoverageAssets', datatype='float'))
ReportCompliance.add_column(DBColumn('PercentCoverageReportArea', datatype='float'))
ReportCompliance.add_column(DBColumn('Gap', datatype='geometry'))
ReportCompliance.add_column(DBColumn('FovOpacity', datatype='float'))
ReportCompliance.add_column(DBColumn('LisaOpacity', datatype='float'))
ReportCompliance.add_column(DBColumn('ReportStartDateTime', datatype='datetime'))
ReportCompliance.add_column(DBColumn('ShowGaps', datatype='bit'))
ReportCompliance.add_column(DBColumn('EthaneExcludeVehicleExhaust', datatype='bit'))
ReportCompliance.add_column(DBColumn('EthaneExcludeBiogenicMethane', datatype='bit'))
ReportCompliance.add_column(DBColumn('EthaneExcludePossibleNaturalGas', datatype='bit'))
ReportCompliance.add_column(DBColumn('FOVVersion', datatype='float'))
ReportCompliance.add_column(DBColumn('IsReportFinal', datatype='bit'))

#Table 120/172: ReportDrivingSurvey
ReportDrivingSurvey = DBTable('ReportDrivingSurvey')
ReportDrivingSurvey.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportDrivingSurvey.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportDrivingSurvey.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
ReportDrivingSurvey.add_column(DBColumn('Snapped', datatype='bit'))

#Table 121/172: ReportEQ
ReportEQ = DBTable('ReportEQ')
ReportEQ.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportEQ.add_column(DBColumn('MapBufferArea', datatype='float'))
ReportEQ.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
ReportEQ.add_column(DBColumn('SCFHThreshold', datatype='float'))
ReportEQ.add_column(DBColumn('IsReportFinal', datatype='bit'))

#Table 122/172: ReportEQResults
ReportEQResults = DBTable('ReportEQResults')
ReportEQResults.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportEQResults.add_column(DBColumn('RankingConfidence', datatype='decimal'))

#Table 123/172: ReportEvent
ReportEvent = DBTable('ReportEvent')
ReportEvent.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportEvent.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportEvent.add_column(DBColumn('ReportTypeId', datatype='uniqueidentifier'))
ReportEvent.add_column(DBColumn('ReportEventTypeId', datatype='int'))
ReportEvent.add_column(DBColumn('ExternalSystemId', datatype='uniqueidentifier'))
ReportEvent.add_column(DBColumn('ExternalSystemRequestData', datatype='nvarchar'))
ReportEvent.add_column(DBColumn('EventDateTime', datatype='datetime'))
ReportEvent.add_column(DBColumn('EventStatus', datatype='nvarchar'))
ReportEvent.add_column(DBColumn('EventResponseContent', datatype='nvarchar'))

#Table 124/172: ReportEventType
ReportEventType = DBTable('ReportEventType')
ReportEventType.add_column(DBColumn('Id', datatype='int'))
ReportEventType.add_column(DBColumn('Name', datatype='nvarchar'))
ReportEventType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 125/172: ReportFieldOfViewAggregated
ReportFieldOfViewAggregated = DBTable('ReportFieldOfViewAggregated')
ReportFieldOfViewAggregated.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportFieldOfViewAggregated.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportFieldOfViewAggregated.add_column(DBColumn('Shape', datatype='geometry'))
ReportFieldOfViewAggregated.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))

#Table 126/172: ReportGap
ReportGap = DBTable('ReportGap')
ReportGap.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportGap.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportGap.add_column(DBColumn('Shape', datatype='geometry'))

#Table 127/172: ReportImageJob
ReportImageJob = DBTable('ReportImageJob')
ReportImageJob.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportImageJob.add_column(DBColumn('ReportJobId', datatype='uniqueidentifier'))
ReportImageJob.add_column(DBColumn('ReportInvestigationId', datatype='uniqueidentifier'))

#Table 128/172: ReportInvestigation
ReportInvestigation = DBTable('ReportInvestigation')
ReportInvestigation.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportInvestigation.add_column(DBColumn('InvestigationTemplateId', datatype='int'))
ReportInvestigation.add_column(DBColumn('LeakFinderUserId', datatype='uniqueidentifier'))
ReportInvestigation.add_column(DBColumn('FoundDateTime', datatype='datetime'))
ReportInvestigation.add_column(DBColumn('LeakLatitude', datatype='float'))
ReportInvestigation.add_column(DBColumn('LeakLongitude', datatype='float'))
ReportInvestigation.add_column(DBColumn('GpsPrecision', datatype='float'))
ReportInvestigation.add_column(DBColumn('Notes', datatype='nvarchar'))
ReportInvestigation.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
ReportInvestigation.add_column(DBColumn('CreatedDate', datatype='datetime'))
ReportInvestigation.add_column(DBColumn('UpdatedDate', datatype='datetime'))
ReportInvestigation.add_column(DBColumn('UniqueIdentifier', datatype='nvarchar'))
ReportInvestigation.add_column(DBColumn('SyncTime', datatype='datetime'))

#Table 129/172: ReportInvestigationItem
ReportInvestigationItem = DBTable('ReportInvestigationItem')
ReportInvestigationItem.add_column(DBColumn('Id', datatype='bigint'))
ReportInvestigationItem.add_column(DBColumn('ReportInvestigationId', datatype='uniqueidentifier'))
ReportInvestigationItem.add_column(DBColumn('InvestigationTemplateItemId', datatype='int'))
ReportInvestigationItem.add_column(DBColumn('SelectedValue', datatype='nvarchar'))
ReportInvestigationItem.add_column(DBColumn('CreatedDate', datatype='datetime'))
ReportInvestigationItem.add_column(DBColumn('UpdatedDate', datatype='datetime'))

#Table 130/172: ReportJob
ReportJob = DBTable('ReportJob')
ReportJob.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportJob.add_column(DBColumn('ReportJobTypeId', datatype='uniqueidentifier'))
ReportJob.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportJob.add_column(DBColumn('DateStarted', datatype='datetime'))
ReportJob.add_column(DBColumn('ReportJobStatusId', datatype='uniqueidentifier'))
ReportJob.add_column(DBColumn('ReportViewId', datatype='uniqueidentifier'))
ReportJob.add_column(DBColumn('ProcessingStarted', datatype='datetime'))
ReportJob.add_column(DBColumn('ProcessingCompleted', datatype='datetime'))
ReportJob.add_column(DBColumn('MaxMemory', datatype='int'))

#Table 131/172: ReportJobStatusType
ReportJobStatusType = DBTable('ReportJobStatusType')
ReportJobStatusType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportJobStatusType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 132/172: ReportJobType
ReportJobType = DBTable('ReportJobType')
ReportJobType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportJobType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 133/172: ReportLabel
ReportLabel = DBTable('ReportLabel')
ReportLabel.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportLabel.add_column(DBColumn('LabelId', datatype='uniqueidentifier'))
ReportLabel.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
ReportLabel.add_column(DBColumn('UpdatedBy', datatype='uniqueidentifier'))
ReportLabel.add_column(DBColumn('CreatedDate', datatype='datetime'))
ReportLabel.add_column(DBColumn('UpdatedDate', datatype='datetime'))
ReportLabel.add_column(DBColumn('IsActive', datatype='bit'))

#Table 134/172: ReportLeak
ReportLeak = DBTable('ReportLeak')
ReportLeak.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportLeak.add_column(DBColumn('LeakFinderUserId', datatype='uniqueidentifier'))
ReportLeak.add_column(DBColumn('FoundDateTime', datatype='datetime'))
ReportLeak.add_column(DBColumn('LeakLatitude', datatype='float'))
ReportLeak.add_column(DBColumn('LeakLongitude', datatype='float'))
ReportLeak.add_column(DBColumn('GpsPrecision', datatype='float'))
ReportLeak.add_column(DBColumn('LeakTypeId', datatype='int'))
ReportLeak.add_column(DBColumn('AddressStreetNumber', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('AddressApartmentNumber', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('AddressStreetName', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('AddressCity', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('AddressState', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('MapNumber', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('SurfaceReading', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('BarholeReading', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('LeakGrade', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('LeakLocationTypeId', datatype='int'))
ReportLeak.add_column(DBColumn('PipeMaterialType', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('IsPavedWallToWall', datatype='bit'))
ReportLeak.add_column(DBColumn('SurfaceOverLeakTypeId', datatype='int'))
ReportLeak.add_column(DBColumn('MeterNumber', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('LocationRemarks', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('Notes', datatype='nvarchar'))
ReportLeak.add_column(DBColumn('LeakSourceTypeId', datatype='int'))
ReportLeak.add_column(DBColumn('BoxId', datatype='uniqueidentifier'))
ReportLeak.add_column(DBColumn('SurfaceReadingUnitTypeId', datatype='int'))
ReportLeak.add_column(DBColumn('BarholeReadingUnitTypeId', datatype='int'))

#Table 135/172: ReportParameterMapping
ReportParameterMapping = DBTable('ReportParameterMapping')
ReportParameterMapping.add_column(DBColumn('Id', datatype='bigint'))
ReportParameterMapping.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportParameterMapping.add_column(DBColumn('CustomerSurveyorMappingId', datatype='int'))

#Table 136/172: ReportPeakArchive
ReportPeakArchive = DBTable('ReportPeakArchive')
ReportPeakArchive.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportPeakArchive.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportPeakArchive.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
ReportPeakArchive.add_column(DBColumn('EpochTime', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Amplitude', datatype='float'))
ReportPeakArchive.add_column(DBColumn('CH4', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Position', datatype='geometry'))
ReportPeakArchive.add_column(DBColumn('Lisa', datatype='geometry'))
ReportPeakArchive.add_column(DBColumn('LisaOpeningAngle', datatype='float'))
ReportPeakArchive.add_column(DBColumn('LisaBearing', datatype='float'))
ReportPeakArchive.add_column(DBColumn('CarBearing', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Major', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Minor', datatype='float'))
ReportPeakArchive.add_column(DBColumn('CarSpeedNorth', datatype='float'))
ReportPeakArchive.add_column(DBColumn('CarSpeedEast', datatype='float'))
ReportPeakArchive.add_column(DBColumn('WindDirectionStdDev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('WindSpeedNorth', datatype='float'))
ReportPeakArchive.add_column(DBColumn('WindSpeedEast', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Sigma', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Distance', datatype='float'))
ReportPeakArchive.add_column(DBColumn('GpsLatitude', datatype='float'))
ReportPeakArchive.add_column(DBColumn('GpsLongitude', datatype='float'))
ReportPeakArchive.add_column(DBColumn('PassedAutoThreshold', datatype='bit'))
ReportPeakArchive.add_column(DBColumn('PeakNumber', datatype='int'))
ReportPeakArchive.add_column(DBColumn('EthaneRatio', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthaneRatioSdevRaw', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthaneRatioSdev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthaneConcentrationSdev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthyleneRatio', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthyleneRatioSdevRaw', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthyleneRatioSdev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('EthyleneConcentrationSdev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('PipEnergy', datatype='float'))
ReportPeakArchive.add_column(DBColumn('MethanePeaktoPeak', datatype='float'))
ReportPeakArchive.add_column(DBColumn('Disposition', datatype='int'))
ReportPeakArchive.add_column(DBColumn('ClassificationConfidence', datatype='float'))
ReportPeakArchive.add_column(DBColumn('AggregatedEthaneRatio', datatype='float'))
ReportPeakArchive.add_column(DBColumn('AggregatedEthaneRatioSdev', datatype='float'))
ReportPeakArchive.add_column(DBColumn('AggregatedDisposition', datatype='int'))
ReportPeakArchive.add_column(DBColumn('AggregatedClassificationConfidence', datatype='float'))

#Table 137/172: ReportStatusType
ReportStatusType = DBTable('ReportStatusType')
ReportStatusType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportStatusType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 138/172: ReportSummary
ReportSummary = DBTable('ReportSummary')
ReportSummary.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportSummary.add_column(DBColumn('LisaProgress', datatype='nvarchar'))
ReportSummary.add_column(DBColumn('GapProgress', datatype='nvarchar'))
ReportSummary.add_column(DBColumn('CreatedDateTime', datatype='datetime'))
ReportSummary.add_column(DBColumn('UpdatedDateTime', datatype='datetime'))

#Table 139/172: ReportTransferStatus
ReportTransferStatus = DBTable('ReportTransferStatus')
ReportTransferStatus.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportTransferStatus.add_column(DBColumn('ExternalSystemId', datatype='uniqueidentifier'))
ReportTransferStatus.add_column(DBColumn('CreatedBy', datatype='uniqueidentifier'))
ReportTransferStatus.add_column(DBColumn('CreatedDate', datatype='datetime'))
ReportTransferStatus.add_column(DBColumn('UpdatedDate', datatype='datetime'))
ReportTransferStatus.add_column(DBColumn('OTAStatusTypeId', datatype='int'))

#Table 140/172: ReportType
ReportType = DBTable('ReportType')
ReportType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportType.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 141/172: ReportView
ReportView = DBTable('ReportView')
ReportView.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ReportView.add_column(DBColumn('ReportId', datatype='uniqueidentifier'))
ReportView.add_column(DBColumn('ViewName', datatype='nvarchar'))
ReportView.add_column(DBColumn('ShowLisa', datatype='bit'))
ReportView.add_column(DBColumn('ShowFov', datatype='bit'))
ReportView.add_column(DBColumn('ShowVehiclePath', datatype='bit'))
ReportView.add_column(DBColumn('ShowIndications', datatype='bit'))
ReportView.add_column(DBColumn('ShowIsotopicCaptures', datatype='bit'))
ReportView.add_column(DBColumn('ShowGaps', datatype='bit'))
ReportView.add_column(DBColumn('ShowAssets', datatype='bit'))
ReportView.add_column(DBColumn('ShowBoundaries', datatype='bit'))
ReportView.add_column(DBColumn('BaseMapId', datatype='uniqueidentifier'))
ReportView.add_column(DBColumn('BaseMapType_Id', datatype='uniqueidentifier'))
ReportView.add_column(DBColumn('ViewNameOrder', datatype='smallint'))
ReportView.add_column(DBColumn('HighlightLISAAssets', datatype='bit'))
ReportView.add_column(DBColumn('HighlightGAPAssets', datatype='bit'))
ReportView.add_column(DBColumn('ShowAssetBoxNumber', datatype='bit'))

#Table 142/172: ResourceReservation
ResourceReservation = DBTable('ResourceReservation')
ResourceReservation.add_column(DBColumn('Id', datatype='nvarchar'))
ResourceReservation.add_column(DBColumn('Owner', datatype='nvarchar'))
ResourceReservation.add_column(DBColumn('Created', datatype='datetime'))
ResourceReservation.add_column(DBColumn('LastAck', datatype='datetime'))

#Table 143/172: Resources
Resources = DBTable('Resources')
Resources.add_column(DBColumn('CultureId', datatype='varchar'))
Resources.add_column(DBColumn('Name', datatype='varchar'))
Resources.add_column(DBColumn('Value', datatype='nvarchar'))

#Table 144/172: Role
Role = DBTable('Role')
Role.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Role.add_column(DBColumn('Name', datatype='nvarchar'))

#Table 145/172: Segment
Segment = DBTable('Segment')
Segment.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
Segment.add_column(DBColumn('Order', datatype='int'))
Segment.add_column(DBColumn('Mode', datatype='int'))
Segment.add_column(DBColumn('Shape', datatype='geometry'))
Segment.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Segment.add_column(DBColumn('StartEpoch', datatype='float'))
Segment.add_column(DBColumn('EndEpoch', datatype='float'))
Segment.add_column(DBColumn('LengthMeters', datatype='float'))
Segment.add_column(DBColumn('DurationSeconds', datatype='float'))
Segment.add_column(DBColumn('WindSpeedMinimum', datatype='float'))
Segment.add_column(DBColumn('WindSpeedMaximum', datatype='float'))
Segment.add_column(DBColumn('WindSpeedMedian', datatype='float'))
Segment.add_column(DBColumn('CarSpeedMinimum', datatype='float'))
Segment.add_column(DBColumn('CarSpeedMaximum', datatype='float'))
Segment.add_column(DBColumn('CarSpeedMedian', datatype='float'))
Segment.add_column(DBColumn('CH4Minimum', datatype='float'))
Segment.add_column(DBColumn('CH4Maximum', datatype='float'))
Segment.add_column(DBColumn('CH4Median', datatype='float'))

#Table 146/172: ServerLog
ServerLog = DBTable('ServerLog')
ServerLog.add_column(DBColumn('Id', datatype='int'))
ServerLog.add_column(DBColumn('Date', datatype='datetime'))
ServerLog.add_column(DBColumn('Thread', datatype='bigint'))
ServerLog.add_column(DBColumn('Level', datatype='nvarchar'))
ServerLog.add_column(DBColumn('Logger', datatype='nvarchar'))
ServerLog.add_column(DBColumn('Message', datatype='nvarchar'))
ServerLog.add_column(DBColumn('Exception', datatype='nvarchar'))

#Table 147/172: SnappedPeak
SnappedPeak = DBTable('SnappedPeak')
SnappedPeak.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SnappedPeak.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
SnappedPeak.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))
SnappedPeak.add_column(DBColumn('EpochTime', datatype='float'))
SnappedPeak.add_column(DBColumn('Position', datatype='geometry'))
SnappedPeak.add_column(DBColumn('Lisa', datatype='geometry'))
SnappedPeak.add_column(DBColumn('GpsLatitude', datatype='float'))
SnappedPeak.add_column(DBColumn('GpsLongitude', datatype='float'))

#Table 148/172: SnappedPeakArchive
SnappedPeakArchive = DBTable('SnappedPeakArchive')
SnappedPeakArchive.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
SnappedPeakArchive.add_column(DBColumn('EpochTime', datatype='float'))
SnappedPeakArchive.add_column(DBColumn('Position', datatype='geometry'))
SnappedPeakArchive.add_column(DBColumn('Lisa', datatype='geometry'))
SnappedPeakArchive.add_column(DBColumn('GpsLatitude', datatype='float'))
SnappedPeakArchive.add_column(DBColumn('GpsLongitude', datatype='float'))
SnappedPeakArchive.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SnappedPeakArchive.add_column(DBColumn('PeakId', datatype='uniqueidentifier'))

#Table 149/172: SnappedSegment
SnappedSegment = DBTable('SnappedSegment')
SnappedSegment.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SnappedSegment.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SnappedSegment.add_column(DBColumn('Order', datatype='int'))
SnappedSegment.add_column(DBColumn('Mode', datatype='int'))
SnappedSegment.add_column(DBColumn('Shape', datatype='geometry'))
SnappedSegment.add_column(DBColumn('StartEpoch', datatype='float'))
SnappedSegment.add_column(DBColumn('EndEpoch', datatype='float'))
SnappedSegment.add_column(DBColumn('LengthMeters', datatype='float'))
SnappedSegment.add_column(DBColumn('DurationSeconds', datatype='float'))
SnappedSegment.add_column(DBColumn('WindSpeedMinimum', datatype='float'))
SnappedSegment.add_column(DBColumn('WindSpeedMaximum', datatype='float'))
SnappedSegment.add_column(DBColumn('WindSpeedMedian', datatype='float'))
SnappedSegment.add_column(DBColumn('CarSpeedMinimum', datatype='float'))
SnappedSegment.add_column(DBColumn('CarSpeedMaximum', datatype='float'))
SnappedSegment.add_column(DBColumn('CarSpeedMedian', datatype='float'))
SnappedSegment.add_column(DBColumn('CH4Minimum', datatype='float'))
SnappedSegment.add_column(DBColumn('CH4Maximum', datatype='float'))
SnappedSegment.add_column(DBColumn('CH4Median', datatype='float'))

#Table 150/172: SurfaceOverLeakTypes
SurfaceOverLeakTypes = DBTable('SurfaceOverLeakTypes')
SurfaceOverLeakTypes.add_column(DBColumn('Id', datatype='int'))
SurfaceOverLeakTypes.add_column(DBColumn('Name', datatype='nvarchar'))
SurfaceOverLeakTypes.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 151/172: Survey
Survey = DBTable('Survey')
Survey.add_column(DBColumn('Id', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('AnalyzerId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('SurveyorUnitId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('ReferenceGasBottleId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('SurveyModeTypeId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('StartEpoch', datatype='float'))
Survey.add_column(DBColumn('EndEpoch', datatype='float'))
Survey.add_column(DBColumn('StartDateTime', datatype='datetime'))
Survey.add_column(DBColumn('EndDateTime', datatype='datetime'))
Survey.add_column(DBColumn('Tag', datatype='nvarchar'))
Survey.add_column(DBColumn('StabilityClass', datatype='nvarchar'))
Survey.add_column(DBColumn('MinimumAmplitude', datatype='float'))
Survey.add_column(DBColumn('Status', datatype='nvarchar'))
Survey.add_column(DBColumn('Deleted', datatype='bit'))
Survey.add_column(DBColumn('ProcessingDateStarted', datatype='datetime'))
Survey.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
Survey.add_column(DBColumn('BuildNumber', datatype='nvarchar'))
Survey.add_column(DBColumn('ProcessingDateCompleted', datatype='datetime'))
Survey.add_column(DBColumn('Snapped', datatype='bit'))
Survey.add_column(DBColumn('FOV3Capable', datatype='bit'))
Survey.add_column(DBColumn('SurveyAreaBoundary', datatype='geometry'))
Survey.add_column(DBColumn('MinimumFlowRate', datatype='float'))
Survey.add_column(DBColumn('FlowRateFilterUsed', datatype='bit'))
Survey.add_column(DBColumn('AnemometerRotationAngleApplied', datatype='float'))
Survey.add_column(DBColumn('DrivingLengthMeters', datatype='float'))

#Table 152/172: SurveyArea
SurveyArea = DBTable('SurveyArea')
SurveyArea.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SurveyArea.add_column(DBColumn('AreaModeTypeId', datatype='uniqueidentifier'))
SurveyArea.add_column(DBColumn('StartLat', datatype='float'))
SurveyArea.add_column(DBColumn('StartLong', datatype='float'))
SurveyArea.add_column(DBColumn('EndLat', datatype='float'))
SurveyArea.add_column(DBColumn('EndLong', datatype='float'))
SurveyArea.add_column(DBColumn('Shape', datatype='geometry'))
SurveyArea.add_column(DBColumn('ExternalId', datatype='nvarchar'))

#Table 153/172: SurveyCondition
SurveyCondition = DBTable('SurveyCondition')
SurveyCondition.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SurveyCondition.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SurveyCondition.add_column(DBColumn('Name', datatype='nvarchar'))
SurveyCondition.add_column(DBColumn('Value', datatype='nvarchar'))

#Table 154/172: SurveyJob
SurveyJob = DBTable('SurveyJob')
SurveyJob.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SurveyJob.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SurveyJob.add_column(DBColumn('JobTypeId', datatype='uniqueidentifier'))
SurveyJob.add_column(DBColumn('JobStatusTypeId', datatype='uniqueidentifier'))
SurveyJob.add_column(DBColumn('ProcessingStarted', datatype='datetime'))
SurveyJob.add_column(DBColumn('ProcessingCompleted', datatype='datetime'))
SurveyJob.add_column(DBColumn('MaxMemory', datatype='int'))

#Table 155/172: SurveyModeType
SurveyModeType = DBTable('SurveyModeType')
SurveyModeType.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SurveyModeType.add_column(DBColumn('Description', datatype='nvarchar'))
SurveyModeType.add_column(DBColumn('ResourceName', datatype='varchar'))

#Table 156/172: SurveyModeTypeConfiguration
SurveyModeTypeConfiguration = DBTable('SurveyModeTypeConfiguration')
SurveyModeTypeConfiguration.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
SurveyModeTypeConfiguration.add_column(DBColumn('SurveyModeTypeId', datatype='uniqueidentifier'))
SurveyModeTypeConfiguration.add_column(DBColumn('FromDate', datatype='datetime'))
SurveyModeTypeConfiguration.add_column(DBColumn('MinimumAmplitude', datatype='float'))

#Table 157/172: SurveyorUnit
SurveyorUnit = DBTable('SurveyorUnit')
SurveyorUnit.add_column(DBColumn('Id', datatype='uniqueidentifier'))
SurveyorUnit.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
SurveyorUnit.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 158/172: SurveyQACheck
SurveyQACheck = DBTable('SurveyQACheck')
SurveyQACheck.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SurveyQACheck.add_column(DBColumn('NumReadingsTotal', datatype='int'))
SurveyQACheck.add_column(DBColumn('NumReadingsFiltered', datatype='int'))
SurveyQACheck.add_column(DBColumn('LateralCorrelation', datatype='float'))
SurveyQACheck.add_column(DBColumn('LongitudinalCorrelation', datatype='float'))
SurveyQACheck.add_column(DBColumn('LateralRotation', datatype='float'))
SurveyQACheck.add_column(DBColumn('LongitudinalRotation', datatype='float'))
SurveyQACheck.add_column(DBColumn('MissingMinutes', datatype='int'))
SurveyQACheck.add_column(DBColumn('NumberOfPeaks', datatype='int'))
SurveyQACheck.add_column(DBColumn('SurveyDurationSeconds', datatype='float'))
SurveyQACheck.add_column(DBColumn('AverageFlowRate', datatype='float'))
SurveyQACheck.add_column(DBColumn('FlowRateStandardDeviation', datatype='float'))
SurveyQACheck.add_column(DBColumn('MedianRingdownRateHz', datatype='float'))

#Table 159/172: SurveyResult
SurveyResult = DBTable('SurveyResult')
SurveyResult.add_column(DBColumn('SurveyId', datatype='uniqueidentifier'))
SurveyResult.add_column(DBColumn('FieldOfView', datatype='geometry'))
SurveyResult.add_column(DBColumn('Breadcrumb', datatype='geometry'))

#Table 160/172: TimeZone
TimeZone = DBTable('TimeZone')
TimeZone.add_column(DBColumn('Id', datatype='uniqueidentifier'))
TimeZone.add_column(DBColumn('Description', datatype='nvarchar'))
TimeZone.add_column(DBColumn('UIDescription', datatype='nvarchar'))

#Table 161/172: TimeZoneAdjustmentRule
TimeZoneAdjustmentRule = DBTable('TimeZoneAdjustmentRule')
TimeZoneAdjustmentRule.add_column(DBColumn('Id', datatype='uniqueidentifier'))
TimeZoneAdjustmentRule.add_column(DBColumn('TimeZoneId', datatype='uniqueidentifier'))
TimeZoneAdjustmentRule.add_column(DBColumn('RuleNo', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DateStart', datatype='datetime2'))
TimeZoneAdjustmentRule.add_column(DBColumn('DateEnd', datatype='datetime2'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartIsFixedDateRule', datatype='bit'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartMonth', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartDay', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartWeek', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartDayOfWeek', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionStartTimeOfDay', datatype='time'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndIsFixedDateRule', datatype='bit'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndMonth', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndDay', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndWeek', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndDayOfWeek', datatype='int'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightTransitionEndTimeOfDay', datatype='time'))
TimeZoneAdjustmentRule.add_column(DBColumn('DaylightDeltaSec', datatype='int'))

#Table 162/172: TimeZoneList
TimeZoneList = DBTable('TimeZoneList')
TimeZoneList.add_column(DBColumn('Id', datatype='uniqueidentifier'))
TimeZoneList.add_column(DBColumn('Identifier', datatype='nvarchar'))
TimeZoneList.add_column(DBColumn('SupportsDaylightSavingTime', datatype='bit'))
TimeZoneList.add_column(DBColumn('BaseUtcOffsetSec', datatype='int'))
TimeZoneList.add_column(DBColumn('StdAbb', datatype='nvarchar'))
TimeZoneList.add_column(DBColumn('DSTAbb', datatype='nvarchar'))

#Table 163/172: UnitMeasurementDistances
UnitMeasurementDistances = DBTable('UnitMeasurementDistances')
UnitMeasurementDistances.add_column(DBColumn('Id', datatype='uniqueidentifier'))
UnitMeasurementDistances.add_column(DBColumn('Name', datatype='nvarchar'))
UnitMeasurementDistances.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 164/172: UnitMeasurementFlows
UnitMeasurementFlows = DBTable('UnitMeasurementFlows')
UnitMeasurementFlows.add_column(DBColumn('Id', datatype='uniqueidentifier'))
UnitMeasurementFlows.add_column(DBColumn('Name', datatype='nvarchar'))
UnitMeasurementFlows.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 165/172: UnitMeasurementSpeeds
UnitMeasurementSpeeds = DBTable('UnitMeasurementSpeeds')
UnitMeasurementSpeeds.add_column(DBColumn('Id', datatype='uniqueidentifier'))
UnitMeasurementSpeeds.add_column(DBColumn('Name', datatype='nvarchar'))
UnitMeasurementSpeeds.add_column(DBColumn('Description', datatype='nvarchar'))

#Table 166/172: User
User = DBTable('User')
User.add_column(DBColumn('Id', datatype='uniqueidentifier'))
User.add_column(DBColumn('CustomerId', datatype='uniqueidentifier'))
User.add_column(DBColumn('OpQualExpiration', datatype='datetime'))
User.add_column(DBColumn('Active', datatype='bit'))
User.add_column(DBColumn('EulaAccepted', datatype='bit'))
User.add_column(DBColumn('TimeZoneId', datatype='uniqueidentifier'))
User.add_column(DBColumn('LocationId', datatype='uniqueidentifier'))
User.add_column(DBColumn('FirstName', datatype='nvarchar'))
User.add_column(DBColumn('LastName', datatype='nvarchar'))
User.add_column(DBColumn('CellPhoneNumber', datatype='nvarchar'))
User.add_column(DBColumn('Email', datatype='nvarchar'))
User.add_column(DBColumn('EmailConfirmed', datatype='bit'))
User.add_column(DBColumn('PasswordHash', datatype='nvarchar'))
User.add_column(DBColumn('SecurityStamp', datatype='nvarchar'))
User.add_column(DBColumn('PhoneNumber', datatype='nvarchar'))
User.add_column(DBColumn('PhoneNumberConfirmed', datatype='bit'))
User.add_column(DBColumn('TwoFactorEnabled', datatype='bit'))
User.add_column(DBColumn('LockoutEndDateUtc', datatype='datetime'))
User.add_column(DBColumn('LockoutEnabled', datatype='bit'))
User.add_column(DBColumn('AccessFailedCount', datatype='int'))
User.add_column(DBColumn('UserName', datatype='nvarchar'))
User.add_column(DBColumn('CultureId', datatype='varchar'))
User.add_column(DBColumn('LastLoginDateTime', datatype='datetime'))

#Table 167/172: UserAccountManagement
UserAccountManagement = DBTable('UserAccountManagement')
UserAccountManagement.add_column(DBColumn('Id', datatype='uniqueidentifier'))
UserAccountManagement.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
UserAccountManagement.add_column(DBColumn('PasswordCreationDate', datatype='datetime'))
UserAccountManagement.add_column(DBColumn('PasswordTokenHash', datatype='nvarchar'))
UserAccountManagement.add_column(DBColumn('PasswordTokenExpirationDate', datatype='datetime'))
UserAccountManagement.add_column(DBColumn('PasswordTokenUsed', datatype='bit'))
UserAccountManagement.add_column(DBColumn('AccountActivationTokenHash', datatype='nvarchar'))
UserAccountManagement.add_column(DBColumn('AccountActivationTokenExpirationDate', datatype='datetime'))

#Table 168/172: UserClaim
UserClaim = DBTable('UserClaim')
UserClaim.add_column(DBColumn('Id', datatype='int'))
UserClaim.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
UserClaim.add_column(DBColumn('ClaimType', datatype='nvarchar'))
UserClaim.add_column(DBColumn('ClaimValue', datatype='nvarchar'))

#Table 169/172: UserLogin
UserLogin = DBTable('UserLogin')
UserLogin.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
UserLogin.add_column(DBColumn('LoginProvider', datatype='nvarchar'))
UserLogin.add_column(DBColumn('ProviderKey', datatype='nvarchar'))

#Table 170/172: UserPreference
UserPreference = DBTable('UserPreference')
UserPreference.add_column(DBColumn('Id', datatype='uniqueidentifier'))
UserPreference.add_column(DBColumn('UserId', datatype='uniqueidentifier'))
UserPreference.add_column(DBColumn('Latitude', datatype='float'))
UserPreference.add_column(DBColumn('Longitude', datatype='float'))

#Table 171/172: UserRole
UserRole = DBTable('UserRole')
UserRole.add_column(DBColumn('RoleId', datatype='uniqueidentifier'))
UserRole.add_column(DBColumn('UserId', datatype='uniqueidentifier'))

#Table 172/172: ViewConfiguration
ViewConfiguration = DBTable('ViewConfiguration')
ViewConfiguration.add_column(DBColumn('Id', datatype='uniqueidentifier'))
ViewConfiguration.add_column(DBColumn('Description', datatype='nvarchar'))
ViewConfiguration.add_column(DBColumn('Value', datatype='decimal'))
ViewConfiguration.add_column(DBColumn('GroupId', datatype='int'))


# Export all table definitions for easy access
__all__ = [
    '__MigrationHistory',
    'AnalyticsPeakArchive',
    'Analyzer',
    'AnalyzerAlarmLog',
    'AnalyzerHardwareCapabilityType',
    'AnalyzerHeartbeat',
    'AnalyzerLog',
    'AnalyzerUpdateJob',
    'AnemometerRaw',
    'AssetBoxMetadata',
    'AssetFovMetadata',
    'AssetHighlightingTypes',
    'AssetType',
    'AuditLog',
    'AutomatedEmissionSource',
    'AutomatedInvalidPeak',
    'Backup_InvestigationTemplateItem_Table',
    'Backup_MasterInvestigationItem_Table',
    'BaseMapType',
    'Box',
    'BoxTransferStatus',
    'BoxTypes',
    'CaptureAnalysisDispositionTypes',
    'CaptureEvent',
    'ClientJSLog',
    'ClusteringTypes',
    'Culture',
    'Customer',
    'CUSTOMER_20231221',
    'CustomerBoundaryType_20231013',
    'CustomerDashboard',
    'CustomerDashboard_20250630',
    'CustomerDashBoard_DEVOPS_6332',
    'CustomerDashboard_DEVOPS_6448',
    'CustomerIdentityProvider',
    'CustomerLicensedFeatureOptions',
    'CustomerLicensedFeatureOptions_20240327',
    'CustomerMaterialType_20231013',
    'CustomerSurveyorMapping',
    'CustomerSurveyorMasterParameterMapping',
    'CustomerSurveyorMasterParameterMapping_20240327',
    'CustomerSurveyorMasterParameterMapping_20240327_RRA',
    'CustomerSurveyorMasterParameterMapping_20250425',
    'CustomerSurveyorMasterParameterMappingHistory',
    'CustomerSurveyorMasterParameterMappingHistory_20240327',
    'CustomerViewConfiguration',
    'EmissionSource',
    'EmissionSourceRiskScoreMeta',
    'EQConfidenceGroup',
    'EQInvalidPeakArchive',
    'EQPeakArchive',
    'EQPeakWindMetricArchive',
    'EQSourceArchive',
    'EQSourceComparisonArchive',
    'EQSourceEQPeakArchive',
    'EthaneAnalysisDispositionTypes',
    'ExternalSystem',
    'FieldDataType',
    'FTPConfiguration',
    'FTPLog',
    'GeoServerConfiguration',
    'GeoServerConfiguration_20231013',
    'GPSRaw',
    'HandheldTimeseriesCheckpoint',
    'HardwareCapabilityTypes',
    'Inlet',
    'InvalidPeak',
    'InvestigationAssignment',
    'InvestigationDataType',
    'InvestigationSession',
    'InvestigationStatusTypes',
    'InvestigationTemplate',
    'InvestigationTemplateItem',
    'InvestigationTemplateItem_20240910',
    'InvestigationTemplateItem_20240919',
    'InvestigationTemplateType',
    'IsotopicIdentity',
    'Label',
    'LeakLocationTypes',
    'LeakSourceTypes',
    'LeakTypes',
    'LicensedFeature',
    'LicensedFeature_20240327',
    'LicensedFeatureOptions',
    'LicensedFeatureOptions_20240327',
    'Location',
    'LocationAnalyticsParameter',
    'LocationEQParameter',
    'LocationFOV3Parameter',
    'LocationLisaParameter',
    'LocationPipeLineParameter',
    'MasterInvestigationItem',
    'MasterInvestigationItem_20240910',
    'MasterInvestigationItem_20240919',
    'MasterParameter',
    'MasterParameter_20240327',
    'Measurement',
    'Note',
    'OTAStatusTypes',
    'ParameterGroup',
    'ParameterGroup_20240327',
    'ParameterType',
    'Peak',
    'PeakArchive',
    'PeakAutomatedEmissionSourceMapping',
    'PeakEmissionSourceMapping',
    'PreviousUserPassword',
    'ReadingUnitTypes',
    'ReferenceGasBottle',
    'Report',
    'ReportArea',
    'ReportAreaCovered',
    'ReportAreaModeType',
    'ReportAsset',
    'ReportAssetLayer',
    'ReportBoundaryLayer',
    'ReportBreadCrumbAggregated',
    'ReportCaptureEvent',
    'ReportCompliance',
    'ReportDrivingSurvey',
    'ReportEQ',
    'ReportEQResults',
    'ReportEvent',
    'ReportEventType',
    'ReportFieldOfViewAggregated',
    'ReportGap',
    'ReportImageJob',
    'ReportInvestigation',
    'ReportInvestigationItem',
    'ReportJob',
    'ReportJobStatusType',
    'ReportJobType',
    'ReportLabel',
    'ReportLeak',
    'ReportParameterMapping',
    'ReportPeakArchive',
    'ReportStatusType',
    'ReportSummary',
    'ReportTransferStatus',
    'ReportType',
    'ReportView',
    'ResourceReservation',
    'Resources',
    'Role',
    'Segment',
    'ServerLog',
    'SnappedPeak',
    'SnappedPeakArchive',
    'SnappedSegment',
    'SurfaceOverLeakTypes',
    'Survey',
    'SurveyArea',
    'SurveyCondition',
    'SurveyJob',
    'SurveyModeType',
    'SurveyModeTypeConfiguration',
    'SurveyorUnit',
    'SurveyQACheck',
    'SurveyResult',
    'TimeZone',
    'TimeZoneAdjustmentRule',
    'TimeZoneList',
    'UnitMeasurementDistances',
    'UnitMeasurementFlows',
    'UnitMeasurementSpeeds',
    'User',
    'UserAccountManagement',
    'UserClaim',
    'UserLogin',
    'UserPreference',
    'UserRole',
    'ViewConfiguration',
]
