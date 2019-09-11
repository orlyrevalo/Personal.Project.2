'''If Statements'''
# Simple If Statements
print("\nSimple If Statements")
age = 19
if age > 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# If-elif-else Chain
print("\nIf-elif-else Chain")
age = int(input("What is your age? "))
if age < 4:
    print("Your admission cost is $ 0")
elif age < 18:
    print("Your admission cost is $ 5")
else:
    print("Your admission cost is $ 10")

age = int(input("What is your age? "))
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $ "+ str(price))

# Using Multiple elif Blocks
print("\nUsing Multiple elif Blocks")
age = int(input("What is your age? "))
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $ "+ str(price))

# Testing Multiple Conditions
print('T\nesting Multiple Conditions')
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished making your pizza')
