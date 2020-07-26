oldHeader=("Trip Duration" "Start Time" "Stop Time" "Start Station ID" "Start Station Name" "Start Station Latitude" "Start Station Longitude" "End Station ID" "End Station Name" "End Station Latitude" "End Station Longitude" "Bike ID" "User Type" "Birth Year" "Gender")
newHeader=("tripduration" "starttime" "stoptime" "start station id" "start station name" "start station latitude" "start station longitude" "end station id" "end station name" "end station latitude" "end station longitude" "bikeid" "usertype" "birth year" "gender")

for files in "csvfiles/failed/*.csv"
do
	for i in "${!oldHeader[@]}"; do
		#echo $files
		echo "${oldHeader[$i]} ${newHeader[$i]}"
		sed -i "s/${oldHeader[$i]}/${newHeader[$i]}/g" $files
	done
done