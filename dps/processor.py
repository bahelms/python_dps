import csv
import glob
from dps import Session, config
from dps.sanitizer import sanitize
from dps.helpers import classify, extract_table_name

def start(directory=config["data_dir"], files=config["data_files"]):
    """Start DPS"""
    for file_name in glob.glob("{0}/{1}".format(directory, files)):
        table = extract_table_name(file_name, directory)
        source_class = classify(config[table]["model"])
        public_class = classify(config[table]["public_table"]["model"])

        with open(file_name, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                source_model = source_class(sanitize(row))
                print(source_model.sacode)
                # public_model
                session = Session()

