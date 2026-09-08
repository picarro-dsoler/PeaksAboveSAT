import pandas as pd
from datetime import datetime
import pytz

COMMON_TIMEZONE_MAPPINGS = {
    'Pacific Standard Time': 'America/Los_Angeles',
    'Mountain Standard Time': 'America/Denver',
    'Central Standard Time': 'America/Chicago',
    'Eastern Standard Time': 'America/New_York',
    'Atlantic Standard Time': 'America/Halifax',
    'Argentina Standard Time': 'America/Argentina/Buenos_Aires',
    'GMT Standard Time': 'Europe/London',
    'UTC': 'UTC',
    'W. Europe Standard Time': 'Europe/Berlin',
    'Central European Standard Time': 'Europe/Warsaw',
    'E. Europe Standard Time': 'Europe/Kiev',
    'E. Africa Standard Time': 'Africa/Nairobi',
    'Pakistan Standard Time': 'Asia/Karachi',
    'Bangladesh Standard Time': 'Asia/Dhaka',
    'SE Asia Standard Time': 'Asia/Bangkok',
    'China Standard Time': 'Asia/Shanghai',
    'Tokyo Standard Time': 'Asia/Tokyo',
    'E. Australia Standard Time': 'Australia/Brisbane',
    'Central Pacific Standard Time': 'Pacific/Guadalcanal',
    'New Zealand Standard Time': 'Pacific/Auckland',
    'Hawaiian Standard Time': 'Pacific/Honolulu',
    'Alaskan Standard Time': 'America/Anchorage',
}

@pd.api.extensions.register_dataframe_accessor("timezone")
class TimezoneAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj


    def convert_utc_column_to_local(self, utc_column_name, timezone_column_name = 'TimeZone', new_column_name = None):
        def convert_row_to_local(row):
            utc_datetime = row[utc_column_name]
            # Check if utc_datetime is not already a datetime object
            if isinstance(utc_datetime, str):
                utc_datetime = datetime.strptime(utc_datetime, '%Y-%m-%d %H:%M:%S.%f')

            common_timezone_name = row[timezone_column_name]
            iana_timezone_name = COMMON_TIMEZONE_MAPPINGS.get(common_timezone_name)

            if iana_timezone_name is None:
                return 'TimeZoneNotFound'

            # No need to localize if utc_datetime is already timezone-aware
            if utc_datetime.tzinfo is None:
                utc_localized = pytz.utc.localize(utc_datetime)
            else:
                utc_localized = utc_datetime

            target_timezone = pytz.timezone(iana_timezone_name)
            local_datetime = utc_localized.astimezone(target_timezone)
            # Format the datetime to include AM or PM
            return local_datetime.strftime('%Y-%m-%d %I:%M:%S %p')

        if new_column_name is None:
            new_column_name = utc_column_name + '_local'    
        else:
            new_column_name = new_column_name

        self._obj[new_column_name] = self._obj.apply(convert_row_to_local, axis=1)
        return self._obj
