'''Dictionaries'''
# Looping through a dictionary's keys in order
print("Looping through a dictionary's keys in order")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary
print("\nLooping through all values in a dictionary")
print("The following language has been mentioned")
for language in favorite_languages.values():
    print(language.title())

# Checking for repeated values in a dictionary
print("\nChecking for repeated values in a dictionary")
for language in set(favorite_languages.values()):
    print(language.title())

