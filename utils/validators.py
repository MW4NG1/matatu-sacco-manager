import re

def is_non_empty(value: str) -> bool:
    """Check if input string is not empty or just whitespace."""
    return bool(value and value.strip())

def is_valid_phone(phone: str) -> bool:
    """Validate standard phone number format (e.g., 0712345678 or +254712345678)."""
    pattern = r"^(\+254|0)[71]\d{8}$"
    return bool(re.match(pattern, phone.strip()))

def is_positive_number(value) -> bool:
    """Check if value is a valid positive float/int."""
    try:
        val = float(value)
        return val > 0
    except (ValueError, TypeError):
        return False