import hashlib
from utils.storage import load_json, save_json

_current_user = None

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(phone: str, password: str):
    global _current_user
    users = load_json("data/users.json")
    hashed_pwd = hash_password(password)
    
    for user in users:
        if user.get("phone") == phone and user.get("password_hash") == hashed_pwd:
            _current_user = user
            return user
    return None

def logout_user():
    global _current_user
    _current_user = None

def get_current_user():
    global _current_user
    return _current_user

def register_user(phone, name, password, role="operator"):

    users = load_json("data/users.json")
    
    for user in users:
        if user.get("phone") == phone:
            print("[!] Error: Phone number already registered.")
            return False
            
    new_user = {
        "name": name,
        "phone": phone,
        "password_hash": hash_password(password),
        "role": role  # 'admin' or 'operator'
    }
    
    users.append(new_user)
    save_json("data/users.json", users)
    print(f"[+] Success: User {name} registered successfully!")
    return True