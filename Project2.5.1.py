'''If Statements'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality
print("\nChecking for Inequality")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Checking Multiple Conditions
print("\nChecking Multiple Conditions")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

# Checking Whether a Value is in a List
print("\nChecking Whether a Value is in a List")
requested_topping = ['mushrooms', ' onions', 'pineapple']
print('mushrooms'in requested_topping)
print('pepperoni'in requested_topping)

# Checking Whether a Value is not in a List
print("\nChecking Whether a Value is not in a List")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Boolean Expressions
print('\nBoolean Expressions')
game_active = True
can_edit = False 

# done