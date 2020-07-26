import glob
from pathlib import Path

CSVFiles = glob.glob("csvfiles/failed/*.csv")
print(f"total files: {len(CSVFiles)}")
print(CSVFiles)


for filein in CSVFiles:
    # use Path() so that it will work for both Windows and Mac
    filein = Path(filein.strip())

    print(f"processing {filein.name}")
    f = open(filein,'r')
    filedata = f.read()
    f.close()

    oldHeader=["Trip Duration","Start Time","Stop Time","Start Station ID","Start Station Name","Start Station Latitude","Start Station Longitude","End Station ID","End Station Name","End Station Latitude","End Station Longitude","Bike ID","User Type","Birth Year","Gender"]
    newHeader=["tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"]

    for i in range(len(oldHeader)):
        newdata = filedata.replace(oldHeader[i],newHeader[i])

    f = open(filein,'w')
    f.write(newdata)
    f.close()