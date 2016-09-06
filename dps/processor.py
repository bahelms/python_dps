import csv
import glob
from dps import Session, config
from dps.sanitizer import sanitize

def start(directory=config["data_dir"], files=config["data_files"]):
    """Start DPS"""
    for file_name in glob.glob("{0}/{1}".format(directory, files)):
        source_class = classify(config[file_name]["model"])
        public_class = classify(config[file_name]["public_table"]["model"])

        with open(file_name, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                source_model = source_class(sanitize(row))
                # public_model
                session = Session()

