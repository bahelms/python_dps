import csv
import config
from sanitizer import sanitize

for path in config.file_paths:
    with open(path, newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            print(sanitize(row))

