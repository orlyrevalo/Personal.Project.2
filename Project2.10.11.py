"""Files and Exception"""
# Saving and Reading User-Generated Data
import json
print("\nSaving and Reading User-Generated Data ")

username = input("What is your name")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back " + username + "!")

import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username)


