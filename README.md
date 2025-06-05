# 📩 User Authentication Project

Just a small command-line Python application for user registration and login with password hashing using bcrypt.  
User data is stored securely in a JSON file. 

---

## Features

- User registration with:
  - Unique usernames
  - Password validation (minimum 8 characters, at least one uppercase letter and one number)
  - Password hashing with bcrypt for security

- User login with password verification

- Stores user credentials in a local JSON file (`usernames.json`)

- Colored terminal output for clear success/error messages

---

## Getting Started

### Prerequisites

- Python 3.x
- Install required packages:

```bash
pip install -r requirements.txt
Run the main script: python main.py
Follow the prompts to either Login or Register.
```

---
#Project Structure

| File               | Description |
|--------------------|-------------|
| `main.py`          | Main application logic and user interaction|
| `auth.py`          | Authentication functions (login, register, password checks)|
| `config.py`        | Configuration constants like file paths|
| `requirements.txt ` | Python dependencies |
| `usernames.json `  | User data storage (auto-created on first registration) |
| `.gitignore`       | Specifies files/folders to ignore in git |
| `README.md`        | This file |

---
# Configuration
User data file location and password rules are set in config.py
You can adjust password complexity requirements in the code if needed.

---
# Notes
Make sure .gitignore includes .idea/, .DS_Store, and any virtual environment folders to keep your repo clean.
Passwords are securely hashed using bcrypt — plaintext passwords are never stored.

---
# License
This project is open source and free to use.

---
# Additional comment
I would love to receive more ideas for my code. Ready to learn 👨🏻‍💻
