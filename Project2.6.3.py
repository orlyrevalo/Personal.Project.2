'''Dictionaries: Try it Yourself 6-1 - 6-3'''
# 6-1 Person
user_details = {
    'first name': 'orly',
    'last name': 'revalo',
    'age': '28',
    'city': 'pasig city',
}
for user_detail in user_details:
    print(user_detail.title() + ": " + user_details[user_detail].title())
print(user_details)

# 6-2 Favorite Numbers
favorite_numbers = {
    'orly': 25,
    'ash': 30,
    'rik': 40,
    'price': 45,
    'jasmine': 50,
}
for favorite_number in favorite_numbers:
    print("Your favorite number " + favorite_number.title() + " is "+
          str(favorite_numbers[favorite_number]))

# 6-3 Glossary
glossary_list = {
    'if statement': 'is a programming conditional statement that, if proved true, '
                    'performs a function or displays information',
    'tuples': 'is a collection which is ordered and unchangeable.',
    'list': 'is a collection which is ordered and changeable',
    }
for glossary in glossary_list:
    print(glossary.title() + "\n" + glossary_list[glossary] + "\n")

