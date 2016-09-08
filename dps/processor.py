import csv
import glob
from dps import Session, config
from dps.sanitizer import sanitize
from dps.helpers import classify, extract_table_name

def start(directory=config["data_dir"], files=config["data_files"]):
    """Start DPS"""
    for file_name in glob.glob("{0}/{1}".format(directory, files)):
        table = extract_table_name(file_name, directory)

        module_name, class_name = config[table]["model"].split(".")
        source_class = classify(
            "dps.models.{0}".format(module_name),
            class_name)

        public_table = config[table]["public_table"]
        module_name, class_name = config[public_table]["model"].split(".")
        public_class = classify(
            "dps.models.{0}".format(module_name),
            class_name)

        with open(file_name, newline="") as csv_file:
            for row in csv.DictReader(csv_file):
                source_model = source_class(**sanitize(row))
                public_model = public_class(**source_model.transform_public())
                session = Session()
                session.add(source_model)
                session.add(public_model)
                session.commit()

