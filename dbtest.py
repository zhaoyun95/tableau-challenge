# simple database test with timing
from sqlalchemy import create_engine
import time

start = time.time()
db_uri = f'postgresql://postgres:postgres@localhost:5432/citibike_db'
engine = create_engine(db_uri)

result = engine.execute("select count(id) as totalRows from tripdata")
for record in result:
    print(record)
end = time.time()
duration = end - start
print(f"duration: {duration} seconds")