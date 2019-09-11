'''Functions: Try it Yourself 8-3 - 8-5'''
# 8-3 T-Shirt
print("\nT-Shirt")


def make_shirt(size, text):
    print("The size of the shirt is " + size + " with a print of \"" + text + "\".")


make_shirt('medium', 'Instant Human, Just add Coffee')
make_shirt(size='medium', text='Instant Human, Just add Coffee')

# 8-4 Large Shirts
print("\nLarge Shirts")


def make_shirt(size='large', text='I love Python'):
    print("The size of the shirt is " + size + " with a print of \"" + text + "\".")


make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='Instant Human, Just add Coffee')


# 8-5 Cities
print("\nCities")


def describe_city(city_name, country='Philippines'):
    print(city_name.title() + ' is in ' + country.title())


describe_city('manila')
describe_city(city_name='makati')
describe_city('kuala lumphur', country='malaysia')
