"""Functions Try it Yourself 8-9 - 8-11"""
# 8-9  Magicians
print("\n8-9  Magicians")


def show_magicians1(magician_names):

    for magician_name in magician_names:
        print(magician_name)


magician_names = ['Rik', 'Price', 'Jasmine', 'Ash', 'Orly']
print("Here is the list of all the magicians: ")
show_magicians1(magician_names)



# 8-10 Great Magicians
print("\n8-10 Great Magicians")


def show_magicians2(magician_names):
    '''Print the names of all the magician'''
    for magician_name in magician_names:
        print(magician_name)


def make_great(magician_names, great_magician):
    '''Append 'the great' to each magician'''
    while magician_names:
        great_magician_name = magician_names.pop() + " the great"
        great_magician.append(great_magician_name)


magician_names = ['Rik', 'Price', 'Jasmine', 'Ash', 'Orly']
great_magicians = []
print("Here is the list of all the great magicians: ")
make_great(magician_names, great_magicians)
show_magicians2(great_magicians)


# 8-11 Un-changed Magicians
print("\n8-11 Unchanged Magicians")


def show_magicians3(great_magicians):
    '''Print the names of all the magician'''
    for great_magician in great_magicians:
        print(great_magician)
    for magician_name in magician_names:
        print(magician_name)

def make_great1(magician_names, great_magician):
    '''Append 'the great' to each magician'''
    while magician_names:
        great_magician_name = magician_names.pop() + " the great"
        great_magician.append(great_magician_name)


magician_names = ['Rik', 'Price', 'Jasmine', 'Ash', 'Orly']
great_magicians = []
print("Here is the list of all the great magicians: ")
make_great1(magician_names[:], great_magicians)
show_magicians3(great_magicians)
print(great_magicians)
print(magician_names)
