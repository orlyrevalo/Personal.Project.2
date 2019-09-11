'''Functions'''
# Returning a Simple Value
print("Returning a Simple Value")

def get_formatted(first_name, last_name):
    """"Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted('jimi', 'hendrix')
print(musician)

# Making an  Argument Optional
print("\nMaking an Argument Optional")


def get_formatted(first_name, middle_name, last_name):
    """"Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted('jimi', 'lee', 'hendrix')
print(musician)

# Returning a Dictionary
print("\nReturning a Dictionary")

def build_person(first_name, last_name, age=''):
    """Return  a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('Orly', 'Revalo', age=27)
print(musician)

