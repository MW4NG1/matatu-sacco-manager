import json
import os

# Simulated session state
CURRENT_USER = None

def login_user(phone_number: str, users_file: str = "data/users.json") -> dict:
    global CURRENT_USER
    if not os.path.exists(users_file):
        return None

    try:
        with open(users_file, "r") as file:
            users = json.load(file)
            for user in users:
                if user.get("phone_number") == phone_number:
                    CURRENT_USER = user
                    return CURRENT_USER
    except (json.JSONDecodeError, IOError):
        return None

    return None

def logout_user():
    global CURRENT_USER
    CURRENT_USER = None

def get_current_user() -> dict:
    return CURRENT_USER