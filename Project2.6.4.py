'''Dictionary'''
# Looping through a Dictionary
print("Looping through a Dictionary")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("\n")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Looping Through All the Keys in a Dictionary
print("\nLooping Through All the Keys in a Dictionary")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for names in favorite_languages.keys():
    print(names.title())
''' Is the Same as: 
for names in favorite_languages: <<< without the .keys() 
    print(names.title())
'''
print("\n")
friend = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friend:
        print(" Hi " + name.title() + ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

print("\n")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")