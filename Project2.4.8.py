'''Lists'''
# Using the range() Function
for value in range(1, 5):
    print(value)

# Using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(0, 11, 2))
print(even_numbers)

# Building square values and storing in a list
squares = []
for value in range(1,11):
    square = value*value
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Simple Statistics with a list of numbers
print("\nSimple Statistics with a list of numbers")
digits = [1, 2, 3, 4,5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
