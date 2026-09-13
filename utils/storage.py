import json
import os

def load_json(file_path: str) -> list:
    
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_json(file_path: str, data: list) -> bool:
    
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        return False