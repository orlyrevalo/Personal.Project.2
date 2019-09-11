'''Organizing List'''
# Sorting a list Permanently with the sort() Method
print("Sorting a list Permanently with the sort() Method")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
print("\nSorting a List Temporarily with the sorted() Function")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list:again")
print(cars)

# Printing a List in Reverse Order
print("\nPrinting a List in Reverse Order")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
print("\nFinding the Length of a List")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))