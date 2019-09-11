""""Files & Exception Try it Yourself 10-3 - 10-5"""

# 10-3 Guest
print("\nGuest")

value = input("What is your name? ")
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(value)

# 10-4 Guest Book
print("\nGuest Book")

while True:
    value = input("What is your name? ")
    print("Hi " + value + ". Thank you for visiting us")
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(value + "\n")
    prompt = input("Quit or Continue?")
    if prompt.lower() == 'quit':
        break
    else:
        continue

# 10-5 Programming Poll
print("\nProgramming Poll")

prompt = input("What are the reasons why you like programming?")
while True:
    with open('programming_responses.txt', 'a') as file_object:
        file_object.write(prompt + "\n")
    prompt = input("If you have don't have other reasons, type in 'quit'.")
    if prompt.lower() == 'quit':
        break





