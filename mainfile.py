import json
from datetime import datetime
from tracker import create_record
records = [
    create_record("Paris", "Loved the Eiffel Tower!", "05-06-2022"),
    create_record("Tokyo", "Amazing sushi experience.", "12-09-2023"),
    create_record("New York", "Times Square was dazzling.", "25-12-2024")
]
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")
json_string = json.dumps(records, indent=4)
print("JSON Output:\n", json_string)
parsed_records = json.loads(json_string)
print("\nParsed Records:")
for rec in parsed_records:
    print(rec)