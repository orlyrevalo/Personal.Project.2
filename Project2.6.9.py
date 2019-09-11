'''Dictionaries: Dictionary in a Dictionary'''
# Dictionary in a Dictionary
print("\nDictionary in a Dictionary")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " "+ user_info['last']
    location = user_info['location']
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())

#   for description_key, description_value in descriptions[user].items():
#      print("\t" + description_key + ": " + description_value.title())

'''
==========================================================================
==========================================================================
'''
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    for user_key, user_value in user_info.items():
        print("\t" + user_key.title() + ": " + user_value.title())
