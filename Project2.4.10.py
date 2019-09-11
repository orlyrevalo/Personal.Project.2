'''Working with Part of a List'''
# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # Start at index position 0 and end at 2
print(players[1:4])  # Start at index position 1 and end at 3
print(players[:4])  # Start at index position 0 and end at 3
print(players[2:])  # Start at index position 2 and end at the last element
print(players[-3:])  # Start at index position -3 and end at the last element

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)



