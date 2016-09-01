from dps import config

def transform(source_data: dict, table: str) -> dict:
    """Maps keys and modifies values from source data to public"""

    fields = config[table]["fields"]
    return {fields[field]: value for field, value in source_data.items()}
