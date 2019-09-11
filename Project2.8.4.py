"""Functions: Using a with a while loop"""
# Using a Function with a while Loop
print("\nUsing a Function with a while Loop")


def get_formatted(first_name, last_name):
    """"Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# This is an infinte loop!

while True:
    print("Please tell me your name:")
    print("(enter 'q'at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted(f_name, l_name)
    print(formatted_name)

