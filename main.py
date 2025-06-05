# Project Manager Self Care

# Imports
from auth import register_user, is_username_available, is_valid_password, check_credentials
from config import COLOR_GREEN, COLOR_RED, COLOR_RESET

# Coloring
print(f"{COLOR_GREEN}Login successful!{COLOR_RESET}")

def login():
    nickname = input("Username: ")
    password = input("Password: ")
    if check_credentials(nickname, password):
        print(f'{COLOR_GREEN}Login successful!{COLOR_RESET}')
    else:
        print(f'{COLOR_RED}Incorrect username or password!{COLOR_RESET}')

def register():
    while True:
        new_nickname = input("Your username: ")
        if is_username_available(new_nickname):
            break
        else:
            print(f'{COLOR_RED}Sorry, the username "{new_nickname}" is already taken. Please choose a different one.{COLOR_RESET}')

    while True:
        new_password = input("Your password: ")
        if is_valid_password(new_password):
            register_user(new_nickname, new_password)
            print(f'{COLOR_GREEN}Registration successful! Now you can log in.{COLOR_RESET}')
            login()
            break
        else:
            print(f'{COLOR_RED}Password must be at least 8 characters long, contain at least one uppercase letter, and include at least one number.{COLOR_RESET}')

# Main program
print(f'Welcome to our project manager self care\nIt\'s nice to see you!\n')
choice = input(f'Do you wanna \033[1m{COLOR_GREEN}"Login"\033[0m or \033[33m"Register"{COLOR_RESET}\n').lower()

if choice in ["login", "log in"]:
    login()
elif choice == "register":
    register()
else:
    print(f'{COLOR_RED}Syntax error. Please choose \033[1m{COLOR_GREEN}"Login"\033[0m or \033[33m"Register"{COLOR_RESET}')