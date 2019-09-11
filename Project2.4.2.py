'''Lists'''
friends = ['jasmine', 'rik', 'price', 'Ash']

for friend in friends:
    print("Hi " + friend.title() + "\nPlease come to my Party\n")

transportation_mode = ['box', 'copter', 'rail', 'tomato']

print("I would like to ride a ")
for mode in transportation_mode:
    print(mode)
print("\n")

'''Appending Elements to the End of a List'''
print("Appending Elements to the End of a List")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print("\n")

'''Inserting Elements into a list'''
print("Inserting Elements into a list")
motorcycles = ['honda', 'yamaha', 'suzuki'""]
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("\n")

'''Removing Elements from a List'''
print("Removing Elements from a List")
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
print("\n")

'''Removing an Item Using the pop'''
print("Removing an Item Using the pop")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)
print("\n")

'''Popping Items from any Position in a list'''
print('Popping Items from any Position in a list')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(1)
print(popped_motorcycles)
print(motorcycles)
print("\n")

'''Removing an Item by Value'''
print("Removing an Item by Value")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")



