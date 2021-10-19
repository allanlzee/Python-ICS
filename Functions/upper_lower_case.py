def to_upper(string): 
    """Converts all lowercase characters to uppercase characters 
    and prints the new string."""

    uppercase_string = ""

    for char in string: 
        if 97 <= ord(char) <= 122: 
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char

    return uppercase_string


def to_lower(string): 
    """Converts all uppercase characters to lowercase characters 
    and prints the new string."""

    lowercase_string = ""

    for char in string: 
        if 65 <= ord(char) <= 90: 
            lowercase_string += chr(ord(char) + 32)
        else:
            lowercase_string += char

    return lowercase_string

