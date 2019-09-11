'''If Statements: Try it Yourself 5-3 - 5-4'''
# 5.3 Alien Colors #1
alien_color = 'green'
if alien_color == 'green':
    print('You earn 5 points.')

# 5.4 Alien Colors #2
alien_color = 'green'
if alien_color == 'green':
    points = 5
else:
    points = 10
print("You earn " + str(points) + " points.")

# 5.5 Alien Colors #3
alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
print("You earn " + str(points) + " points.")

# 5.6 Stages of Life
age = 25
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'
print("You are a/an " + stage + ".")

# 5.7 Favorite Fruit
favorite_fruits = ['mango', 'jack fruit', 'banana', 'orange']
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
    