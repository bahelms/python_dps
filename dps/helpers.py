import re
from dps import config

def classify(string):
    """Converts a string into a Class object"""
    print(globals().keys())
    return globals()[string]

def extract_table_name(file_path_str, directory):
    """Extracts table name from file path"""
    pattern = "{0}/(.+)\.csv".format(directory)
    return re.match(pattern, file_path_str).group(1)
