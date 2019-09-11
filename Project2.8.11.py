'''Function'''
# Importing an Entire Module
print("Importing an Entire Module")
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# from module_name import function_name
# from module_name import function_name_0, function_name_1, function_name_2
print("\nImporting Specific Functions")

from pizza import make_pizza

make_pizza(15,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
# from module_name import function_name as fn
print("\nUsing as to Give a Function an Alias")

import pizza as p

p.make_pizza(15, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# from module_name import *
print("\nImporting  All Functions in a Module")

from pizza import *

make_pizza(15, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')









