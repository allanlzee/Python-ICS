def string_separator(string): 
    """Print a string so each character is on its own line, 
    preceded by its index."""

    for index in range(len(string)): 
        print("Index {}: '{}'".format(index, string[index]))


input_string = input("Enter a string: ")
string_separator(input_string)