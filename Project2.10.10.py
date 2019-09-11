"""Files & Exception"""
# Using json.dump() and json.load()
print("\nUsing json.dump() and json.load()")
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

