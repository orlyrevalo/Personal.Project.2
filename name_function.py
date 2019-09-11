
'''
# initial instance of name_function.py
def get_formatted_name(first, last):
    """Generated a neatly formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()
'''
'''
# second instance of name_function.py
def get_formatted_name(first, middle,  last):
    """Generated a neatly formatted full name"""
    full_name = first + ' ' +middle + ' ' + last
    return full_name.title()
'''

# second instance of name_function.py

def get_formatted_name(first, last, middle=''):
    """Generated a neatly formatted full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()