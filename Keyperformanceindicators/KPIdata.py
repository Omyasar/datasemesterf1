import json
import numpy as np
import pandas as pd
from fastf1.core import Session
from db_conn import db_connection
import fastf1._api

conn = db_connection()
def fetch_page(path, name):
    """
    .. warning::
        :mod:`fastf1.api` will be considered private in future releases and
        potentially be removed or changed.

    Fetch data from the formula1 livetiming web api, given url base path and page name. An attempt
    to parse json or decode known messages is made.

    Args:
        path (str): api path base string (usually ``Session.api_path``)
        name (str): page name (see :attr:`pages` for all known pages)

    Returns:
        - dictionary if content was json
        - list of entries if jsonStream, where each entry again contains two elements: [timestamp, content]. Content is
          parsed with :func:`parse` and will usually be a dictionary created from json data.
        - None if request failed

    """
    page = fastf1._api.pages[name]
    is_stream = 'jsonStream' in page
    is_z = '.z.' in page
    r = Cache.requests_get(fastf1._api.base_url + path + fastf1._api.pages[name], headers=fastf1._api.headers)
    if r.status_code == 200:
        raw = r.content.decode('utf-8-sig')
        if is_stream:
            records = raw.split('\r\n')[:-1]  # last split is empty
            if name in ('position', 'car_data'):
                # Special case to improve memory efficiency
                return records
            else:
                decode_error_count = 0
                tl = 12  # length of timestamp: len('00:00:00:000')
                ret = list()
                for e in records:
                    try:
                        ret.append([e[:tl], fastf1._api.parse(e[tl:], zipped=is_z)])
                    except json.JSONDecodeError:
                        decode_error_count += 1
                        continue
                if decode_error_count > 0:
                    _logger.warning(f"Failed to decode {decode_error_count}"
                                    f" messages ({len(records)} messages "
                                    f"total)")
                return ret
        else:
            return fastf1._api.parse(raw, is_z)
    else:
        return None


from fastf1.logger import get_logger, soft_exceptions
from fastf1.req import Cache
from fastf1.utils import recursive_dict_get, to_timedelta, to_datetime

_logger = get_logger('api')

def make_path(wname, wdate, sname, sdate):
    """Create the api path base string to append on livetiming.formula1.com for api
    requests.

    The api path base string changes for every session only.

    Args:
        wname: Weekend name (e.g. 'Italian Grand Prix')
        wdate: Weekend date (e.g. '2019-09-08')
        sname: Session name 'Qualifying' or 'Race'
        sdate: Session date (formatted as wdate)

    Returns:
        relative url path
    """
    smooth_operator = f'{wdate[:4]}/{wdate} {wname}/{sdate} {sname}/'
    return '/static/' + smooth_operator.replace(' ', '_')



# define all empty columns for timing data
EMPTY_LAPS = {'Time': pd.NaT, 'Driver': str(), 'LapTime': pd.NaT,
              'NumberOfLaps': np.NaN, 'NumberOfPitStops': np.NaN,
              'PitOutTime': pd.NaT, 'PitInTime': pd.NaT,
              'Sector1Time': pd.NaT, 'Sector2Time': pd.NaT,
              'Sector3Time': pd.NaT, 'Sector1SessionTime': pd.NaT,
              'Sector2SessionTime': pd.NaT, 'Sector3SessionTime': pd.NaT,
              'SpeedI1': np.NaN, 'SpeedI2': np.NaN, 'SpeedFL': np.NaN,
              'SpeedST': np.NaN, 'IsPersonalBest': False}

EMPTY_STREAM = {'Time': pd.NaT, 'Driver': str(), 'Position': np.NaN,
                'GapToLeader': np.NaN, 'IntervalToPositionAhead': np.NaN}

@Cache.api_request_wrapper
def weather_data(path, response=None, livedata=None):
    """
    .. warning::
        :mod:`fastf1.api` will be considered private in future releases and
        potentially be removed or changed.

    Fetch and parse weather data.

    Weather data provides the following data channels per sample:

        - Time (datetime.timedelta): session timestamp (time only)
        - AirTemp (float): Air temperature [°C]
        - Humidity (float): Relative humidity [%]
        - Pressure (float): Air pressure [mbar]
        - Rainfall (bool): Shows if there is rainfall
        - TrackTemp (float): Track temperature [°C]
        - WindDirection (int): Wind direction [°] (0°-359°)
        - WindSpeed (float): Wind speed [m/s]

    Weather data is updated once per minute.

    Args:
        path (str): api path base string (usually ``Session.api_path``)
        response: Response as returned by :func:`fetch_page` can
            be passed if it was downloaded already.
        livedata: An instance of
            :class:`fastf1.livetiming.data.LiveTimingData`
            to use as a source instead of the api

    Returns:
        A dictionary containing one key for each data channel and a list
        of values per key.

    Raises:
        SessionNotAvailableError: in case the F1 live timing api
            returns no data
    """
    if livedata is not None and livedata.has('WeatherData'):
        # does not need any further processing
        _logger.info("Loading weather data")
        response = livedata.get('WeatherData')
    elif response is None:
        _logger.info("Fetching weather data...")
        response = fetch_page(path, 'weather_data')
        if response is None:  # no response received
            raise SessionNotAvailableError(
                "No data for this session! If this session only finished "
                "recently, please try again in a few minutes."
            )

    data = {
        'Time': [], 'AirTemp': [], 'Humidity': [], 'Pressure': [],
        'Rainfall': [], 'TrackTemp': [], 'WindDirection': [], 'WindSpeed': []
    }

    data_keys = ('AirTemp', 'Humidity', 'Pressure', 'Rainfall',
                 'TrackTemp', 'WindDirection', 'WindSpeed')
    converters = (float, float, float,
                  lambda v: True if v == '1' else False,  # rain: str -> bool
                  float, int, float)

    for entry in response:
        if len(entry) < 2:
            continue
        row = entry[1]
        if not isinstance(row, dict):
            continue

        data['Time'].append(to_timedelta(entry[0]))
        for key, conv in zip(data_keys, converters):
            try:
                data[key].append(conv(row[key]))
            except (KeyError, ValueError):
                # type conversion failed or key is missing
                data[key].append(conv(0))

    return data

class SessionNotAvailableError(Exception):
    """Raised if an api request returned no data for the requested session.
    A likely cause is that the session does not exist because it was cancelled."""

    def __init__(self, *args):
        super().__init__(*args)

# Function to insert data into PostgreSQL
def insert_weather_data(data):
    conn, cursor = db_connection()
    for i in range(len(data['Time'])):
        time = data['Time'][i]
        air_temp = data['AirTemp'][i]
        humidity = data['Humidity'][i]
        pressure = data['Pressure'][i]
        rainfall = data['Rainfall'][i]
        track_temp = data['TrackTemp'][i]
        wind_direction = data['WindDirection'][i]
        wind_speed = data['WindSpeed'][i]

        # Replace 'your_table' with the actual table name in your database
        insert_query = f"""
            INSERT INTO weather_data
            (time, air_temp, humidity, pressure, rainfall, track_temp, wind_direction, wind_speed)
            VALUES
            ('{time}', {air_temp}, {humidity}, {pressure}, {rainfall}, {track_temp}, {wind_direction}, {wind_speed});
        """

        cursor.execute(insert_query)
        conn.commit()


# Call the function to insert data into PostgreSQL
session = fastf1.get_session(2021, 'Monza', 'Q')
session.load()

weather_data_result = session.weather_data
insert_weather_data(weather_data_result)