import pandas as pd
from db_conn import db_connection
import fastf1._api

def insert_car_data(data):
    conn, cursor = db_connection()
    for i in range(len(data['Date'])):
        date = data['Date'][i]
        rpm = data['RPM'][i]
        speed = data['Speed'][i]
        nGear = data['Gear'][i]
        throttle = data['Throttle'][i]
        brake = data['brake'][i]
        drs = data['DRS'][i]
        source = data['source'][i]

        insert_query = """
            INSERT INTO car_data
         (date, rpm, speed, nGear, throttle, brake, drs, source)
            VALUES
         (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        # Include session_id as a parameter in the execute method
        cursor.execute(insert_query, (date, rpm, speed, nGear, throttle, brake, drs, source))
        conn.commit()

API_paths = [
    ("654393aa3268db5850cd6f83",2020, "Austrian Grand Prix"),
    ("654393aa3268db5850cd6f84",2020, "Styrian Grand Prix"),
    ("654393aa3268db5850cd6f85",2020, "Hungarian Grand Prix"),
    ("654393aa3268db5850cd6f86",2020, "British Grand Prix"),
    ("654393aa3268db5850cd6f87",2020, "70th Anniversary Grand Prix"),
    ("654393aa3268db5850cd6f88",2020, "Spanish Grand Prix"),
    ("654393aa3268db5850cd6f89",2020, "Belgian Grand Prix"),
    ("654393aa3268db5850cd6f8a",2020, "Italian Grand Prix"),
    ("654393aa3268db5850cd6f8b",2020, "Tuscan Grand Prix"),
    ("654393aa3268db5850cd6f8c",2020, "Russian Grand Prix"),
    ("654393aa3268db5850cd6f8d",2020, "Eifel Grand Prix"),
    ("654393aa3268db5850cd6f8e",2020, "Portuguese Grand Prix"),
    ("654393aa3268db5850cd6f8f",2020, "Emilia Romagna Grand Prix"),
    ("654393aa3268db5850cd6f90",2020, "Turkish Grand Prix"),
    ("654393aa3268db5850cd6f91",2020, "Bahrain Grand Prix"),
    ("654393aa3268db5850cd6f92",2020, "Sakhir Grand Prix"),
    ("654393aa3268db5850cd6f93",2020, "Abu Dhabi Grand Prix"),
    ("654393aa3268db5850cd6f94",2021, "Emilia Romagna Grand Prix"),
    ("654393aa3268db5850cd6f95",2022, "Bahrain Grand Prix"),
    ("654393aa3268db5850cd6f96",2021, "Bahrain Grand Prix"),
    ("654393aa3268db5850cd6f97",2021, "Qatar Grand Prix"),
    ("654393aa3268db5850cd6f98",2021, "Portuguese Grand Prix"),
    ("654393aa3268db5850cd6f99",2021, "Spanish Grand Prix"),
    ("654393aa3268db5850cd6f9a",2021, "Monaco Grand Prix"),
    ("654393aa3268db5850cd6f9b",2021, "Azerbaijan Grand Prix"),
    ("654393aa3268db5850cd6f9c",2021, "Styrian Grand Prix"),
    ("654393aa3268db5850cd6f9d",2021, "French Grand Prix"),
    ("654393aa3268db5850cd6f9e",2021, "Austrian Grand Prix"),
    ("654393aa3268db5850cd6f9f",2021,  "British Grand Prix"),
    ("654393aa3268db5850cd6fa0",2021, "Hungarian Grand Prix"),
    ("654393aa3268db5850cd6fa1",2021, "Belgian Grand Prix"),
    ("654393aa3268db5850cd6fa2",2021, "Dutch Grand Prix"),
    ("654393aa3268db5850cd6fa3",2021, "Italian Grand Prix"),
    ("654393aa3268db5850cd6fa4",2021, "Russian Grand Prix"),
    ("654393aa3268db5850cd6fa5",2021, "Turkish Grand Prix"),
    ("654393aa3268db5850cd6fa6",2021, "United States Grand Prix"),
    ("654393aa3268db5850cd6fa7",2021, "Mexico City Grand Prix"),
    ("654393aa3268db5850cd6fa8",2021, "São Paulo Grand Prix"),
    ("654393aa3268db5850cd6fa9",2021, "Saudi Arabian Grand Prix"),
    ("654393aa3268db5850cd6faa",2021, "Abu Dhabi Grand Prix"),
    ("654393aa3268db5850cd6fab",2022, "Saudi Arabian Grand Prix"),
    ("654393aa3268db5850cd6fac",2022, "Australian Grand Prix"),
    ("654393aa3268db5850cd6fad",2022, "Emilia Romagna Grand Prix"),
    ("654393aa3268db5850cd6fae",2022, "Miami Grand Prix"),
    ("654393aa3268db5850cd6faf",2022, "Spanish Grand Prix"),
    ("654393aa3268db5850cd6fb0",2022, "Monaco Grand Prix"),
    ("654393aa3268db5850cd6fb1",2022, "Azerbaijan Grand Prix"),
    ("654393aa3268db5850cd6fb2",2022, "Canadian Grand Prix"),
    ("654393aa3268db5850cd6fb3",2022, "British Grand Prix"),
    ("654393aa3268db5850cd6fb4",2022, "Austrian Grand Prix"),
    ("654393aa3268db5850cd6fb5",2022, "French Grand Prix"),
    ("654393aa3268db5850cd6fb6",2022, "Hungarian Grand Prix"),
    ("654393aa3268db5850cd6fb7",2022, "Belgian Grand Prix"),
    ("654393aa3268db5850cd6fb8",2022, "Dutch Grand Prix"),
    ("654393aa3268db5850cd6fb9",2022, "Italian Grand Prix"),
    ("654393aa3268db5850cd6fba",2022, "Singapore Grand Prix"),
    ("654393aa3268db5850cd6fbb",2022, "Japanese Grand Prix"),
    ("654393aa3268db5850cd6fbc",2022, "United States Grand Prix"),
    ("654393aa3268db5850cd6fbd",2022, "Mexico City Grand Prix"),
    ("654393aa3268db5850cd6fbe",2022, "São Paulo Grand Prix"),
    ("654393aa3268db5850cd6fbf",2022, "Abu Dhabi Grand Prix"),
    ("654393aa3268db5850cd6fc0",2023, "Bahrain Grand Prix"),
    ("654393aa3268db5850cd6fc1",2023, "Saudi Arabian Grand Prix"),
    ("654393aa3268db5850cd6fc2",2023, "Australian Grand Prix"),
    ("654393aa3268db5850cd6fc3",2023, "Azerbaijan Grand Prix"),
    ("654393aa3268db5850cd6fc4",2023, "Miami Grand Prix"),
    ("654393aa3268db5850cd6fc5",2023, "Monaco Grand Prix"),
    ("654393aa3268db5850cd6fc6",2023, "Spanish Grand Prix"),
    ("654393aa3268db5850cd6fc7",2023, "Canadian Grand Prix"),
    ("654393aa3268db5850cd6fc8",2023, "Austrian Grand Prix"),
    ("654393aa3268db5850cd6fc9",2023, "British Grand Prix"),
    ("654393aa3268db5850cd6fca",2023, "Hungarian Grand Prix"),
    ("654393aa3268db5850cd6fcb",2023, "Belgian Grand Prix"),
    ("654393aa3268db5850cd6fcc",2023, "Dutch Grand Prix"),
    ("654393aa3268db5850cd6fcd",2023, "Italian Grand Prix"),
    ("654393aa3268db5850cd6fce",2023, "Singapore Grand Prix"),
    ("654393aa3268db5850cd6fcf",2023, "Japanese Grand Prix"),
    ("654393aa3268db5850cd6fd0",2023, "Qatar Grand Prix"),
    ("654393aa3268db5850cd6fd1",2023, "United States Grand Prix"),
    ("654393aa3268db5850cd6fd2",2023, "Mexico City Grand Prix"),
    ("654393aa3268db5850cd6fd3",2023, "São Paulo Grand Prix"),
    ("654393aa3268db5850cd6fd4",2023, "Las Vegas Grand Prix"),
    ("654393aa3268db5850cd6fd5",2023, "Abu Dhabi Grand Prix")
]

for record in API_paths:
    session_id, year, circuit_name = record
    try:
        session = fastf1.get_session(year, circuit_name, "R")
        session.load()
        pd.set_option('display.max_columns', 11)
        print(session.car_data)
        insert_car_data(session.car_data)  # Pass session_id to the function
    except Exception as e:
        print(f"Failed to obtain data for: {circuit_name} {year}: {str(e)}")

