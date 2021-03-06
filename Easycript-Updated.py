"""This program performs encryption, decryption, key generation, and 
key determination. """


import random


__author__ = "Gabriel Dinner-David, Allan Zhou"


# Gaby (code) and Allan (docstring and examples)
def chunked_string(letters: str) -> str:
    """Space out the string letters in chunks of 5 letters, separacted by a 
    space. Return the new string.
    
    >>> chunked_string("ABCDEFGH")
    "ABCDE FGH" 

    >>> chunked_string("ABCDE") 
    "ABCDE" 

    >>> chunked_string("HFSKAFHEF")
    "HFSKA FHEF" 
    """

    string = ""

    for i in range(len(letters)):
        if (i + 1) % 5 == 0:
            string += letters[i].upper() + " "
        else:
            string += letters[i].upper()

    return string


# Gaby (code) and Allan (docstring)
def get_int(prompt: str) -> int:
    """Return a user inputted integer with prompt prompt."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.\n")


# Gaby (code) and Allan (docstring)
def get_str(prompt: str) -> str:
    """Get a string and filter out all characters not between A and Z.
    Return the filtered string. """

    string = input(prompt)
    letters = ""

    for char in string:
        if "A" <= char.upper() <= "Z":
            letters += char.upper()

    return letters


# Gaby 
def get_key() -> str:
    """Return a string with a length of 1-500, spaced out in chunks of 5."""

    while True:
        key = get_str("A key is any string of letters (1-500 chars): ")

        if 0 < len(key) < 501:
            print("Using encryption key: {}\n".format(key))
            return key

        print("Invalid length.\n")


# Gaby 
def generate_key(length: int) -> str:
    """Generate a string with length characters."""

    key = ""

    for _ in range(length):
        key += chr(random.randrange(65, 91))

    return key


# Gaby
def main_menu():
    """Print the easycrypt menu and return a valid user inputted choice."""

    print(
        "Please choose from one of the following menu options:\n" +
        "1. Encrypt plaintext.\n" + 
        "2. Decrypt ciphertext.\n" + 
        "3. Generate key.\n" + 
        "4. Determine key.\n" + 
        "5. Exit."
    )

    while True:
        choice = get_int("> ")

        if 1 <= choice <= 5:
            return choice
        
        print("Invalid choice. Try again.")


# Gaby (header, body) and Allan (header and function docstring)
def encrypt_menu() -> tuple:
    """Get plaintext and a key from the user and print out the chunked 
    version of it. Return the plaintext and key as strings."""

    plaintext = get_str("Please enter text to encrypt: ")
    print("This is the plaintext: {}\n".format(chunked_string(plaintext)))

    return plaintext, get_key()


# Gaby (body) and Allan (docstring)
def key_gen_menu() -> int:
    """Print the key generation menu and return a user inputted length.
    Ensure that the inputted integer length is between 1 and 500."""

    MAX_LENGTH = 500

    print("Generate an encryption key comprised of random characters " 
        + "(max 500).")
    
    while True:
        length = get_int("\nEnter the desired length of key: ")

        if 0 < length <= MAX_LENGTH:
            return length

        print("Invalid length.\n")


# Gaby 
def decrypt_menu() -> tuple:
    """Get ciphertext and a key from the user and print out the chunked 
    version of it. Return the ciphertext and key as strings."""

    ciphertext = get_str("Please enter text to decrypt: ")
    print("This is the ciphertext: {}\n".format(chunked_string(ciphertext)))
    
    return ciphertext, get_key()


# Allan
def key_menu() -> tuple: 
    """Get plaintext and ciphertext from the user and print out the chunked 
    version of it. Return the plaintext and ciphertext as strings."""

    plaintext = get_str("Please enter the plaintext: ")
    print("This is the plaintext: {}\n".format(chunked_string(plaintext)))

    ciphertext = get_str("Please enter the ciphertext: ")
    print("This is the ciphertext: {}\n".format(chunked_string(ciphertext))) 

    return plaintext, ciphertext


# Gaby (code) and Allan (docstring, examples)
def combine_letters(first: str, second: str, sign: int) -> str:
    """Encrypt character first using character key second if sign is positive.
    Decrypt character first using character key second if sign is negative.
    
    >>> combine_letters("A", "B", 1)
    "C" 

    >>> combine_letters("Z", "F", -1) 
    "T"
    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    char_total = ord(first) + sign*(ord(second) - ENCRYPTION_CONVERSION)

    if chr(char_total) > "Z":
        return chr(char_total - ASCII_CONVERSION)

    elif chr(char_total) < "A": 
        return chr(char_total + ASCII_CONVERSION)

    return chr(char_total)
    

# Allan
def easycrypt(message: str, key: str, decrypt = False) -> str:
    """Return the decrypted version of message using encryption key, key.

    >>> easycrypt("HELLO WORLD", "ABC")
    "IGOMQ ZPTOE" 

    >>> easycrypt("IGOMQ ZPTOE", "ABC", True)
    "HELLO WORLD" 
    """

    new_message = ""

    # Iterate through the string key to encrypt the message.
    key_counter = 0

    for i in range(len(message)): 
        # Rotate back to the first index of the key.
        if key_counter == len(key):
            key_counter = 0

        # Encryption 
        if not decrypt: 
            new_message += combine_letters(message[i], key[key_counter], 1)

        # Decryption
        else:
            new_message += combine_letters(message[i], key[key_counter], -1)

        key_counter += 1

    return new_message


# Allan 
def determine_key(msg: str, encrypted_msg: str) -> str:
    """Print the encryption key from the initial message, msg, and 
    the encrypted message, encrypted_msg. """
    
    ALPHABET_LENGTH = 26
    ASCII_CONVERSION = 64

    key = ""

    # Determine key using the shorter string between msg and encrypted_msg. 
    for i in range(min(len(msg), len(encrypted_msg))):
        if msg[i] == " ":
            continue

        # Figure out the size of the letter shift.
        letter_shift = ord(encrypted_msg[i]) - ord(msg[i])

        # Rotate to end of the alphabet.
        if letter_shift < 1:
            letter_shift = ALPHABET_LENGTH - abs(letter_shift)

        key += chr(letter_shift + ASCII_CONVERSION)

    return shortest_repeating_substring(key)
    

# Allan 
def shortest_repeating_substring(string: str) -> str:
    """Return the shortest repeating substring in string.

    >>> shortest_repeating_substring("AAAAAA") 
    "A"

    >>> shortest_repeating_substring("ABCABCABCAB")
    "ABC" 

    >>> shortest_repeating_substring("ABCDEFGH")
    "ABCDEFGH"
    """

    curr_substring = ""
    length = len(string)

    for char in string:
        curr_substring += char

        length_sub = len(curr_substring)

        # Check for full reoccurences of the substring.
        repeat = length // length_sub

        start_index = 0
        end_index = length_sub

        for i in range(repeat):
            if not(curr_substring == string[start_index:end_index]):
                break

            # Check the next substring of letters in string.
            elif end_index + length_sub <= length:
                start_index += length_sub
                end_index += length_sub
                continue

            else:
                # Check remaining letters for partial occurence 
                # of the substring.
                shortest_substring = curr_substring
                is_matching = True

                substring_index = 0

                for i in range(end_index, length):
                    if not(shortest_substring[substring_index] == string[i]):
                        is_matching = False

                    else:
                        substring_index += 1

                if is_matching:
                    # Key should be given in chunks of 5 characters.
                    key = ""

                    for i in range(len(shortest_substring)):
                        if i % 5 == 0 and i != 0:
                            key += " "

                        key += shortest_substring[i]

                    return key


# Gaby and Allan
def main():
    """Runs easycrypt with menu options for encryption, decryption, key
    generation, key determination, and exiting."""
    
    print(
        "----------------------------------\n" + 
        "EasyCrypt Text Encryptor/Decryptor\n" + 
        "----------------------------------"
    )

    while True:
        choice = main_menu()

        if choice == 1:
            print()
            plaintext, key = encrypt_menu()
            print("Your message has been encrypted:")
            print(chunked_string(easycrypt(plaintext, key)))
            print()

        elif choice == 2:
            print()
            cyphertext, key = decrypt_menu()
            print("Your message has been decrypted:")
            print(chunked_string(easycrypt(cyphertext, key, True)))
            print()

        elif choice == 3:
            print()
            length = key_gen_menu()
            print("Your new encryption key: ")
            print(generate_key(length))
            print()

        elif choice == 4: 
            print() 
            plaintext, ciphertext = key_menu()
            key = determine_key(plaintext, ciphertext)
            print("The encryption key used is: \n{}\n".format(key))

        elif choice == 5:
            break


if __name__ == "__main__":
    main()
