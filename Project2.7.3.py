'''Introducing While Loops'''

# While loop
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit & using a Flag
prompt = "\nTell me something, and I will repeat it back to you. "
prompt += "\nEnter 'quit' to end 'the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

