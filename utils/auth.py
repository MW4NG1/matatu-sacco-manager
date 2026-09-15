import hashlib
from utils.storage import load_json

# Keep track of the currently logged-in user session globally
_current_user = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(phone, password):
    global _current_user
    users = load_json("data/users.json")
    
    input_hash = hash_password(password)
    
    for user in users:
        if user.get("phone") == phone and user.get("password_hash") == input_hash:
            _current_user = user
            return user
            
    return None

def logout_user():
    global _current_user
    _current_user = None

def get_current_user():
    global _current_user
    return _current_user