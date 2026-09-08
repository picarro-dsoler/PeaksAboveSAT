from locallib.query.Query import Query
from locallib.picarrodb import *

def setup_query(query_func):
    def wrapper(*args, **kwargs):
        query = query_func(*args, **kwargs)
        return Query(query = query)
    return wrapper

@setup_query
def get_report_info(report_table, table_name = None):
    # Always fully qualify ReportId when ambiguous (table.ReportId)
    report_id_filter = f"R.Id IN (SELECT t.ReportId FROM {report_table} t)"
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""

    query = f"""
    WITH SurveyCTE AS (
        SELECT 
            S.Id AS SurveyId,
            S.StartDateTime,
            S.EndDateTime,
            RDS.ReportId
        FROM
            Survey S
            INNER JOIN ReportDrivingSurvey RDS ON S.Id = RDS.SurveyId
        WHERE 
            RDS.ReportId IN (SELECT t.ReportId FROM {report_table} t)
    ),
    LabelCTE AS (
        SELECT 
            RL.ReportId,
            STRING_AGG(L.Title, ' | ') AS Labels
        FROM
            ReportLabel RL
            INNER JOIN Label L ON RL.LabelId = L.Id
        WHERE 
            RL.IsActive = 1 
            AND RL.ReportId IN (SELECT t.ReportId FROM {report_table} t)
        GROUP BY RL.ReportId
    )
    SELECT 
        C.Name AS CustomerName,
        CASE
            WHEN ReportType.Description = 'Compliance' THEN CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            WHEN ReportType.Description = 'Emissions' THEN CONCAT('ER-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            ELSE CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
        END AS ReportName,
        R.Id AS ReportId,
        R.ReportTitle AS ReportTitle,
        L.Title AS FinalCheckboxLabel,
        (SELECT Labels FROM LabelCTE WHERE LabelCTE.ReportId = R.Id) AS Labels,
        -- Get the earliest and latest survey start time per report from SurveyCTE
        (SELECT MIN(StartDateTime) FROM SurveyCTE WHERE SurveyCTE.ReportId = R.Id) AS EarliestSurveyStart,
        (SELECT MIN(EndDateTime) FROM SurveyCTE WHERE SurveyCTE.ReportId = R.Id) AS EarliestSurveyEnd,
        (SELECT MAX(StartDateTime) FROM SurveyCTE WHERE SurveyCTE.ReportId = R.Id) AS LatestSurveyStart,
        (SELECT MAX(EndDateTime) FROM SurveyCTE WHERE SurveyCTE.ReportId = R.Id) AS LatestSurveyEnd,
        R.DateStarted AS ReportDate,
        RA.ExternalId AS BoundaryName,
        RA.Shape.STAsText() AS ReportArea,
        RAC.AssetLengthKM AS ReportAssetLengthKm,
        RC.PercentCoverageAssets AS ReportPercentCoverageAssets,
        RAC.AssetLengthKM * RC.PercentCoverageAssets AS AssetCoveredLengthKm,
        RAC.DistributionPipeCoveredKm,
        RAC.DistributionPipeKm,
        RAC.DistributionPipePercentCovered,
        RAC.ServicePipeKm,
        RAC.ServicePipeCoveredKm,
        (SELECT Description from TimeZone where Id = R.TimeZoneId) AS TimeZone
    {into_clause}
    FROM
        Report R
    LEFT JOIN Customer C ON
        R.CustomerId = C.Id
    LEFT JOIN ReportLabel RL ON
        R.Id = RL.ReportId
    LEFT JOIN Label L ON
        RL.LabelId = L.Id
    LEFT JOIN ReportType ON
        R.ReportTypeId = ReportType.Id
    LEFT JOIN ReportArea RA ON R.Id = RA.ReportId
    LEFT JOIN ReportCompliance RC ON R.Id = RC.ReportId
    LEFT JOIN ReportAreaCovered RAC ON R.Id = RAC.ReportId
    WHERE
        {report_id_filter}
    AND L.Title = 'Final Checkbox'
        AND RL.IsActive = 1 
    """
    return query

@setup_query
def get_reports(customer_name, table_name = None, years=None, start_date = None, end_date = None, final_checkbox = True):
    year_filter = ""
    start_date_filter = ""
    end_date_filter = ""

    # Make year filter mutually exclusive with start/end date; prioritize date range if specified
    if start_date or end_date:
        if start_date:
            start_date_filter = f"AND R.DateStarted >= '{start_date}'"
        if end_date:
            end_date_filter = f"AND R.DateStarted <= '{end_date}'"
        # If date range is specified, ignore years
        year_filter = ""
    elif years:
        years_str = ", ".join(str(year) for year in years)
        year_filter = f"AND YEAR(R.DateStarted) IN ({years_str})"

    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""

    if final_checkbox:
        label_filter = "AND L.Title = 'Final Checkbox'"
    else:
        label_filter = ""

    query = f"""
    SELECT 
        C.Name AS CustomerName,
        CASE
            WHEN ReportType.Description = 'Compliance' THEN CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            WHEN ReportType.Description = 'Emissions' THEN CONCAT('ER-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            ELSE CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
        END AS ReportName,
        R.Id AS ReportId,
        R.ReportTitle AS ReportTitle,
        R.DateStarted AS ReportDate,
        RA.ExternalId AS BoundaryName,
        RA.BoundaryType AS BoundaryType,
        RA.Shape.STAsText() AS ReportArea,
        RAC.AssetLengthKM AS ReportAssetLengthKm,
        RC.PercentCoverageAssets AS ReportPercentCoverageAssets,
        RAC.AssetLengthKM * RC.PercentCoverageAssets AS AssetCoveredLengthKm,
        STUFF((SELECT DISTINCT ', ' + L.Title
               FROM ReportLabel RL
               INNER JOIN Label L ON RL.LabelId = L.Id
               WHERE RL.ReportId = R.Id AND RL.IsActive = 1 AND L.Title IS NOT NULL
               FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS Labels,
        RAC.DistributionPipeKm,
        RAC.DistributionPipeCoveredKm,
        RAC.DistributionPipePercentCovered,
        RAC.ServicePipeKm,
        RAC.ServicePipeCoveredKm,
        RAC.AreaKM2,
        RAC.AreaCoveredKM2,
        YEAR(R.DateStarted) AS ReportYear,
        MONTH(R.DateStarted) AS ReportMonth,
        DATEPART(WEEK, R.DateStarted) AS ReportWeek,
        DATEPART(QUARTER, R.DateStarted) AS ReportQuarter
    {into_clause}
    FROM
        Report R
    LEFT JOIN Customer C ON
        R.CustomerId = C.Id
    LEFT JOIN ReportLabel RL ON
        R.Id = RL.ReportId
    LEFT JOIN Label L ON
        RL.LabelId = L.Id
    LEFT JOIN ReportType ON
        R.ReportTypeId = ReportType.Id
    LEFT JOIN ReportArea RA ON R.Id = RA.ReportId
    LEFT JOIN ReportCompliance RC ON R.Id = RC.ReportId
    LEFT JOIN ReportAreaCovered RAC ON R.Id = RAC.ReportId
    WHERE
        LOWER(C.Name) = LOWER('{customer_name}')
        AND L.Title = 'Final Checkbox'
        AND RL.IsActive = 1
        {year_filter}

    GROUP BY
        C.Name,
        R.Id,
        R.ReportTitle,
        R.DateStarted,
        RA.ExternalId,
        RA.BoundaryType,
        RAC.AssetLengthKM,
        RA.Shape.STAsText(),
        ReportType.Description,
        RAC.AssetLengthKM,
        RAC.AreaCoveredKM2,
        RC.PercentCoverageAssets,
        RAC.DistributionPipeKm,
        RAC.DistributionPipeCoveredKm,
        RAC.DistributionPipePercentCovered,
        RAC.ServicePipeKm,
        RAC.ServicePipeCoveredKm,
        RAC.AreaKM2,
        RAC.AreaCoveredKM2
    """
    return query

def get_final_reports(customer_name, table_name = None, years=None):
    if isinstance(customer_name, list):
        customer_name_clauses = []
        for name in customer_name:
            customer_name_clauses.append(f"LOWER(C.Name) = LOWER('{name}')")
        customer_name_filter = " OR ".join(customer_name_clauses)
        customer_name_filter = f"({customer_name_filter})"
    else:
        customer_name_filter = f"LOWER(C.Name) = LOWER('{customer_name}')"
    year_filter = ""
    if years:
        years_str = ", ".join(str(year) for year in years)
        year_filter = f"AND YEAR(R.DateStarted) IN ({years_str})"

    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""

    query = f"""
    SELECT 
        C.Name AS CustomerName,
        CASE
            WHEN ReportType.Description = 'Compliance' THEN CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            WHEN ReportType.Description = 'Emissions' THEN CONCAT('ER-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            ELSE CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
        END AS ReportName,
        R.Id AS ReportId,
        R.ReportTitle AS ReportTitle,
        L.Title AS Label,
        R.DateStarted AS ReportDate,
        RA.ExternalId AS BoundaryName,
        RAC.AssetLengthKM AS ReportAssetLengthKm,
        RC.PercentCoverageAssets AS ReportPercentCoverageAssets,
        RAC.AssetLengthKM * RC.PercentCoverageAssets AS AssetCoveredLengthKm,
        RAC.DistributionPipeCoveredKm,
        RAC.DistributionPipePercentCovered,
        RAC.ServicePipeKm,
        RAC.ServicePipeCoveredKm
    {into_clause}
    FROM
        Report R
    LEFT JOIN Customer C ON
        R.CustomerId = C.Id
    LEFT JOIN ReportLabel RL ON
        R.Id = RL.ReportId
    LEFT JOIN Label L ON
        RL.LabelId = L.Id
    LEFT JOIN ReportType ON
        R.ReportTypeId = ReportType.Id
    LEFT JOIN ReportArea RA ON R.Id = RA.ReportId
    LEFT JOIN ReportCompliance RC ON R.Id = RC.ReportId
    LEFT JOIN ReportAreaCovered RAC ON R.Id = RAC.ReportId
    WHERE
        {customer_name_filter}
        AND L.Title = 'Final Checkbox'
        AND RL.IsActive = 1
        {year_filter}
    """
    return query

@setup_query
def get_emission_soruces_for_RER(report_table, table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""

    query = f"""
    SELECT 
        Es.ReportId,
        YEAR(R.DateStarted) AS Year,
        R.DateStarted AS ReportDate,
        Es.Id,
        Es.Disposition,
        Es.IsFiltered,
        Es.CH4,
        RA.ExternalId AS BoundaryName,
        ES.EmissionRate,
        ES.EmissionRateAMean,
        ES.EmissionRateAStd,
        ES.EmissionRateGMean,
        ES.EmissionRateGStd,
        ES.EmissionRateLowerBound,
        ES.EmissionRateUpperBound,
        ES.EthaneRatio,
        ES.NumberOfPasses,
        ES.NumberOfPeaks,
        ES.PeakNumber,
        ES.RepresentativeEmissionRate,
        ES.RepresentativeBinLabel,
        ES.PriorityScore2,
        ES.EthaneRatioUncertainty
    FROM
        EmissionSource ES
    LEFT JOIN Report R ON ES.ReportId = R.Id
    LEFT JOIN ReportArea RA ON ES.ReportId = RA.ReportId
    WHERE
        ES.ReportId IN (SELECT ReportId FROM {report_table})
        AND ES.EmissionRate > 0 
        AND (Es.Disposition = 1 OR Es.Disposition = 3)
    """
    return query
@setup_query
def query_reports_view(report_table,table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query =  f"""select 
    customer_shortname  as "CustomerShortName",
    rp_id  as "ReportId",
    rp_percentcoverageassets as "ReportPercentCoverageAssets_DH",
    lisa_count as "LisaCount",
    rp_title as "ReportTitle",
    rp_name as "ReportName",
    rp_date as "ReportDate",
    rp_label_final as "ReportLabelFinal",
    rp_label_other as "ReportLabelOther",
    bo_name as "BoundaryName",
    bo_mode as "BoundaryMode",
    bo_type as "BoundaryType",
    bo_plant as "BoundaryPlant",
    bo_subplant as "BoundarySubplant",
    bo_region as "BoundaryRegion",
    bo_subregion as "BoundarySubRegion",
    bo_subsubregion as "BoundarySubSubRegion",
    bo_km_network as "BoundaryKmNetwork",
    EXTRACT(YEAR FROM rp_date) as "Year",
    EXTRACT(MONTH FROM rp_date) as "Month"
    {into_clause}
    from dash.v_report 
    where rp_id IN (SELECT LOWER(ReportId::text)::uuid FROM {report_table})"""
    return query

def query_reports_view_by_name(report_table,table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query =  f"""select 
    customer_shortname  as "CustomerShortName",
    rp_id  as "ReportId",
    rp_percentcoverageassets as "ReportPercentCoverageAssets_DH",
    lisa_count as "LisaCount",
    rp_name as "ReportName",
    rp_date as "ReportDate",
    rp_title as "ReportTitle",
    rp_label_final as "ReportLabelFinal",
    rp_label_other as "ReportLabelOther",
    bo_name as "BoundaryName",
    bo_mode as "BoundaryMode",
    bo_type as "BoundaryType",
    bo_plant as "BoundaryPlant",
    bo_subplant as "BoundarySubplant",
    bo_region as "BoundaryRegion",
    bo_subregion as "BoundarySubRegion",
    bo_km_network as "BoundaryKmNetwork",
    EXTRACT(YEAR FROM rp_date) as "Year",
    EXTRACT(MONTH FROM rp_date) as "Month"
    {into_clause}
    from dash.v_report 
    where rp_name IN (SELECT ReportName FROM {report_table})"""
    return query

@setup_query
def query_reports_view_by_year(customer_name, years = None, table_name = None,limit = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    years_str = ", ".join(str(year) for year in years)
    if limit is not None:
        limit_clause = f"LIMIT {limit}"
    else:
        limit_clause = ""
    query =  f"""select 
    customer_shortname  as "customershortname",
    rp_id  as "reportid",
    rp_percentcoverageassets as "ReportPercentCoverageAssets_DH",
    lisa_count as "lisacount",
    rp_name as "reportname",
    rp_date as "reportdate",
    rp_label_final as "reportlabelfinal",
    rp_label_other as "reportlabelother",
    bo_name as "boundaryname",
    bo_mode as "boundarymode",
    bo_type as "boundarytype",
    bo_plant as "boundaryplant",
    bo_subplant as "boundariesubplant",
    bo_region as "boundaryregion",
    bo_subregion as "boundariesubregion",
    bo_km_network as "boundarykmnetwork",
    EXTRACT(YEAR FROM rp_date) as "Year",
    EXTRACT(MONTH FROM rp_date) as "Month"
    {into_clause}
    from dash.v_report 
        where customer_shortname = '{customer_name}'
        and EXTRACT(YEAR FROM rp_date) IN ({years_str})
        {limit_clause}"""
    return query



def reports_view(customer_name, years, is_final_checkbox):
    # Convert the list of years to a string for the SQL IN clause
    years_str = ', '.join(map(str, years))
    
    # Start building the query
    query = f"""
    SELECT 
        customer_shortname AS "CustomerName",
        rp_id AS "ReportId",
        rp_name AS "ReportName",
        rp_title AS "ReportTitle",
        rp_date AS "ReportDate",
        rp_time AS "ReportTime",
        rp_percentcoverageassets AS "ReportPercentCoverageAssets",
        lisa_count AS "LisaCount",
        rp_label_final AS "ReportLabelFinal",
        rp_label_other AS "ReportLabelOther",
        bo_mode AS "BoundaryMode",
        bo_name AS "BoundaryName",
        bo_type AS "BoundaryType",
        bo_plant AS "BoundaryPlant",
        bo_subplant AS "BoundarySubplant",
        bo_region AS "BoundaryRegion",
        bo_subregion AS "BoundarySubRegion",
        bo_km_network AS "BoundaryKmNetwork"
    FROM dash.v_report vr 
    WHERE customer_shortname = '{customer_name}'
    AND EXTRACT(YEAR FROM rp_date) IN ({years_str})
    """
    
    # Conditionally add the rp_label_final filter
    if is_final_checkbox:
        query += "AND rp_label_final = 'Final Checkbox' "
    
    return query

@setup_query
def survey_query(report_table=None, table_name=None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""
    SELECT
        UPPER(C.Name) CustomerName,
        CASE
            WHEN ReportType.Description = 'Compliance' THEN CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            WHEN ReportType.Description = 'Emissions' THEN CONCAT('ER-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
            ELSE CONCAT('CR-', SUBSTRING(CONVERT(nvarchar(50), R.Id), 1, 6))
        END AS ReportName,
        R.Id AS ReportId,
        S.Tag,
        U.UserName,
        A.SerialNumber AnalyzerSerialNumber,
        S.StartDateTime AS StartDateTimeSurvey,
        S.EndDateTime   AS EndDateTimeSurvey,
        U.FirstName UserFirstName,
        U.LastName UserLastName,
        U.FirstName + ' ' + U.LastName AS Driver,
        S.Id AS SurveyId,
        S.StartDateTime,
        S.EndDateTime,
        S.StabilityClass,
        S.Status,
        S.BuildNumber,
        S.AnalyzerId,
        S.ReferenceGasBottleId,
        SU.Description SurveyorUnit,
        SMT.Description SurveyMode,
        S.DrivingLengthMeters / 1000 AS DrivingLengthKM,
        S.DrivingLengthMeters / 1000 * 0.621371 AS DrivingLengthMiles,
        ROUND((SELECT SUM(DurationSeconds) FROM Segment WHERE SurveyId = S.Id AND Mode = 0), 0) DurationSeconds,
        (SELECT SUM(DurationSeconds) / 60.0
        FROM Segment
        WHERE SurveyId = S.Id AND Mode = 0) AS DurationMinutes,
        DATEDIFF(MINUTE, S.StartDateTime, S.EndDateTime) AS RawDurationMinutes,
        S.StartEpoch,
        S.EndEpoch,
        L.Description AS Zone ,
        TZ.Description AS TimeZone
    {into_clause}
    FROM Customer C
        INNER JOIN [User] U ON C.Id = U.CustomerId
        INNER JOIN Survey S ON U.Id = S.UserId
        INNER JOIN ReportDrivingSurvey RDS on S.Id = RDS.SurveyId
        INNER JOIN Report R on RDS.ReportId = R.Id
        INNER JOIN ReportType ON R.ReportTypeId = ReportType.Id
        INNER JOIN Location L ON S.LocationId  = L.Id
        INNER JOIN TimeZone TZ ON U.TimeZoneId = TZ.Id
        LEFT JOIN Analyzer A ON S.AnalyzerId = A.Id
        LEFT JOIN SurveyorUnit SU on S.SurveyorUnitId = SU.Id
        LEFT JOIN SurveyModeType SMT on S.SurveyModeTypeId = SMT.Id
    WHERE R.Id  IN (SELECT ReportId FROM {report_table})
    """
    return query

@setup_query
def get_surveys(user_table, start_date = None, survey_table = None, end_date = None):
    if survey_table is not None:
        into_clause = f"INTO {survey_table}"
    else:
        into_clause = ""
    if start_date is not None:
        start_date_clause = f"AND s.StartDateTime >= '{start_date}'"
    else:
        start_date_clause = ""
    query = f"""
    SELECT 
        s.Id as SurveyId,
        s.UserId as UserId,
        u.UserName as UserName,
        su.Description as SurveyorUnit,
        a.SerialNumber as AnalyzerSerialNumber,
        s.Tag as SurveyTag,
        S.StartDateTime AS StartDateTimeSurvey,
        S.EndDateTime   AS EndDateTimeSurvey,
        U.FirstName + ' ' + U.LastName AS Driver,
        S.StartDateTime,
        S.EndDateTime,
        S.StabilityClass,
        S.Status,
        SA.Shape.STAsText() as SurveyArea,
        S.BuildNumber,
        S.AnalyzerId,
        S.ReferenceGasBottleId,
        S.DrivingLengthMeters / 1000 AS DrivingLengthKM,
        S.DrivingLengthMeters / 1000 * 0.621371 AS DrivingLengthMiles,
        ROUND((SELECT SUM(DurationSeconds) FROM Segment WHERE SurveyId = S.Id AND Mode = 0), 0) DurationSeconds,
        (SELECT SUM(DurationSeconds) / 60.0
        FROM Segment
        WHERE SurveyId = S.Id AND Mode = 0) AS DurationMinutes,
    DATEDIFF(MINUTE, S.StartDateTime, S.EndDateTime) AS RawDurationMinutes
    {into_clause} FROM Survey s
    JOIN [User] u ON s.UserId = u.Id
    JOIN SurveyArea SA ON s.Id = SA.SurveyId
    INNER JOIN Analyzer a ON s.AnalyzerId = a.Id
    LEFT JOIN SurveyorUnit su ON s.SurveyorUnitId = su.Id
    WHERE UserId IN (SELECT UserId FROM {user_table})
    {start_date_clause}
    """
    if end_date:
        query += f"AND s.StartDateTime <= '{end_date}'"
    return query

@setup_query
def get_users(customer_name, user_table):
    query = f"""
    SELECT 
    u.Id as UserId,
    u.UserName as UserName
    INTO {user_table}
    FROM [User] u
    JOIN Customer c ON c.id = u.CustomerId 
    WHERE 
    LOWER(c.Name) = LOWER('{customer_name}')
    """
    return query

@setup_query
def emission_sources_table_dispo2_given_report_id(report_table=None,table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""
    SELECT
        UPPER(CONVERT(NVARCHAR(50), ES.Id))     AS EmissionSourceId,
        ES.PeakNumber AS LisaNumber,
        CASE
            WHEN ES.UniqueIdentifier IS NOT NULL THEN ES.UniqueIdentifier
            ELSE
                CONCAT(
                    'CR-',
                    SUBSTRING(CONVERT(nvarchar(50), ES.ReportId), 1, 6),
                    CASE
                        WHEN ES.PeakNumber >= 0 THEN '-L-'
                        ELSE '-LF-'
                    END,
                    ABS(ES.PeakNumber)
                )
        END AS UniqueIdentifier,
        ES.CH4,
        ES.ClassificationConfidence,
        ES.RepresentativePeakId,
        ES.PriorityScore2,
        ES.Disposition,
        ES.DetectionProbability,
        ES.EmissionRate,
        ES.EmissionRateAMean,
        ES.EmissionRateAStd,
        ES.EmissionRateGMean,
        ES.EmissionRateGStd,
        ES.EmissionRateLowerBound,
        ES.EmissionRateUpperBound,
        ES.EthaneRatio,
        ES.EthaneRatioUncertainty,
        ES.GeocodeAddress,
        ES.GpsLatitude AS LisaLatitude,
        ES.GpsLongitude AS LisaLongitude,
        ES.Lisa.STAsText() AS LisaGeometry,
        ES.IsFiltered,
        ES.MaxAmplitude,
        ES.MaxCarSpeed,
        ROUND(CAST(ES.NumberOfPeaks AS FLOAT) / NULLIF(CAST(ES.NumberOfPasses AS FLOAT), 0), 2) AS Persistence,
        ES.MaxWindSpeed,
        ES.MinWindSpeed,
        ES.NumberOfPasses,
        ES.NumberOfPeaks,
        ES.PeakNumber,
        ES.PriorityScore,
        ES.RankingGroup AS RiskRankingBin,
        (SELECT SurveyId FROM Peak WHERE Id = ES.RepresentativePeakId) AS SurveyId,
        ES.ReportId,
        ES.EmissionRate * 0.471947 AS "EmissionRate(lpm)",
        ES.EmissionRate * 19.1 AS "EmissionRate(g/h)",
        ES.RepresentativeEmissionRate,
        ES.RepresentativeEmissionRate * 0.471947 AS "RepresentativeEmissionRate(lpm)",
        ES.RepresentativeEmissionRate * 19.1 AS "RepresentativeEmissionRate(g/h)",
        ES.RepresentativeBinLabel,
        P.EpochTime AS RepresentativePeakEpochTime,
        STUFF((SELECT DISTINCT ' | ' + L.Title
               FROM ReportLabel RL
               INNER JOIN Label L ON RL.LabelId = L.Id
               WHERE RL.ReportId = R.Id AND RL.IsActive = 1
               FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS Labels,
        (SELECT COUNT(DISTINCT L.Title)
         FROM ReportLabel RL
         INNER JOIN Label L ON RL.LabelId = L.Id
         WHERE RL.ReportId = R.Id AND RL.IsActive = 1) AS NumberOfLabels,
        TZ.Description AS CommonTimeZone
    {into_clause}
    FROM Customer C
    JOIN Report R ON C.Id = R.CustomerID
    JOIN EmissionSource ES ON R.Id = ES.ReportId
    LEFT JOIN Peak P ON ES.RepresentativePeakId = P.Id
    LEFT JOIN ReportCompliance RC ON R.Id = RC.ReportId
    LEFT JOIN ReportStatusType RST ON R.ReportStatusTypeId = RST.Id
    LEFT JOIN ReportAreaCovered RAC ON R.Id = RAC.ReportId
    INNER JOIN ReportType ON R.ReportTypeId = ReportType.Id
    INNER JOIN TimeZone TZ ON R.TimeZoneId = TZ.Id
    WHERE R.Id IN (SELECT ReportId FROM {report_table})"""
    return query


@setup_query
def emission_sources_table_query_given_report_id(report_table=None,table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""
    SELECT
        UPPER(CONVERT(NVARCHAR(50), ES.Id))     AS EmissionSourceId,
        ES.PeakNumber AS LisaNumber,
        CASE
            WHEN ES.UniqueIdentifier IS NOT NULL THEN ES.UniqueIdentifier
            ELSE
                CONCAT(
                    'CR-',
                    SUBSTRING(CONVERT(nvarchar(50), ES.ReportId), 1, 6),
                    CASE
                        WHEN ES.PeakNumber >= 0 THEN '-L-'
                        ELSE '-LF-'
                    END,
                    ABS(ES.PeakNumber)
                )
        END AS UniqueIdentifier,
        ES.CH4,
        ES.ClassificationConfidence,
        ES.RepresentativePeakId,
        ES.PriorityScore2,
        ES.Disposition,
        ES.DetectionProbability,
        ES.EmissionRate,
        ES.EmissionRateAMean,
        ES.EmissionRateAStd,
        ES.EmissionRateGMean,
        ES.EmissionRateGStd,
        ES.EmissionRateLowerBound,
        ES.EmissionRateUpperBound,
        ES.EthaneRatio,
        ES.EthaneRatioUncertainty,
        ES.GeocodeAddress,
        ES.GpsLatitude AS LisaLatitude,
        ES.GpsLongitude AS LisaLongitude,
        ES.Lisa.STAsText() AS LisaGeometry,
        ES.IsFiltered,
        ES.MaxAmplitude,
        ES.MaxCarSpeed,
        ROUND(CAST(ES.NumberOfPeaks AS FLOAT) / NULLIF(CAST(ES.NumberOfPasses AS FLOAT), 0), 2) AS Persistence,
        ES.MaxWindSpeed,
        ES.MinWindSpeed,
        ES.NumberOfPasses,
        ES.NumberOfPeaks,
        ES.PeakNumber,
        ES.PriorityScore,
        ES.RankingGroup AS RiskRankingBin,
        (SELECT SurveyId FROM Peak WHERE Id = ES.RepresentativePeakId) AS SurveyId,
        ES.ReportId,
        ES.EmissionRate * 0.471947 AS "EmissionRate(lpm)",
        ES.EmissionRate * 19.1 AS "EmissionRate(g/h)",
        ES.RepresentativeEmissionRate,
        ES.RepresentativeEmissionRate * 0.471947 AS "RepresentativeEmissionRate(lpm)",
        ES.RepresentativeEmissionRate * 19.1 AS "RepresentativeEmissionRate(g/h)",
        ES.RepresentativeBinLabel,
        P.EpochTime AS RepresentativePeakEpochTime,
        STUFF((SELECT DISTINCT ' | ' + L.Title
               FROM ReportLabel RL
               INNER JOIN Label L ON RL.LabelId = L.Id
               WHERE RL.ReportId = R.Id AND RL.IsActive = 1
               FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS Labels,
        (SELECT COUNT(DISTINCT L.Title)
         FROM ReportLabel RL
         INNER JOIN Label L ON RL.LabelId = L.Id
         WHERE RL.ReportId = R.Id AND RL.IsActive = 1) AS NumberOfLabels,
        TZ.Description AS CommonTimeZone
    {into_clause}
    FROM Customer C
    JOIN Report R ON C.Id = R.CustomerID
    JOIN EmissionSource ES ON R.Id = ES.ReportId
    LEFT JOIN Peak P ON ES.RepresentativePeakId = P.Id
    LEFT JOIN ReportCompliance RC ON R.Id = RC.ReportId
    LEFT JOIN ReportStatusType RST ON R.ReportStatusTypeId = RST.Id
    LEFT JOIN ReportAreaCovered RAC ON R.Id = RAC.ReportId
    INNER JOIN ReportType ON R.ReportTypeId = ReportType.Id
    INNER JOIN TimeZone TZ ON R.TimeZoneId = TZ.Id
    WHERE R.Id IN (SELECT ReportId FROM {report_table}) AND (ES.Disposition = 1 OR ES.Disposition = 3)"""
    return query

@setup_query
def query_box_table(report_table = None, table_name = None, indication_type = 'L'):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    if indication_type is not None:
        if indication_type == 'L':
            indication_type_clause = f"AND B.UniqueIdentifier LIKE '%L%'"
        elif indication_type == 'G':
            indication_type_clause = f"AND B.UniqueIdentifier LIKE '%G%'"
        else:
            indication_type_clause = ""
    else:
        indication_type_clause = ""
    query = f"""SELECT B.Id as BoxId,
                B.BoxShape.STAsText() as BoxShape,
                B.EmissionSourceId as EmissionSourceId,
                (SELECT Description FROM InvestigationStatusTypes IST WHERE IST.Id = B.InvestigationStatusTypeId) AS InvestigationStatusName,
                (SELECT BT.Name FROM BoxTypes BT WHERE BT.Id = B.BoxTypeId) AS BoxType,
                B.ReportId, B.UniqueIdentifier
                {into_clause}
                FROM Box B 
                
                WHERE B.ReportId IN (SELECT ReportId FROM {report_table}) AND
                B.UniqueIdentifier NOT LIKE '%G-0'
                {indication_type_clause}
                """
    return query

@setup_query
def query_report_investigation(box_table = None, table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""SELECT RI.* , 
    (
        SELECT ITT.Name 
        FROM InvestigationTemplateType ITT 
        WHERE ITT.Id = (
            SELECT IT.InvestigationTemplateTypeId 
            FROM InvestigationTemplate IT 
            WHERE IT.Id = RI.InvestigationTemplateId
        )
    ) AS InvestigationTemplateType
    FROM ReportInvestigation RI 
    WHERE RI.BoxId IN (SELECT BoxId FROM {box_table})"""
    return query

@setup_query
def query_InvestigationStatusTypes():
    IST = InvestigationStatusTypes.copy()
    query = f"""SELECT {IST.get_columns()} FROM {IST.get_table_name()} IST"""
    return query

@setup_query
def query_report_asset_coverage(report_table = None, table_name = None):
    RAC = ReportAreaCovered.copy()
    RAC.delete_column('Id')
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""SELECT {RAC.get_columns()} {into_clause} FROM ReportAreaCovered RAC WHERE RAC.ReportId IN (SELECT ReportId FROM {report_table})"""
    return query

@setup_query
def query_emission_sources_table(report_table = None, table_name = None):
    ES_Columns = EmissionSource.copy()
    ES_Columns.delete_column('Lisa')
    ES_Columns.set_column_alias('Id','EmissionSourceId')

    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""SELECT {ES_Columns.get_columns()} {into_clause} FROM EmissionSource ES WHERE ES.ReportId IN (SELECT ReportId FROM {report_table})"""
    return query

@setup_query
def query_surveys_table(report_table = None, table_name = None):
    Survey_Columns = Survey.copy()
    Survey_Columns.delete_column('SurveyAreaBoundary')
    Survey_Columns.set_column_alias('Id','SurveyId')
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""SELECT {Survey_Columns.get_columns()},
    SQC.LateralRotation as LateralRotation,
    SQC.NumberOfPeaks as NumberOfPeaks,
    (SELECT Description FROM SurveyorUnit SU WHERE SU.Id = S.SurveyorUnitId) AS SurveyorUnit, 
    (SELECT SerialNumber FROM Analyzer A WHERE A.Id = S.AnalyzerId) AS AnalyzerSerialNumber,
    RDS.ReportId AS ReportId 
    {into_clause} FROM Survey S 
    LEFT JOIN ReportDrivingSurvey RDS ON S.Id = RDS.SurveyId
    LEFT JOIN SurveyQACheck SQC ON S.Id = SQC.SurveyId
    WHERE RDS.ReportId IN (SELECT ReportId FROM {report_table})"""
    return query


@setup_query
def query_segments_table(survey_table = None, table_name = None):
    segments_Columns = Segment.copy()
    #segments_Columns.delete_column('Shape')
    segments_Columns.delete_column('Order')
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    query = f"""SELECT {segments_Columns.get_columns()}, S.[Order] as [Order] {into_clause} FROM Segment S WHERE S.SurveyId IN (SELECT SurveyId FROM {survey_table}) """
    return query


@setup_query
def query_SurveyH3Aggregation(survey_table = None, table_name = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    segment_union_query = f"""
    SELECT 
        S.SurveyId,
        geometry::UnionAggregate(S.Shape).STAsText() AS Breadcrumb
    {into_clause}
    FROM Segment S
    WHERE S.SurveyId IN (SELECT SurveyId FROM {survey_table})
    GROUP BY S.SurveyId"""
    return segment_union_query


@setup_query
def query_SurveyH3Aggregation_byReport(report_table = None, table_name: str = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    segment_union_query = f"""
    SELECT 
        RDS.ReportId AS ReportId,
        S.SurveyId,
        geometry::UnionAggregate(S.Shape).STAsText() AS Breadcrumb
    {into_clause}
    FROM Segment S
    JOIN ReportDrivingSurvey RDS ON S.SurveyId = RDS.SurveyId
    WHERE RDS.ReportId IN (SELECT ReportId FROM {report_table})
    GROUP BY S.SurveyId,
    RDS.ReportId"""
    return segment_union_query

def query_Segments_byReport(report_table = None, table_name: str = None):
    if table_name is not None:
        into_clause = f"INTO {table_name}"
    else:
        into_clause = ""
    segment_union_query = f"""
    SELECT 
        RDS.ReportId AS ReportId,
        S.SurveyId,
        S.Shape.STAsText() AS Breadcrumb,
        S.[Order] as [Order]
    {into_clause}
    FROM Segment S
    JOIN ReportDrivingSurvey RDS ON S.SurveyId = RDS.SurveyId
    WHERE RDS.ReportId IN (SELECT ReportId FROM {report_table})
    """
    return segment_union_query