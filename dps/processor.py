import csv
import glob
from dps import Session
from dps.sanitizer import sanitize

def start():
    """Start DPS"""
    for file_name in glob.glob("data/*.csv"):
        with open(file_name, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                source_data = sanitize(row)
                # public_data = transform(source_data)
                # save to source
                # save to public

