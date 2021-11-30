"""Easily encrypt and decrypt text"""
import random


__author__ = "Gabriel Dinner-David, Allan Zhou"


def chunked_string(letter_list: list) -> str:
    """Return a string made up of uppercase letters from a letter_list
    seperated into groups of 5.
    
    >>> chunked_string(["A", "B", "C", "D", "E", "F", "G", "H"])
    "ABCDE FGH" 

    >>> chunked_string(["A", "B", "C", "D", "E"]) 
    "ABCDE" 
    """

    string = ""
    for i in range(len(letter_list)):
        if (i + 1) % 5 == 0:
            string += letter_list[i].upper() + " "
        else:
            string += letter_list[i].upper()

    return string


def get_int(prompt: str = None) -> int:
    """Return a user inputted integer with prompt prompt."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("invalid input")


def get_str_list(prompt: str = None) -> list:
    """Get a list of characters from an entered string and
    return the list. """

    string = input(prompt)
    str_list = []
    for char in string:
        if "A" <= char.upper() <= "Z":
            str_list.append(char.upper())
    return str_list


def get_key() -> list:
    """Return a string with a length of 1-500, spaced out in chunks of 5."""

    while True:
        key = get_str_list("A key is any string of letters (1-500 chars): ")
        if 0 < len(key) < 501:
            print("Using encryption key: {}\n".format(chunked_string(key)))
            return key
        print("Invalid length")


def gen_key(length: int) -> list:
    """Generate a list of length letters."""

    key = []
    for _ in range(length):
        key.append(chr(random.randrange(65, 91)))
    return key


def main_menu():
    """Print the easycrypt menu and return a valid user inputted choice."""

    print(
        "Please choose from one of the following menu options: " +
        "1. Encrypt plaintext." + 
        "2. Decrypt ciphertext." +
        "3. Generate key." + 
        "4. Exit.\n"
    )
    while True:
        choice = get_int("> ")
        if 0 < choice < 5:
            return choice
        print("Invalid choice. Try again.")


def encrypt_menu() -> tuple:
    """Get unencrypted text and a key from the user and print out the chunked 
    version of it. Return the string and key as a list of characters."""

    plaintext = get_str_list("Please enter text to encrypt: ")
    print("This is the plaintext: {}\n".format(chunked_string(plaintext)))
    return plaintext, get_key()


def key_gen_menu() -> int:
    """Print the key generation menu and return a user inputted length.
    Ensure that the length is between 1 and 500."""

    print("Generate an encryption key comprised of random characters " 
        + "(max 500).")

    while True:
        length = get_int("Enter the desired length of key: ")
        if 0 < length < 501:
            return length
        print("Invalid length. Please try again.")


def decrypt_menu() -> tuple:
    """Get encrypted text and a key from the user and print out the chunked 
    version of it. Return the string and key as a list of characters."""

    ciphertext = get_str_list("Please enter text to decrypt: ")
    print("This is the ciphertext: {}\n".format(chunked_string(ciphertext)))
    return ciphertext, get_key()


def combine_letters(first: str, second: str, sign: int) -> str:
    """Encrypt character first using character key second if sign is positive.
    Decrypt character first using character key second if sign is negative."""

    char_total = ord(first) + sign*(ord(second) - 64)

    if char_total > 90:
        return chr(char_total - 26)

    elif char_total < 65: 
        return chr(char_total + 26)

    return chr(char_total)
    

def easycrypt(text: list, key: list, decrypt: bool = False) -> list:
    """Encrypt plaintext text using encryption key key if decrypt is False. 
    Decrypt ciphertext test using encryption key key if decrypt is True.
    
    >>> easycrypt("""

    sign = 1

    if decrypt:
        sign = -1

    encrypted_message: list[str] = []

    for i in range(len(text)):
        encrypted_message.append(combine_letters(text[i], key[i], sign))

    return encrypted_message


def fill_plaintext(plaintext: list):
    while len(plaintext) % 5 != 0:
        plaintext.append(chr(random.randrange(96, 123)))


def fill_key(key: list, text: list):
    while len(key) < len(text):
        key.append(key[-1])


def main():
    """Run's the whole easycrypt with nice menu's"""
    print(
        """----------------------------------
EasyCrypt Text Encryptor/Decryptor
----------------------------------"""
    )

    print(easycrypt("ABCDEFHGHIJK", "ABC"))
    
    """ while True:
        choice = main_menu()
        if choice == 1:
            print()
            plaintext, key = encrypt_menu()
            fill_plaintext(plaintext)
            fill_key(key, plaintext)
            print("Your message has been encrypted:")
            print(chunked_string(easycrypt(plaintext, key)))
            print()

        elif choice == 2:
            print()
            cyphertext, key = decrypt_menu()
            fill_key(key, cyphertext)
            print("Your message has been decrypted:")
            print(chunked_string(easycrypt(cyphertext, key, True)))

        elif choice == 3:
            print()
            length = key_gen_menu()
            key_string = ""
            for letter in gen_key(length):
                key_string += letter
            print(key_string)
            print()

        elif choice == 4:
            break

    print("\nThank you for using EasyCrypt. Goodbye.") """


if __name__ == "__main__":
    main()