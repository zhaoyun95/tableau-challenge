# ask before continueing
goahead = input("Warning!!! \nThis program will drop all data from database, \nType 'Y/y' to continue, 'N/n to quit: ")
if goahead.upper() != 'Y':
    exit()

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime


Base = declarative_base()

# Create class to match the database table
# ----------------------------------
class Tripdata(Base):
    __tablename__ = 'tripdata'

    id = Column(Integer, primary_key=True)
    tripDuration = Column(Integer)
    startTime = Column(DateTime)
    stopTime = Column(DateTime)
    startStationId = Column(Integer)
    startStationName = Column(String)
    startStationLat = Column(Float)
    startStationLon = Column(Float)
    endStationId = Column(Integer)
    endStationName = Column(String)
    endStationLat = Column(Float)
    endStationLon = Column(Float)
    bikeId = Column(Integer)
    userType = Column(String)
    birthYear = Column(Integer)
    gender = Column(Integer)

    def __repr__(self):
        return id

db_uri = f'postgresql://postgres:postgres@localhost:5432/citibike_db'
engine = create_engine(db_uri)
# connection = engine.connect()

# Add Records to the Appropriate DB
# ----------------------------------
session = Session(bind=engine)

# drop table tripdata if exists, careful
# try:
#     session.execute("DROP TABLE tripdata")
#     session.commit()  # must call commit to drop table!
# except Exception as e:
#     print(e)

# drop_all() doesn't work! save this for future reference!
# this one will cause execution hangup, and lock postgres database
# I will need to exit VSCode to reset it.
# use session.execute("DROP TABLE tripdata"); and session.commit(); instead
# ----------------------------------
#Base.metadata.drop_all(engine)

# Create the table(s)
# ----------------------------------
Base.metadata.create_all(engine)

def db_test():
    tripdata = Tripdata(
        tripDuration = 505,
        startTime = '6/2/2020 12:24:38',
        stopTime = '6/2/2020 12:33:03',
        startStationId = 3244,
        startStationName = 'Douglass St & 4 Ave',
        startStationLat = 40.6792788,
        startStationLon = -73.98154004,
        endStationId = 3419,
        endStationName = 'Douglass St & 4 Ave',
        endStationLat = 40.6792788,
        endStationLon = -73.98154004,
        bikeId = 39852,
        userType = 'Customer',
        birthYear = 1997,
        gender = 2
        )

    # add one row for testing
    session.add(tripdata)
    session.commit()
    session.close()  # good to close session after we are done

    # Query the Tables
    # ----------------------------------
    tripdata_list = session.query(Tripdata).all()
    for tripdata in tripdata_list:
        print(type(tripdata))
        print(tripdata.id, tripdata.tripDuration)
        # for key in tripdata:
        #     print(f"{key}: {tripdata[key]}")


# run a simple db test
# db_test()
