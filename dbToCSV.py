# read from database and save results to csv file using pandas
from sqlalchemy import create_engine
import time
import pandas as pd

db_uri = f'postgresql://postgres:postgres@localhost:5432/citibike_db'
print(db_uri)
engine = create_engine(db_uri)

start = time.time()
sql = "select * from tripdata where 'startTime' > '2017-01-01'"
outFile = "tripdataSince2017.csv"

count = 1
for chunk in pd.read_sql(sql , con=engine, chunksize=100):
    print(f"chunk #{count}")
    chunk.to_csv(outFile, mode='a',sep=',',encoding='utf-8')

end = time.time()
print(f"Time spent: {end - start} seconds")
