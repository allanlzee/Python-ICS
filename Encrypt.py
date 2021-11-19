""""Encrypt, decrypt, generate a key, and guess the encyrption key."""

__author__ = "Allan Zhou" 


from random import randint 


def char_filter(message: str) -> str: 
    """Filters out all non-letter characters from message, which is a string
    with letters that have all been capitalized.
    
    >>> char_filter("IIIHDHSN&(#^@*")
    IIIHD HSN

    """

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

    Your message is: ABABA BCSBH FS.
    Your key is ZAP.

    The encrypted message is: ACQBB RCTRH GI.

    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    # Filter out all non-letter characters from message and key.
    message = char_filter(message.upper())
    key = char_filter(key.upper()) 

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

    Your message is: ABCDE FGHIJ KLMNO P.
    Your key is ABCD.

    The decrypted message is: ZZZZD DDDHH HHLLL L.
    """

    ASCII_CONVERSION = 26
    ENCRYPTION_CONVERSION = 64

    # Filter out all non-letter characters from message and key.
    message = char_filter(message.upper())
    key = char_filter(key.upper())

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
        # Space out key characters in chunks of 5. 
        if i % 5 == 0 and i != 0: 
            random_key += " "

        random_key += chr(randint(65, 90)) 


    return random_key


def determine_key(message: str, encrypted_message: str) -> str: 
    """Determine the encryption key from the initial message, message, and 
    the encrypted message, encrypted_message. """

    message = char_filter(message.upper())
    encrypted_message = char_filter(encrypted_message.upper()) 

    if len(message) != len(encrypted_message):
        print("\nInvalid arguments were passed. Please try again.")
        return

    ALPHABET_LENGTH = 26
    ASCII_CONVERSION = 64

    key = ""

    # message and encrypted_message should be the same length. 
    for i in range(len(message)): 
        if message[i] == " ": 
            key += " "
            continue

        # Figure out the size of the letter shift. 
        letter_shift = ord(encrypted_message[i]) - ord(message[i])

        if letter_shift < 1: 
            letter_shift = ALPHABET_LENGTH - letter_shift 

        key += chr(letter_shift + ASCII_CONVERSION)
    
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

            if determine_key(message, encrypted_message) != None: 
                print("The encryption key is: {}.".format(determine_key(message, encrypted_message))) 
                
            else: 
                print("There is no encryption key possible.")

        else:
            print("Good bye.\n")
            break 


if __name__ == "__main__":
    main()
