"""Files & Exception: Try it Yourself 10-1 - 10-2"""
# 10-1 Learning Python
print("\n10-1  Learning Python")

filename = 'learning_python.txt'

with open(filename) as file_object:
    contents, counter = [], 0
    for line in file_object:
        contents.append(line.strip())
    while counter < 3:
        counter += 1
        print("Number of prints: " + str(counter))
        for content in contents:
            print(content)

print("\nPrinting contents once by reading entire file by looping over the file object")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\nPrinting contents once by reading entire file and storing lines in a list ")
with open(filename) as file_object:
    contents = file_object.readlines()
    for content in contents:
        print(content.strip())

# 10-2 Learning C
print("\nLearning C")

with open(filename) as file_object:
    contents = file_object.readlines()
    for content in contents:
        print(content.replace("Python", "C").strip())
    print(contents)
