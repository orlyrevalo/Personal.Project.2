'''Lists: Try it Yourself 4-10 - 4-12'''

# 4-10 Slices
digits = [1, 2, 3, 4,5, 6, 7, 8, 9, 0]
print("The first three items in the list are:")
for digit in digits[:3]:
    print(digit)
print("Three items from the middle of the list are:")
for digit in digits[3:6]:
    print (digit)
print("The last three items in the lsit are:")
for digit in digits[-3:]:
    print(digit)

# 4-11 My Pizzas, Your Pizzas
pizza_list = ['Pepperoni', 'Hawaiian', 'Tribecca', 'Shitake']
friend_pizza = pizza_list[:]
pizza_list.append('4 Cheese')
friend_pizza.append('Prosciutto')
print("My favorite pizza are ")
for pizza in pizza_list:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

