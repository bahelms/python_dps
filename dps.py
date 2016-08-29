import csv
import glob
from sanitizer import sanitize

"""Start DPS"""
for file_name in glob.glob("data/*.csv"):
    with open(file_name, newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            sanitize(row)

