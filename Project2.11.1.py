"""Testing your Code"""

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

# Unit Tests and Test Cases
print("\nUnit Tests and Test Case")

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py' """

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()

# A Failing Test
print("\nA failing Test")

'''
# second instance of name_function.py
def get_formatted_name(first, middle,  last):
    """Generated a neatly formatted full name"""
    full_name = first + ' ' +middle + ' ' + last
    return full_name.title()
'''




