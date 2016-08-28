import csv
import config
import setup
from sanitizer import sanitize

"""Start DPS"""
for path in config.file_paths:
    with open(path, newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            sanitize(row)

