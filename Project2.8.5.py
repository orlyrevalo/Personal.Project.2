"""Function: Try it Yourself 8-6 - 8-8"""
# 8-6 City Names
print("\nCity Names")


def city_names(city_name, country):
    formatted_city_name = "\"" + city_name.title() + ", " + country.title() + "\""
    print(formatted_city_name)


city_pairs = [['Manila', 'Philippines'], ['Espana', 'Spain'], ['Paris', 'France']]

for city_pair in city_pairs:
    city_names(city_pair[0], city_pair[1])

# 8-7 Album
print("\nAlbum")


def make_album(artist_name, album_title, tracks=''):
    album = {'artist name': artist_name,  'album title': album_title}
    if tracks:
        album['No. of tracks'] = tracks
    print(album)
    return album


make_album('Stromae', 'Papatoui')
make_album('CNCO', 'Para Enamorarte', '2')
make_album('La Vie en Rose', 'Neil Armstrong')

# 8-8 User Album
print("\nUser Albums")


def make_album(artist_name, album_title, tracks=''):
    album = {'artist name': artist_name,  'album title': album_title}
    if tracks:
        album['No. of tracks'] = tracks
    print(album)
    return album


while True:
    a_name = input("Who is the artist of your album track? ")
    a_title = input("What is the title of your album track? ")
    make_album(a_name, a_title)
    prompt = input("Enter 'q' to quit ")
    if prompt == 'q':
        break
