def sanitize(record: dict) -> dict:
    """Returns a new dict with values sanitized"""
    return {k.lower(): _sanitize(v) for k, v in record.items()}

def nullify(value: str) -> str or None:
    """Converts empty strings to None"""
    return None if value == "" else value

def _sanitize(value: str) -> str or None:
    """Strips surrounding whitespace and converts empty strings to None"""
    return nullify(value.strip())
