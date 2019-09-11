'''Files & Exception'''

# Handling the Zero Division Exception
print("\nHandling the Zero Division Exception")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")

# Using Exceptions to Prevent Crashes
print("\nUsing Exceptions to Prevent Crashes")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

try:
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("\nSecond number: ")
        if second_number == 'q':
            break
        answer = int(first_number)/int(second_number)
        print(answer)
except ZeroDivisionError:
    print("You can't divide by zero")


