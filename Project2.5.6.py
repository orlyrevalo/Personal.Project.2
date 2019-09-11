'''If Statements: Try it Yourself 5-8 - 5-11'''
# 5-8 Hello Admin
user_names = ['Ash', 'Rik', 'Price', 'Jasmine', 'Orly', 'Admin']
for user_name in user_names:
    if user_name == 'Admin':
        print("Hello admin, would you like to see a status report.")
    else:
        print("Hello " + user_name + ", thank you for logging in again.")

# 5-9 No Users
user_names = ['slfsd']
if user_names:
    for user_name in user_names:
        print("Hello " + user_name + ", thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10 Checking User Names
current_users = ['Ash', 'Rik', 'Price', 'Jasmine', 'Orly', 'Admin']
new_users = ['Orly', 'Rik', 'Harry', 'Hermoine', 'Ron', 'ORLY', 'OrLY']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ": This username is not available. Please use another username")
    elif new_user.title() in current_users:
        print(new_user + ": This username is not available. Please use another username")
    elif new_user.upper() in current_users:
        print(new_user + ": This username is not available. Please use another username")
    else:
        print(new_user + ": This username is available.")

# the elif statements can be connected by an or conjunction
current_users = ['Ash', 'Rik', 'Price', 'Jasmine', 'Orly', 'Admin']
new_users = ['Orly', 'Rik', 'Harry', 'Hermoine', 'Ron', 'ORLY', 'OrLY']
for new_user in new_users:
    if new_user.lower() in current_users or new_user.title() in current_users or new_user.upper() in current_users:
        print(new_user + ": This username is not available. Please use another username")
    else:
       print(new_user + ": This username is available.")

current_users = ['Ash', 'Rik', 'Price', 'Jasmine', 'Orly', 'Admin']
lowercase_current_users = [x.lower() for x in current_users] #list comprehension
print(lowercase_current_users)

# 5-11 Ordinal Numbers
ordinal_numbers = [x for x in range(1, 10)]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print('1st')
    elif ordinal_number == 2:
        print('2nd')
    elif ordinal_number == 3:
        print('3rd')
    else:
        print(str(ordinal_number) + "th")