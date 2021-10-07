numbers = ""
letters = "" 
other_chars = ""

input_string = input("Enter a string: ")
 
for letter in input_string: 
    # Find Numbers 
    if ord(letter) >= 48 and ord(letter) <= 57: 
        numbers += letter
    # Uppercase Letters
    elif ord(letter) >= 65 and ord(letter) <= 90: 
        letters += letter
    # Lowercase Letters 
    elif ord(letter) >= 97 and ord(letter) <= 122: 
        letters += letter
    else: 
        other_chars += letter

print("Numbers: {}.".format(numbers))
print("Letters: {}.".format(letters))
print("Other Characters: {}.".format(other_chars))