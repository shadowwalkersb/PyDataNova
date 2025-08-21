def validate_payload(required_fields: list, payload: dict):
    """
    Ensure all required fields exist in the payload.
    Raises ValueError if missing.
    """
    missing = [f for f in required_fields if f not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    return True
