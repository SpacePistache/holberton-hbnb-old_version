import json
import os

DATA_FILE = "storage.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "places": [], "reviews": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_user(user):
    data = load_data()
    data["users"].append(user)
    save_data(data)

def get_users():
    return load_data()["users"]
