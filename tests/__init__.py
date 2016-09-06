import csv
import os
import glob
from dps import config

def create_test_data(entity):
    fields = config[entity]["fields"].keys()
    row_values = [["{0} value{1}".format(field, num) for field in fields]
                    for num in range(0, 5)]
    rows = list(map(lambda row: dict(zip(fields, row)), row_values))

    with open("data/{0}_test.csv".format(entity), "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def remove_test_data():
    for file_name in glob.glob("data/*_test.csv"):
        os.remove(file_name)
