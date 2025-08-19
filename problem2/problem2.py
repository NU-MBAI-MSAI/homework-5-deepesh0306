def date_format(date_str: str):
    """Converts a date from MM/DD/YYYY format to YYYY-MM-DD format."""
    
    month, day, year = date_str.split('/')
    # Formatting as YYYY-MM-DD to return as required
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
