import re

def classify(string):
    """Converts a string into a Class object"""
    return globals()[string]

