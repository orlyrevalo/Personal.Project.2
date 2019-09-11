'''Dictionaries Try it Yourself 6-4 - 6-6'''
# 6-4 Glossary 2
# 6-5 Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'africa',
    'yangtze': 'china',
}
for river, place in rivers.items():
    print("The " + river.title() + " river runs through " + place.title() +".")
for river in rivers.keys():
    print(river.title())
for place in rivers.values():
    print(place.title())

# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'orly': 'python',
    'ash': 'ruby',
    'rik': 'java',
    'jasmine': 'c',
    'price': 'java',
}
poll_takers = ['orly', 'joy', 'cy', 'catherine', 'ash', 'jen']
for poll_taker in poll_takers:
    if poll_taker in favorite_languages.keys():
        print("Thank you for responding to the poll, " + poll_taker.title())
    else:
        print("Please take the poll, " + poll_taker.title())
print("\nThe following languages where mentioned in the poll: ")
for language in set(favorite_languages.values()):
    print(language.title())


