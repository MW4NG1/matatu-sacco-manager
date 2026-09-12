import json
import os

# Simulated session state
CURRENT_USER = None

def login_user(phone_number: str, users_file: str = "data/users.json") -> dict:
    """Authenticate a user by phone number and set active session."""
    global CURRENT_USER
    if not os.path.exists(users_file):
        return None