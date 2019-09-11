'''While Loop'''
# Using break to Exit a Loop
print("Using break to Exit a Loop")
prompt = "\nPlease enter the name of the city you have visited"
prompt += "\n(Enter 'quit' when you are finished.)"
city = input(prompt)
while True:
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a Loop
print("\nUsing continue in a Loop")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Avoiding Infinite Loops
print("\nAvoiding Infinite Loops")
x = 1
while x <= 5:
    print(x)
    x += 1
