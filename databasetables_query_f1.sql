CREATE TABLE circuits (
    _id varchar(255) PRIMARY KEY,
    circuit_id integer,
    circuit_ref VARCHAR(255),
    name varchar(255),
    location varchar(255),
    country VARCHAR(255),
    lat DECIMAL(9,6),
    lng DECIMAL(9,6),
    alt INTEGER,
    url VARCHAR(255)
);


CREATE TABLE constructor_results (
    _id varchar(255) PRIMARY KEY,
    constructorResultsId integer,
    raceId integer,
    constructorId integer,
    points float,
    status varchar(255)
);

create table constructor_standings (
    _id varchar(255)Primary key,
    constructorStandingsId integer,
    raceId integer,
    constructorId integer,
    points float,
    position integer,
    position_text varchar(255),
    wins integer
);



create table driver_standings (
    _id varchar(255) Primary key,
    driverStandingsId integer,
    raceId integer,
    driverId integer,
    points float,
    position integer,
    positionText varchar(255),
    wins integer
);


create table drivers (
    _id varchar(255) primary key,
    driverId integer,
    driverRef varchar(255),
    number varchar(255),
    code varchar(255),
    forename varchar(255),
    surname varchar(255),
    dob date,
    nationality varchar(255),
    url varchar(255)
);

create table lap_times (
    _id varchar(255) primary key,
    raceId integer,
    driverId integer,
    lap integer,
    position integer,
    time time,
    milliseconds integer
);

create table pit_stops(
    _id varchar(255) primary key,
    raceId integer,
    driverId integer,
    stop integer,
    lap integer,
    time time,
    duration varchar(255),
    milliseconds integer
);

create table qualifying(
    _id varchar(255) primary key,
    qualifyId integer,
    raceId integer,
    driverId integer,
    constructorId integer,
    number integer,
    position integer,
    q1 varchar(255),
    q2 varchar(255),
    q3 varchar(255)
);

create table races(
    _id varchar(255) PRIMARY KEY,
    raceId integer,
    year integer,
    round integer,
    circuitId integer,
    name VARCHAR(255),
    date DATE,
    time TIME NULL,
    url varchar(255)
);

CREATE TABLE results (
    _id varchar(255) PRIMARY KEY,
    resultId INTEGER,
    raceId INTEGER,
    driverId varchar(255),
    constructorId varchar(255),
    number varchar(255),
    grid varchar(255),
    position varchar(255),
    positionText VARCHAR(255),
    positionOrder varchar(255),
    points varchar(255),
    laps varchar(255),
    time varchar(255),
    milliseconds varchar(255) ,
    fastestLap varchar(255),
    rank varchar(255),
    fastestLapTime Varchar(255),
    fastestLapSpeed varchar(255),
    statusId varchar(255)
);

create table season_list(
    _id varchar(255) primary key,
    year integer,
    url varchar(255)
);

create table sprint_results (
    _id varchar(255) primary key,
    resultId integer,
    raceId integer,
    driverId integer,
    constructorId integer,
    number integer,
    grid integer,
    position integer,
    positionText varchar,
    positionOrder integer,
    points decimal,
    laps integer,
    time interval,
    milliseconds bigint null,
    fastestLap varchar(255),
    rank varchar(255),
    fastestLapTime time,
    fastestLapSpeed decimal,
    statusId varchar(255)
);

create table status(
    _id varchar(255) primary key,
    statusId integer,
    status varchar(255)
);