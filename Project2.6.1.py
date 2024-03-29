''''Dictionaries'''
# Simple Dictionary
print("Simple Dictionary")
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
print("\nStarting with an Empty Dictionary")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

# Modifying Values in a Dictionary
print("\nModifying Values in a Dictionary")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

''' 
=====================================================================
Move the alien to the right
Determine how far to move the line based on its current speed. 
=====================================================================
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

