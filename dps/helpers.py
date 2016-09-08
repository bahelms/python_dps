import re
import importlib
from dps import config

def classify(module_name: str, class_name: str):
    """Converts a string into a Class object"""
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def extract_table_name(file_path: str, directory: str):
    """Extracts table name from file path"""
    pattern = "{0}/(.+)\.csv".format(directory)
    return re.match(pattern, file_path).group(1)
