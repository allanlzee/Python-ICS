def num_digits(string): 
    """Return the number of digits in a string."""

    # Total number of digits in the string.
    digits = 0 

    for char in string: 
        if 48 <= ord(char) <= 57: 
            digits += 1 
        
    return digits 

input_string = input("Enter a string: ") 

print("There are {} digits in the string.".format(num_digits(input_string)))
