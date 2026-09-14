from functools import wraps
from utils.auth import get_current_user

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user:
            print("[!] Access Denied: You must be logged in to perform this action.")
            return None
        return func(*args, **kwargs)
    return wrapper

def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if not user or user.get("role") != "admin":
            print("[!] Access Denied: Admin permissions required.")
            return None
        return func(*args, **kwargs)
    return wrapper