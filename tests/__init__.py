import csv
import os
import glob
import shutil
from dps import config

test_data_dir = "test_data"

def create_test_data(entity):
    fields = config[entity]["fields"].keys()
    row_values = [["{0}{1}".format(field, num) for field in fields]
                    for num in range(0, 5)]
    rows = list(map(lambda row: dict(zip(fields, row)), row_values))
    csv_file = "{0}/{1}.csv".format(test_data_dir, entity)

    if not os.path.isdir(test_data_dir):
        os.mkdir(test_data_dir)

    with open(csv_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def remove_test_data():
    shutil.rmtree(test_data_dir)
