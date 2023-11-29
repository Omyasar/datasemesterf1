from pymongo import MongoClient
from db_conn import db_connection

# Connectie naar mongodb en datacollectie
# Wijzig indien nodig je database naam (Deze naam hebben we onderling besproken voor mongodb)
mongodb = MongoClient()
mongo_db = mongodb['f1_dataset']

# Dit is om de data op te halen voor de collecties
mongo_circuits = mongo_db['circuits']
mongo_constructor_results = mongo_db['constructor_results']
mongo_constructor_standings = mongo_db['constructor_standings']
mongo_driver_standings = mongo_db['driver_standings']
mongo_drivers = mongo_db['drivers']
mongo_lap_times = mongo_db['lap_times']
mongo_pit_stops = mongo_db['pit_stops']
mongo_qualifying = mongo_db['qualifying']
mongo_races = mongo_db['races']
mongo_results = mongo_db['results']
mongo_status = mongo_db['status']
mongo_sprint_results = mongo_db['sprint_results']
mongo_season_list = mongo_db['season_list']


def migrate_constructorresults():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_constructor_results.find():
        transformed_data.append((
            data['_id'],
            data['constructorResultsId'],
            data['raceId'],
            data['constructorId'],
            data['points'] if data['points'] != '\\N' else None,
            data['status'] if data['status'] != '\\N' else None
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO constructor_results (
                _id, constructoRresultsId, raceid, constructorid, points, status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()


def migrate_constructorstands():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_constructor_standings.find():
        transformed_data.append((
            data['_id'],
            data['constructorStandingsId'],
            data['raceId'],
            data['constructorId'],
            data['points'] if data['points'] != '\\N' else None,
            data['position'],
            data['positionText'],
            data['wins'] if data['wins'] != '\\N' else None
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO constructor_standings (
                _id, constructorStandingsid, raceid, constructorid, points,position, position_text, wins
            )
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()


# Transformeert en laad de driverstandings data naar postgres
def migrate_driverstandings_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_driver_standings.find():
        transformed_data.append((
            data['_id'],
            data['driverStandingsId'],
            data['raceId'],
            data['driverId'],
            data['points'] if data['points'] != '\\N' else None,
            data['position'],
            data['positionText'],
            data['wins'] if data['wins'] != '\\N' else None
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO driver_standings (
                _id, driverStandingsId, raceid, driverid, points,position, positiontext, wins
            )
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
            ON CONFLICT (_id)
            DO UPDATE SET
                driverStandingsId = EXCLUDED.driverStandingsId,
                raceid = EXCLUDED.raceid,
                driverid = EXCLUDED.driverid,
                points = EXCLUDED.points,
                position = EXCLUDED.position,
                positiontext = EXCLUDED.positiontext,
                wins = EXCLUDED.wins;
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def migrate_circuits_data():
    conn, cursor = db_connection()

    # Transformeer de data
    transformed_data = []
    for data in mongo_circuits.find():
        transformed_data.append((
            data['_id'],
            data['circuitId'],
            data['circuitRef'],
            data['name'],
            data['location'],
            data['country'],
            data['lat'],
            data['lng'],
            data['alt'] if data['alt'] != '\\N' else None,
            data['url']
        ))

    # Laad de data in PostgreSQL
    try:
        cursor.executemany(
            """
            INSERT INTO circuits (
                _id, circuit_id, circuit_ref, name, location, country,
                lat, lng, alt, url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()


# Transformeert en laad de drivers data naar postgres
def migrate_drivers_data():
    conn, cursor = db_connection()

    # Transformeer de data
    transformed_data = []
    for data in mongo_drivers.find():
        transformed_data.append((
            data['_id'],
            data['driverId'],
            data['driverRef'],
            data['number'],
            data['code'],
            data['forename'],
            data['surname'],
            data['dob'],
            data['nationality'],
            data['url']
        ))

    # Laad de data in PostgreSQL
    try:
        cursor.executemany(
            """
            INSERT INTO drivers (
                _id, driverid, driverref, number, code, forename,
                surname, dob, nationality, url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.cursor()


# Transformeert en laad de lap times data naar postgres
def lap_times_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_lap_times.find():
        transformed_data.append((
            data['_id'],
            data['raceId'],
            data['driverId'],
            data['lap'],
            data['position'],
            data['time'],
            data['milliseconds'],
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO lap_times (
                _id, raceid, driverid, lap, position, time, milliseconds
            )
            VALUES (%s, %s, %s, %s, %s, %s,%s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# transformeert en laad de lap times data naar postgres
def pit_stops_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_pit_stops.find():
        transformed_data.append((
            data['_id'],
            data['raceId'],
            data['driverId'],
            data['stop'],
            data['lap'],
            data['time'],
            data['duration'],
            data['milliseconds'],
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO pit_stops (
                _id, raceid, driverid, stop, lap, time,duration, milliseconds
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# Transformeert en laad de qualifying data naar postgres
def qualifying_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_qualifying.find():
        transformed_data.append((
            data['_id'],
            data['qualifyId'],
            data['raceId'],
            data['driverId'],
            data['constructorId'],
            data['number'],
            data['position'],
            data.get('q1', None),
            data.get('q2', None),
            data.get('q3', None)
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO qualifying (
                _id, qualifyid, raceid, driverid, constructorId, number,position, q1, q2, q3
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# Transformeert en laad de races data
def races_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_races.find():
        transformed_data.append((
            data['_id'],
            data['raceId'],
            data['year'],
            data['round'],
            data['circuitId'],
            data['name'],
            data['date'],
            data['time'] if data['time'] != '\\N' else None,
            data['url']
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO races (
                _id, raceId, year, round, circuitId, name, date, time, url
            )
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()


# Transformeert en laad de results data
def sprint_results():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_results.find():
        transformed_data.append((
            data['_id'],
            data.get('resultId', None),
            data['raceId'],
            data.get('driverId'),
            data.get('constructorId', None),
            data.get('number', None),
            data.get('grid', None),
            data.get('position', None),
            data.get('positionText'),
            data.get('positionOrder'),
            data.get('points', None),
            data.get('laps', None),
            data.get('time', None),
            data.get('milliseconds', None),
            data.get('fastestLap'),
            data.get('fastestLapTime'),
            data.get('statusId'),
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO sprint_results (
                _id, resultId, raceId,driverid, constructorId, number, grid, position,positiontext,positionOrder, points,laps, time,milliseconds,
                fastestlap, fastestLapTime,statusId

            )
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()

def results():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_results.find():
        transformed_data.append((
            data['_id'],
            data.get('resultId', None),
            data['raceId'],
            data.get('driverId'),
            data.get('constructorId', None),
            data.get('number', None),
            data.get('grid', None),
            data.get('position', None) if data.get('position', None) != '\\N' else None,
            data.get('positionText'),
            data.get('points', None),
            data.get('time', None) if data.get('time', None) != '\\N' else None,
            data.get('milliseconds', None) if data.get('milliseconds', None) != '\\N' else None,
            data.get('fastestLap') if data.get('fastestLap', None) != '\\N' else None,
            data.get('rank') if data.get('rank', None) != '\\N' else None,
            data.get('fastestLapTime') if data.get('fastestLapTime', None) != '\\N' else None,
            data.get('fastestLapSpeed') if data.get('FastestLapSpeed', None) != '\\N' else None,
            data.get('statusId') if data.get('statusId', None) != '\\N' else None
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO results (
                _id, resultId, raceId,driverid, constructorId, number, grid, position,positiontext, points, time,milliseconds,
                fastestlap, rank, fastestLapTime,FastestLapSpeed,statusId

            )
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()
def status_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_status.find():
        transformed_data.append((
            data['_id'],
            data['statusId'],
            data['status'],
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO status (
                _id, statusId, status
            )
            VALUES (%s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()

def season_data():
    conn, cursor = db_connection()

    # Tranformeer de data
    transformed_data = []
    for data in mongo_season_list.find():
        transformed_data.append((
            data['_id'],
            data['year'],
            data['url'],
        ))
    try:
        cursor.executemany(
            """
            INSERT INTO season_list (
                _id, year, url
            )
            VALUES (%s, %s, %s)
            """,
            transformed_data
        )
        conn.commit()
    except Exception as e:
        print(f"Data migratie fout: {e}")
        conn.rollback()


if __name__ == "__main__":
    season_data()
    status_data()
    results()
    races_data()
    qualifying_data()
    pit_stops_data()
    lap_times_data()
    migrate_drivers_data()
    migrate_circuits_data()
    migrate_driverstandings_data()
    migrate_constructorstands()
    migrate_constructorresults()
