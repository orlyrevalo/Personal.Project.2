'''List: Try it Yourself 4-3 - 4-9'''
# 4-3 Counting to Twenty
for value in range(1,21):
    print(value)
# 4-4
list = []
for value in range(0, 1001):
    list.append(value)
print(list)

# 4-5 Summing a Million
list = []
list = [value for value in range(1,1000001)]
print(min(list))
print(max(list))
print(sum(list))

# 4-6 Odd Numbers
for value in range(1, 21, 2):
    print(value)

# 4-7 Threes
for value in range(3, 31, 3):
    print(value)

# 4-8 Cubes
list = []
for value in range(1,11):
    list.append(value**3)
    print(value**3)

# 4-9 Cube comprehension
list = []
list = [value**3 for value in range(1, 11)]
