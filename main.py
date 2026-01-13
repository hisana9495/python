import json
from datetime import datetime
from tripdata import create_trip
trips = [
    create_trip("New York", "15-05-2023", "Walked through Central Park"),
    create_trip("Sydney", "20-06-2023", "Saw the Opera House"),
    create_trip("Tokyo", "10-09-2023", "Enjoyed sushi and chSerry blossoms")
]
for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")
trips_json = json.dumps(trips, indent=4)
print(trips_json)