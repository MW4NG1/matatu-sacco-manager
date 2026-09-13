import re

def is_non_empty(value: str) -> bool:
    
    return bool(value and value.strip())

def is_valid_phone(phone: str) -> bool:
    
    pattern = r"^(\+254|0)[71]\d{8}$"
    return bool(re.match(pattern, phone.strip()))

def is_positive_number(value) -> bool:
    
    try:
        val = float(value)
        return val > 0
    except (ValueError, TypeError):
        return False