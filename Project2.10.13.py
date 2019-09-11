"""Try it Yourself 10-11 - 10-13"""
# 10-11 Favorite Number
print("10-11 Favorite Number")

import json


def favorite_number():
    """Asks for the user's favorite number"""
    filename = 'favorite_number.json'
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)


def call_favorite_number():
    """Recalls the user's favorite number"""
    filename = 'favorite_number.json'
    with open(filename) as f_obj:
        number = json.load(f_obj)
    print("I know your favorite number! It's " + number + "!")


favorite_number()
call_favorite_number()

# 10-12 Favorite Number
print("\n10-12 Favorite Number Remembered")


def favorite_number1():
    """Asks for the user's favorite number"""
    number = call_favorite_number1()
    print("I know your favorite number! It's " + number + "!")


def call_favorite_number1():
    """Recalls the user's favorite number"""
    filename = 'favorite_number1.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        number = store_favorite_number1()
    print("Is this your favorite number? " + number)
    while True:
        prompt = input("'y' or 'n'? ")
        if prompt == 'y':
            return number
        elif prompt == 'n':
            number = store_favorite_number1()
            return number
        else:
            print("That's not a valid answer!")


def store_favorite_number1():
    """Stores the favorite number of a user"""
    filename = 'favorite_number1.json'
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number


favorite_number1()

# 10-13 Verify User
print("\nVerify User")


def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = get_new_username()
        return username
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    while True:
        prompt = input("Is this your username? " + username.title() + " 'y' or 'n'? ")
        if prompt == 'y':
            break
        elif prompt == 'n':
            username = get_new_username()
            break
        else:
            print("That is not a valid response!")
    if username and prompt == 'y':
        print("Welcome back, " + username.title() + "!")
    else:
        print("We'll remember you when you come back, " + username.title() + "!")


greet_user()
