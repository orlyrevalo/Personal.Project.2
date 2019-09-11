'''While Loops Try it Yourself 7-4 - 7-7'''
# 7.4 Pizza Toppings:
prompt = "\nWhat toppings would you like to add to your pizza."
prompt += "\nEnter 'quit' when you are finished. "
topping = input(prompt)
counter = False
while True:
    if counter:
        topping = input("Do you want to add more? If no, 'quit' to finish: ")
    if topping == 'quit':
        break
    else:
        print("Adding " + topping.title() + " to your pizza.")
        counter = True

# 7.5 Movie Tickets
print("\nMovie Tickets")
print("To know the cost of your movie ticket")
while True:
    age = input("Please enter your age or enter 'quit' to end.")
    if age == 'quit':
        break
    if int(age) < 3:
        cost = 0
    elif int(age) < 12:
        cost = 10
    else:
        cost = 15
    print("Your movie ticket cost $ " + str(cost)+ ".")

# 7.6 Three Exits
print("\nThree Exits")
print("To know the cost of your movie ticket")
counter = 1
while True:
    age = input("Please enter your age or enter 'quit' to end.")
    if age == 'quit' or counter == 5:
        break
    elif int(age) < 3:
        cost = 0
    elif int(age) < 12:
        cost = 10
    else:
        cost = 15
    counter += 1
    print("Your movie ticket cost $ " + str(cost)+ ".")

# 7.7 Infinity
while True:
    print(":D")
    