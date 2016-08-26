import csv
from sanitizer import sanitize

# use config/data_files.yml
with open("tmp/HA_data.csv", newline="") as csv_file:
    for row in csv.DictReader(csv_file):
        print(sanitize(row))

