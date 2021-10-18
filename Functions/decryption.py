def caesar(upper_string, key): 
    """Return an string that has been encrypted using Caesar Cipher 
    and is spaced out in blocks of 5 uppercase letters."""

    encrypted_string = "" 

    for letter in range(0, len(upper_string)): 
        if letter % 5 == 0 and letter != 0: 
            encrypted_string += " "

        # Caesar Shift for encryption. 

        # If letter goes over the ASCII value for Z when shifted, cycle 
        # back to the beginning of the alphabet. 
        if ord(upper_string[letter]) + key > 90: 
            encrypted_string += chr(ord(upper_string[letter]) - 26 + key)
        else: 
            encrypted_string += chr(ord(upper_string[letter]) + key)

    return encrypted_string 


string = input("Enter a string: ")
key = int(input("Enter an encryption key: "))
encrypted = caesar(string, key)
print(encrypted)
