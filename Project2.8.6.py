""" Functions"""
# Passing a List
print("\nPassing a List")


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
print("\nModifying a List in a Function")

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing

while unprinted_designs:
    current_design = unprinted_designs.pop().title()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model.title())

# Preventing a Function from Modifying a List
print("\nPreventing a Function from Modifying a List")
# The above script can be written into two functions


def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop().title()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    '''
    Show all the models that were printed
    '''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model.title())



unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)