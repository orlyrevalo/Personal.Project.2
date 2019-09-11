"""Files & Exception"""

# Reading from a file

with open('pi_digits.txt') as file_object:
    # with open('text_files\filename.txt') as file_object:
    # text_files must be a folder inside the  directory you are working on
    contents = file_object.read()
    print(contents.rstrip())


# Reading Line by Line
print("\nReading Line by Line")
filename = 'pi_digits.txt'
with open(filename) as pi:
    for line in pi:
        print(line.rstrip())


# Making a List of Lines from a File
print("\nMaking a List of Lines from a File")

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(lines)

# Working with a File's Contents
print("\nWorking with a File's Contents")
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))




