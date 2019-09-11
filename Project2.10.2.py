"""Files & Exception"""
# Large Files: One Million Digits
print("\nLarge Files: One Million Digits")

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:50] + "...")
print(len(pi_string))

# Searching specific string within a string
print("\nSearching specific string within a string")
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

