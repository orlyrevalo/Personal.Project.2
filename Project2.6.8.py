'''Dictionaries: List in a Dictionary'''
# List in a Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + " crust pizza" +
      " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping.title())

'''
===============================================================
===============================================================
'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
    'orly': ['python', 'sql'],
    'ash': ['ruby'],
    'rik': ['java'],
    'jasmine': ['c'],
    'price': ['java', 'ruby']
}

for name, languages in favorite_languages.items():
    if len(favorite_languages[name]) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite languages is:")
    for language in languages:
        print("\t" + language.title())



