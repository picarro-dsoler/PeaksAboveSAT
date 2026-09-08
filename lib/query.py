from locallib.query.Query import Query
from locallib.picarrodb import *

def setup_query(query_func):
    def wrapper(*args, **kwargs):
        query = query_func(*args, **kwargs)
        return Query(query = query)
    return wrapper

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
def get_surveys(user_table, survey_table,start_date,end_date = None):
    query = f"""
    SELECT 
        s.Id as SurveyId,
        s.UserId as UserId,
        u.UserName as UserName,
        su.Description as SurveyorUnit,
        a.SerialNumber as AnalyzerSerialNumber,
        s.Tag as SurveyTag,
        sa.externalid as BoundaryName
    INTO {survey_table} FROM Survey s
    JOIN [User] u ON s.UserId = u.Id
    LEFT JOIN Analyzer a ON s.AnalyzerId = a.Id
    LEFT JOIN SurveyorUnit su ON s.SurveyorUnitId = su.Id
    LEFT JOIN SurveyArea sa ON s.Id = sa.SurveyId
    WHERE UserId IN (SELECT UserId FROM {user_table})
    AND s.StartDateTime >= '{start_date}'   
    """
    if end_date:
        query += f"AND s.StartDateTime <= '{end_date}'"
    return query

@setup_query
def get_peak_table(survey_table, user_table, threshold_lower):
    query = f"""
    SELECT 
        s.SurveyId,
        s.UserId,
        s.UserName,
        s.SurveyTag,
        s.AnalyzerSerialNumber,
        s.SurveyorUnit,
        s.BoundaryName,
        'P' + LEFT(p.Id, 6) as PeakName,
        p.Id as PeakId,
        p.Disposition as Disposition,
        p.Lisa.STAsText() as PeakWkt4326,
        p.PlumeEmissionRate as EmissionRate,
        p.GpsLatitude as PeakGpsLatitude,
        p.GpsLongitude as PeakGpsLongitude,
        p.PlumeEpochStart as PeakPlumeEpochStart,
        p.PlumeEpochEnd as PeakPlumeEpochEnd
    FROM Peak p
    JOIN {survey_table} s ON p.SurveyId = s.SurveyId
    WHERE p.SurveyId IN (SELECT SurveyId FROM {survey_table}) AND
    p.PlumeEmissionRate >= {threshold_lower}
    """
    return query

@setup_query
def get_boundary_table(boundary_table):
    query = f""" SELECT 
    externalid as BoundaryName,
    ST_AsText(geom) AS BoundaryWkt4326
    FROM {boundary_table}"""
    return query