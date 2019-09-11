'''Dictionaries'''
# Removing Key-Value Pairs
print('Removing Key-Value Pairs')
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
print('\nA Dictionary of Similar Objects ')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

