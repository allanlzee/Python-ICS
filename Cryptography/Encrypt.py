""""Encrypt, decrypt, generate a key, and guess the encyrption key."""


__author__ = "Allan Zhou"


from random import randint


def char_filter(message: str) -> str:
    """Filters out all non-letter characters from message, which is a string
    with letters that have all been capitalized.

    >>> char_filter("IIIHDHSN&(#^@*")
    IIIHD HSN

    """
    message = message.upper()

    filtered_chars = []

    filtered_str = ""

    for i in range(len(message)):
        # Append letters to filtered string.
        if "A" <= message[i] <= "Z":
            filtered_chars.append(message[i])

    for i in range(len(filtered_chars)):
        if i % 5 == 0 and i != 0:
            filtered_str += " "

        filtered_str += filtered_chars[i]

    return filtered_str


def encrypt(message: str, key: str) -> str:
    """Return the encrypted version of message using encryption key, key.

    >>> encrypt("ABABABCSBHFS", "ZAP")
    "ACQBB RCTRH GI"

    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    # Filter out all non-letter characters from message and key.
    message = char_filter(message)
    key = char_filter(key)

    if len(message) == 0:
        print("\nYour message is empty.\n")
        return

    elif len(key) == 0:
        print("\nYour key is empty.\n")
        return

    print("\nYour message is: {}.".format(message))
    print("Your key is {}.\n".format(key))

    encrypted_message = ""

    # Iterate through the string key to encrypt the message.
    key_counter = 0

    for i in range(len(message)):
        # Spaces should simply be added to the encrypted message.
        if message[i] == " ":
            encrypted_message += " "
            continue

        # Rptate back to the first index of the key.
        if key_counter == len(key):
            key_counter = 0

        if key[key_counter] == " ":
            key_counter += 1

        curr_msg_char = ord(message[i])

        # The magnitube of the character shift is the letter's alphabet spot.
        key_convert = ord(key[key_counter]) - ENCRYPTION_CONVERSION

        # Ensure that the encrypted character does not become a non-letter.
        if chr(curr_msg_char + key_convert) > "Z":
            curr_msg_char -= ASCII_CONVERSION

        new_msg_char = chr(curr_msg_char + key_convert)

        encrypted_message += new_msg_char

        key_counter += 1

    return encrypted_message


def decrypt(message: str, key: str) -> str:
    """Return the decrypted version of message using encryption key, key.

    >>> decrypt("ABCDEFGHIJKLMNOP", "ABCD")
    "ZZZZD DDDHH HHLLL L" 
    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    # Filter out all non-letter characters from message and key.
    message = char_filter(message)
    key = char_filter(key)

    if len(message) == 0:
        print("\nYour message is empty.\n")
        return

    elif len(key) == 0:
        print("\nYour key is empty.\n")
        return

    print("\nYour message is: {}.".format(message))
    print("Your key is {}.\n".format(key))

    decrypted_message = ""

    # Iterate through the string key to encrypt the message.
    key_counter = 0

    for i in range(len(message)):
        # Spaces should simply be added to the encrypted message.
        if message[i] == " ":
            decrypted_message += " "
            continue

        # Rptate back to the first index of the key.
        if key_counter == len(key):
            key_counter = 0

        if key[key_counter] == " ":
            key_counter += 1

        curr_msg_char = ord(message[i])

        # The magnitube of the character shift is the letter's alphabet spot.
        key_convert = ord(key[key_counter]) - ENCRYPTION_CONVERSION

        # Ensure that the encrypted character does not become a non-letter.
        if chr(curr_msg_char - key_convert) < "A":
            curr_msg_char += ASCII_CONVERSION

        new_msg_char = chr(curr_msg_char - key_convert)

        decrypted_message += new_msg_char

        key_counter += 1

    return decrypted_message


def generate_key(length: int) -> str:
    """Return a string with length random characters. All letters will be
    captialized and spaced in chunks of 5 letters.

    >>> generate_key(10) 
    HSJEH SJACW
    """

    random_key = ""

    for i in range(length):
        random_key += chr(randint(65, 90))

    # Change key into proper format of 5 character chunks.
    random_key = char_filter(random_key)
    return random_key


def determine_key(msg: str, encrypted_msg: str):
    """Print the encryption key from the initial message, msg, and 
    the encrypted message, encrypted_msg. """

    msg = char_filter(msg)
    encrypted_msg = char_filter(encrypted_msg)

    if len(msg) == 0:
        print("\nYour message is empty.\n")
        return

    elif len(encrypted_msg) == 0:
        print("\nYour encrypted message is empty.\n")
        return

    elif len(msg) != len(encrypted_msg):
        print("\nYour message and encrypted message must be the same length.")
        return
    
    else: 
        print("\nYour unencrypted message is: {}".format(msg))
        print("Your encrypted message is: {}".format(encrypted_msg))

    ALPHABET_LENGTH = 26
    ASCII_CONVERSION = 64

    key = ""

    # Message and encrypted_message should be the same length.
    for i in range(len(msg)):
        if msg[i] == " ":
            continue

        # Figure out the size of the letter shift.
        letter_shift = ord(encrypted_msg[i]) - ord(msg[i])

        # Rotate to end of the alphabet.
        if letter_shift < 1:
            letter_shift = ALPHABET_LENGTH - abs(letter_shift)

        key += chr(letter_shift + ASCII_CONVERSION)

    key = shortest_repeating_substring(key)
    print("The encryption key used is: {}".format(key))


def shortest_repeating_substring(string: str) -> str:
    """Return the shortest repeating substring in string.

    >>> shortest_repeating_substring("AAAAAA") 
    A

    >>> shortest_repeating_substring("ABCABCABCAB")
    ABC
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
                # Check remaining letters for partial occurence of the substring.
                shortest_substring = curr_substring
                is_matching = True

                substring_index = 0

                for i in range(end_index, length):
                    if not(shortest_substring[substring_index] == string[i]):
                        is_matching = False

                    else: 
                        # Iterate through the characters in shortest_substring.
                        substring_index += 1

                if is_matching:
                    # Key should be given in chunks of 5 characters. 
                    key = ""
                    
                    for i in range(len(shortest_substring)): 
                        if i % 5 == 0 and i != 0: 
                            key += " "
                        
                        key += shortest_substring[i]
                            
                    return key


def main():
    while True:
        print("\n1. Encrypt. \n2. Decrypt. \n3. Generate Key. \n4. Guess Key. \n5. Exit")
        program = input("\n> ")
        print()

        if program == "1":
            message = input("Enter a message to encrypt: ")
            key = input("Enter a key to decrypt with: ")

            print("The encrypted message is: {}.".format(encrypt(message, key)))

        elif program == "2":
            message = input("Enter a message to decrypt: ")
            key = input("Enter a key to decrypt with: ")

            print("The decrypted message is: {}.".format(decrypt(message, key)))

        elif program == "3":
            try:
                length = int(input("Enter the length of the desired key: "))
                print(generate_key(length))
            except ValueError:
                print("Invalid input...\n")

        elif program == "4":
            message = input("Enter the unencrypted message: ")
            encrypted_message = input("Enter the encrypted message: ")

            determine_key(message, encrypted_message)

        else:
            print("Good bye.\n")
            break


if __name__ == "__main__":
    main()
