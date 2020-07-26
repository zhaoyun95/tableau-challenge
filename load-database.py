# ask before continueing
goahead = input("Warning!!! \nThis program will drop all data from database, \nType 'Y/y' to continue, 'N/n to quit: ")
if goahead.upper() != 'Y':
    exit()

# Python SQL toolkit and Object Relational Mapper
import pandas as pd
import psycopg2
import glob
from pathlib import Path
from sqlalchemy import create_engine
import time

db_uri = f'postgresql://postgres:postgres@localhost:5432/citibike_db'
engine = create_engine(db_uri)


# ----------------- load tripdata csv files ---------------------

# CSVFiles2019 = glob.glob("csvfiles/2019*.csv")
# CSVFiles2020 = glob.glob("csvfiles/2020*.csv")
# CSFFiles = CSVFiles2019 + CSVFiles2020
# CSVFiles = glob.glob("csvfiles/2020*.csv")
# CSVFiles = glob.glob("csvfiles/202006.csv")
CSVFiles = glob.glob("csvfiles/failed/*.csv")
print(f"total files: {len(CSVFiles)}")
print(CSVFiles)

# start time before loading csv files
tstart = time.time()
# loop through all data/*.csv files and load them into price table
for file in CSVFiles:
    # use Path() so that it will work for both Windows and Mac
    file = Path(file.strip())

    # print(file)
    trip_df = pd.read_csv(file)

    # rename column heading to match database table columns
    trip_df.rename(columns = {
        "tripduration":"tripDuration",
        "starttime":"startTime",
        "stoptime":"stopTime",
        "start station id":"startStationId",
        "start station name":"startStationName",
        "start station latitude":"startStationLat",
        "start station longitude":"startStationLon",
        "end station id":"endStationId",
        "end station name":"endStationName",
        "end station latitude":"endStationLat",
        "end station longitude":"endStationLon",
        "bikeid":"bikeId",
        "usertype":"userType",
        "birth year":"birthYear",
        "gender":"gender"
        }, inplace=True)
    
    
    # load dataframe into database
    try:
        print(f"loading {file.name}")
        start = time.time()
        trip_df.to_sql(name='tripdata', con=engine, if_exists='append', index=False)
        end = time.time()
        duration = end - start
        print(f"{duration} seconds")
    except Exception as e:
        print(f"failed>>>>>>>>> {file.name} <<<<<<<<<<<<<")
        print(e)

# print timing
tend = time.time()
tduration = tend - tstart
print(f"total {tduration} seconds")


# trip_df2 = pd.read_sql("select * from tripdata", con=engine)
# print("tripdata table after loading:")
# print("column, count")
# print(trip_df2.count())

# check database after loading
start2 = time.time()
result = engine.execute("select count(id) as totalRows from tripdata")
for record in result:
    print(record)
end2 = time.time()
duration2 = end2 - start2
print(f"duration: {duration2} seconds")


