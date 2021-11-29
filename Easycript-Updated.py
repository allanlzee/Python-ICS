"""Easily encrypt and decrypt text"""
import random

__author__ = "Gabriel Dinner-David, Allan Zhou"


def chunked_string(letters: str) -> str:
    """Space out the string letters in chunks of 5 letters, separacted by a 
    space. Return the new string.
    
    >>> chunked_string("ABCDEFGH")
    "ABCDE FGH" 

    >>> chunked_string("ABCDE") 
    "ABCDE" 
    """

    string = ""

    for i in range(len(letters)):
        if (i + 1) % 5 == 0:
            string += letters[i].upper() + " "
        else:
            string += letters[i].upper()

    return string


def get_int(prompt: str = None) -> int:
    """Return a user inputted integer with prompt prompt."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")


def get_str(prompt: str = None) -> str:
    """Get a string and filter out all characters not between A and Z.
    Return the filtered string. """

    string = input(prompt)
    letters = ""
    for char in string:
        if "A" <= char.upper() <= "Z":
            letters += char.upper()
    return letters


def get_key() -> str:
    """Return a string with a length of 1-500, spaced out in chunks of 5."""

    while True:
        key = get_str("A key is any string of letters (1-500 chars): ")
        if 0 < len(key) < 501:
            print("Using encryption key: {}\n".format(key))
            return key
        print("invalid length")


def gen_key(length: int) -> str:
    """Generate a string with length characters."""

    key = ""

    for _ in range(length):
        key += chr(random.randrange(65, 91))

    return key


def main_menu():
    """Print the easycrypt menu and return a valid user inputted choice."""

    print(
        """Please choose from one of the following menu options:
1. Encrypt plaintext.
2. Decrypt ciphertext.
3. Generate key.
4. Exit."""
    )
    while True:
        choice = get_int("> ")
        if 0 < choice < 5:
            return choice
        print("Invalid choice. Try again.")


def encrypt_menu() -> tuple:
    """Get plaintext and a key from the user and print out the chunked 
    version of it. Return the plaintext and key as strings."""

    plaintext = get_str("Please enter text to encrypt: ")
    print("This is the plaintext: {}\n".format(chunked_string(plaintext)))

    return plaintext, get_key()


def key_gen_menu() -> int:
    """Print the key generation menu and return a user inputted length.
    Ensure that the inputted integer length is between 1 and 500."""

    print("Generate an encryption key comprised of random characters (max 500).")
    
    while True:
        length = get_int("Enter the desired length of key: ")
        if 0 < length < 501:
            return length
        print("invalid length")


def decrypt_menu() -> tuple:
    """Get ciphertext and a key from the user and print out the chunked 
    version of it. Return the ciphertext and key as strings."""

    ciphertext = get_str("Please enter text to decrypt: ")
    print("This is the ciphertext: {}\n".format(chunked_string(ciphertext)))
    
    return ciphertext, get_key()


def combine_letters(first: str, second: str, sign: int) -> str:
    """Encrypt character first using character key second if sign is positive.
    Decrypt character first using character key second if sign is negative."""

    char_total = ord(first) + sign*(ord(second) - 64)

    if char_total > 90:
        return chr(char_total - 26)

    if char_total < 65:
        return chr(char_total + 26)

    return chr(char_total)


def validate_text(text: str) -> bool: 
    """Return False if either message or key is empty.
    Otherwise, return True."""
    
    if len(text) == 0:
        return False

    else: 
        return True 

def easycrypt(message: str, key: str, decrypt = False) -> str:
    """Return the decrypted version of message using encryption key, key.

    >>> decrypt("ABCDEFGHIJKLMNOP", "ABCD", True)
    "ZZZZD DDDHH HHLLL L" 
    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    if not validate_text(message): 
        return 
    
    elif not validate_text(key): 
        return

    crypted_message = ""

    # Iterate through the string key to encrypt the message.
    key_counter = 0

    for i in range(len(message)):
        # Spaces should simply be added to the encrypted message.
        if message[i] == " ":
            crypted_message += " "
            continue

        # Rptate back to the first index of the key.
        if key_counter == len(key):
            key_counter = 0

        if key[key_counter] == " ":
            key_counter += 1

        curr_msg_char = ord(message[i])

        # The magnitube of the character shift is the letter's alphabet spot.
        key_convert = ord(key[key_counter]) - ENCRYPTION_CONVERSION

        if decrypt: 
            if chr(curr_msg_char + key_convert) > "Z":
                curr_msg_char -= ASCII_CONVERSION

            new_msg_char = chr(curr_msg_char + key_convert)

            crypted_message += new_msg_char

            key_counter += 1

        elif decrypt:
            # Ensure that the encrypted character does not become a non-letter.
            if chr(curr_msg_char - key_convert) < "A":
                curr_msg_char += ASCII_CONVERSION

            new_msg_char = chr(curr_msg_char - key_convert)

            crypted_message += new_msg_char

            key_counter += 1

    return crypted_message


def fill_plaintext(plaintext: str):
    letters_needed = 5 - len(plaintext) % 5
    if letters_needed == 5:
        letters_needed = 0
    return plaintext + gen_key(letters_needed)


def fill_key(key: str, text: str):
    while len(key) < len(text):
        key += (key[-1])
    return key


def main():
    """Run's the whole easycrypt with nice menu's"""
    print(
        """----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------"""
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
            key_string = ""
            for letter in gen_key(length):
                key_string += letter
            print(key_string)
            print()

        elif choice == 4: 
            print() 
            

        elif choice == 5:
            break

    print("\nThank you for using EasyCrypt. Goodbye.")


if __name__ == "__main__":
    main()