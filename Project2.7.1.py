'''Input'''

# How the input() Function Work
message = input("Tell me something, and I will repeat it back to you. ")
print(message)
name = input("Please enter your name: ")
print("Hello, " + name + " !")

height = input( "How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'll  be able to ride when you're a little older.")

# Modulo Operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")