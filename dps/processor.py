import csv
import glob
from dps.sanitizer import sanitize

def start():
    """Start DPS"""
    for file_name in glob.glob("data/*.csv"):
        with open(file_name, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                print(sanitize(row))
                # save to source
                # transform
                # save to public

