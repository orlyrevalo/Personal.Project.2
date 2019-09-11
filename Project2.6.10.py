'''Dictionaries: Try it Yourself 6-7 - 6-12'''
# 6-7 People
user_0 = {
        'first name': 'orly',
        'last name': 'revalo',
        'age': '28',
        'city': 'pasig city',
    }
user_1 = {
        'first name': 'rik',
        'last name': 'morty',
        'age': '25',
        'city': 'makati city',
    }
user_2 = {
        'first name': 'rik',
        'last name': 'meister',
        'age': '22',
        'city': 'mandaluyong city',
    }

people = [user_0, user_1, user_2]
for user in people:
    for user_info, user_det in user.items():
        print(user_info.title() + ": " + user_det.title())
    print("\n")

# 6-8 Pets
pia = {
    'name': 'pia',
    'kind': 'cat',
    'owner': 'regg',
}
brownie = {
    'name': 'brownie',
    'kind': 'dog',
    'owner': 'bruce',
}
lucky = {
    'name': 'lucky',
    'kind': 'gerbel',
    'owner': 'dave',
}
pets = [pia, brownie, lucky]
for pet in pets:
    for pet_info, pet_det in pet.items():
        print(pet_info.title() + ": " + pet_det.title())
    print("\n")

# 6-9 Favorite Places
favorite_places = {
    'orly': ['kuala lumphur', 'ho chi minh', 'manila'],
    'jasmine': ['honolulu', 'beijing', 'paris'],
    'price': ['sydney', 'maldives', 'rome'],
}
for name, places in favorite_places.items():
    print("Hi " + name.title() + ", I believe your favorite places are:")
    for place in places:
        print("\t" + place.title())
    print("\n")

# 6-10 Favorite Numbers
favorite_numbers = {
    'orly': [25, 30, 35, 40],
    'ash': [30, 40, 50, 60, 70],
    'rik': [40, 44, 48, 52],
    'price': [45, 60, 75, 90],
    'jasmine': [50, 100, 150]
}
for user, favorite_number in favorite_numbers.items():
    print(user.title() + ", your favorite numbers are:")
    for number in favorite_number:
        print(str(number))

# 6-11 Cities
cities = {
    'manila': {
        'country': 'philippines',
        'population': 25000000,
        'fact': "It's fun in the Philippines",
    },
    'new york': {
        'country': 'United States of America',
        'population': 45000000,
        'fact': 'The Big Apple',
    },
    'amsterdam': {
        'country': 'Netherlands',
        'population': 5000000,
        'fact': "Located in the European Union",
    },
}

for city_name, city_info in cities.items():
    print(city_name.title())
    for key, value in city_info.items():
        print(key.title() + ": " + str(value))
    print("\n")
