import csv

def sanitize(record):
    return record

with open("tmp/HA_data.csv", newline="") as csv_file:
    for row in csv.DictReader(csv_file):
        print(sanitize(row))

