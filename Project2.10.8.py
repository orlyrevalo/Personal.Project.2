'''Files & Exceptions'''
# Working with Multiple Files


def count_words(filename):
    """Count the approximate number of owords in a file."""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry,  the file " + filename + " does not exist."
        print(msg)
    else:
        # Count  approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'alice.txt'
count_words(filename)

# Failing silently
print("\nFailing silently")


def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count  approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

