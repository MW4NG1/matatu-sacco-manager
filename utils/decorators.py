from functools import wraps
from utils.auth import get_current_user

def require_auth(func):
    """Decorator to ensure a user is logged in before executing a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user:
            print("[!] Access Denied: You must be logged in to perform this action.")
            return None
        return func(*args, **kwargs)
    return wrapper