# Imports
import re
import bcrypt
import json
import os
from config import USER_DATA_FILE, MIN_PASSWORD_LENGTH


def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        content = file.read().strip()
        return json.loads(content) if content else {}


def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)


def is_username_available(nickname):
    users = load_users()
    return nickname not in users


def register_user(new_username, password):
    users = load_users()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users[new_username] = hashed_password
    save_users(users)


def is_valid_password(password):
    return (
        len(password) >= MIN_PASSWORD_LENGTH
        and re.search(r"[A-Z]", password)
        and re.search(r"\d", password)
    )


def check_credentials(nickname, password):
    users = load_users()
    if nickname in users:
        stored_hash = users[nickname]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            return True
    return False
