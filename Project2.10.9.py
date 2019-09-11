"""Files & Exception Try it Yourself 10-6 - 10-11"""
# 10-6 Addition
print("10-6 Addition")

print("Input two numbers and I will give you the sum of those two numbers:")
try:
    first_number = int(input("First Number: "))
    second_number = int(input("Second Number: "))
except ValueError:
    print("You can't add string values")
else:
    summation = int(first_number) + int(second_number)
    print("The sum of these two numbers are " + str(summation))

# 10-7 Addition Calculator
print("\nAddition Calculator")

while True:
    print("Input two numbers and I will give you the sum of those two numbers:")
    try:
        first_number = int(input("First Number: "))
        second_number = int(input("Second Number: "))
    except ValueError:
        print("You can't add string values")
    else:
        summation = int(first_number) + int(second_number)
        print("The sum of these two numbers are " + str(summation))
    prompt = input("\nDo you want to try again? 'y' or 'n' ")
    if prompt.lower() == 'n':
        break

# 10-9 Cats and Dogs
print("\nCats and Dogs")

petnames = ['cats.txt', 'dogs.txt']
for pet in petnames:
    try:
        with open(pet) as f_obj:
            contents = f_obj.readlines()
    except FileNotFoundError:
        print("The file " + pet + " does not exist.")
    else:
        print("These are the names of the pets in " + pet + ":")
        for name in contents:
            print(name.title().strip())

# 10-10 Silent Cats and Dogs
print("\nSilent Cats and Dogs")
petnames = ['cats.txt', 'rats.txt', 'dogs.txt']
for pet in petnames:
    try:
        with open(pet) as f_obj:
            contents = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        print("These are the names of the pets in " + pet + ":")
        for name in contents:
            print(name.title().strip())


# 10-11 Common Words
print("\nCommon Words")


def count_the(text_file):
    """Count 'the' in a text file."""

    try:
        with open(text_file) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        the_counter = 0
        for word in words:
            if word.lower() == 'the':
                the_counter += 1
        print("The file " + text_file + " has about " + str(the_counter) + " 'the' words.")


def count_the1(text_file):
    """Count 'the' in a text file."""

    try:
        with open(text_file) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        the_counter = contents.lower().count('the')
        print("The file " + text_file + " has about " + str(the_counter) + " 'the' words.")


count_the('alice.txt')
count_the1('alice.txt')

