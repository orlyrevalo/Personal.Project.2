""""Files & Exception"""

# Writing to a File
print("\nWriting to a File")

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# Writing Multiple Lines
print("\nWriting Multiple Lines")

file_name = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")
    file_object.write("I love creating new games. \n")


# Appending to a File
print("\nAppending to a File")

filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large data sets. \n")
    file_object.write("I love creating apps that can run in a browser \n")



