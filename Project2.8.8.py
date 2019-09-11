"""Function"""
# Passing an Arbitrary Number of Arguments
print(" \nPassing an Arbitrary Number of Arguments")


def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

'''
==============================================================================
==============================================================================
'''


def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza we are about to make")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


