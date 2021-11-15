def letter_distribution(string: str): 
    """Analyze a string entered by the user and collect statistics about what 
    letters (A-Z) appear in the string and how often.
    
    >>> letter_distribution("speedway stadium")
    Frequency of Letters 
    
    Character | Count | Frequency 
    -----------------------------
    S         | 2     |  13.3%
    P         | 1     |  6.7%
    E         | 2     |  13.3%
    D         | 2     |  13.3%
    W         | 1     |  6.7%
    A         | 2     |  13.3%
    Y         | 1     |  6.7%
    T         | 1     |  6.7%
    I         | 1     |  6.7%
    U         | 1     |  6.7%
    M         | 1     |  6.7%

    Mode: S, E, D, A
    Percentage Vowels: 40% 

    """

    ASCII_CONVERSION = 65
    ALPHABET_LENGTH = 26 
    VOWELS = ['A', 'E', 'I', 'O', 'U']

    # Convert all characters in string to uppercase. 
    string = string.upper() 

    # Array to check which letters are present in the string. 
    used_chars = [False] * 26

    # Array to track frequencies of each letter.
    chars_count = [0] * 26

    # Array to hold letters that occur the most often. 
    mode_letters = []

    num_chars = 0
    num_vowels = 0

    # Track the value of the mode based on the array chars_count.
    mode = -1

    for char in string: 
        if 'A' <= char <= 'Z': 
            num_chars += 1 
            index = ord(char) - ASCII_CONVERSION

            # Letter has been used.
            used_chars[index] = True
            chars_count[index] += 1

            if chars_count[index] > mode: 
                mode = chars_count[index]

            if char in VOWELS: 
                num_vowels += 1

    print("Frequency of Letters\n")
    print("Character | Count | Frequency")

    for i in range(len(used_chars)): 

        # If the character is in the string.
        if used_chars[i]: 

            # Find the character, the number of times it appears, 
            # and its percentage frequency in the string. 
            char = chr(i + ASCII_CONVERSION)
            count = chars_count[i]
            freq = round(chars_count[i] / num_chars * 100, 2) 

            print("{:{width_char}} | {:{width_count}} | {:{width_freq}}%"
                .format(char, count, freq, width_char = len("Character"), 
                width_count = len("Count"), width_freq = len("Frequency") - 1))

    # If the character count of a character matches 
    # the value mode, it is a mode letter.
    for i in range(ALPHABET_LENGTH): 
        if chars_count[i] == mode: 
            mode_letters.append(chr(i + ASCII_CONVERSION))

    print("\nMode(s): ", end='')
    for letter in mode_letters: 
        print(letter, end=" ")

    print("\nPercentage of Vowels: {}% ({} vowels)\n".format(round(num_vowels / num_chars * 100, 2), num_vowels))


letter_distribution("speedway stadium")