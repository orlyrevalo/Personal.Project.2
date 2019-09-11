'''Functions'''

# Defining a functino
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def greet_user(username):
    print("Hello! " + username.title() + "!")


greet_user('jesse')

# Keyword Arguments
print("\nKeyword Arguments")


def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type +"'s name is "+ pet_name.title())


describe_pet(animal_type='hamster', pet_name='harry')

# Default Values
print("\nDefault Values")


def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet(pet_name='willie')

# Equivalent Function Calls
print("\nEquivalent Function Calls ")

# a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
