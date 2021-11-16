"""Pair Programming Assignment"""

__author__ = "Allan Zhou, Daniel Hong"

from math import sqrt


def birthday(bday: int, bmonth: int, day: int, month: int):
    """Take in the birthday month and day and the current month               
    and day from the user and print a message accordingly. 

    >>> birthday()
    Enter your birth day: 5
    Enter your birth month: 12
    Enter today's day: 16
    Enter today's month: 11
    Your birthday is approaching. Happy early birthday!
    """
   
    if month == bmonth:
        if day == bday:
            birthday_time = "is today"
            greeting = ""
    
        elif day < bday:
            birthday_time = "is approaching"
            greeting = "early "
            
        else:
            birthday_time = "has passed"
            greeting = "belated "
            
    elif month < bmonth:
        birthday_time = "is approaching"
        greeting = "early "

    else:
        birthday_time = "has passed"
        greeting = "belated "

    print("Your birthday {}. Happy {}birthday!\n"
        .format(birthday_time, greeting))


def leap_year(year: int):
    """Determine if a year given by the user is a leap year.

    >>> leap_year() 

    Enter a year: 2005
    The year 2005 is not a leap year.
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = "a"
            else: 
                leap = "not a"
        else: 
            leap = "a"
    else:
        leap = "not a"


    print("The year {} is {} leap year.\n".format(year, leap))

   
def line_segment():
    """Print the length of the line segment.

    >>> line_segment()
    Enter the coordinates of two points.

    Point 1 x-value: 1
    Point 1 y-value: 3
    Point 2 x-value: 3
    Point 2 y-value: 7

    Your points are (1.0, 3.0) and (3.0, 7.0).

    The slope of the line segment is 2.00.
    The length of the line segment is 4.47.
    """

    print("Enter the coordinates of two points.\n")

    x1 = float(input("Point 1 x-value: "))
    y1 = float(input("Point 1 y-value: "))
    x2 = float(input("Point 2 x-value: "))
    y2 = float(input("Point 2 y-value: "))

    print("\nYour points are ({}, {}) and ({}, {}).\n".format(x1, y1, x2, y2))

    if x2 - x1 == 0: 
        print('The slope is undefined.')
    else: 
        if x2 > x1: 
            slope = (y2 - y1) / (x2 - x1)
        else: 
            slope = (y1 - y2) / (x1 - x2)

        print('The slope of the line segment is {:.2f}.'.format(slope))

    length = sqrt((y2 - y1)**2 + (x2 - x1)**2)
    print('The length of the line segment is {:.2f}.'.format(length))

    print()


def letter_distribution(string: str): 
    """Analyze a string entered by the user and collect statistics about what 
    letters (A-Z) appear in the string and how often.
    
    >>> letter_distribution("speedway stadium")

    Frequency of Letters

     -------------------------------
    | Character | Count | Frequency |
     -------------------------------
    | A         | 2     | 13.33   % |
    | D         | 2     | 13.33   % |
    | E         | 2     | 13.33   % |
    | I         | 1     | 6.67    % |
    | M         | 1     | 6.67    % |
    | P         | 1     | 6.67    % |
    | S         | 2     | 13.33   % |
    | T         | 1     | 6.67    % |
    | U         | 1     | 6.67    % |
    | W         | 1     | 6.67    % |
    | Y         | 1     | 6.67    % |
     -------------------------------

    Mode(s): A D E S (each appears 2 time(s))

    Percentage of Vowels: 40.0% (6 vowels)
    """

    ASCII_CONVERSION = 65
    ALPHABET_LENGTH = 26 
    VOWELS = ['A', 'E', 'I', 'O', 'U']

    # Convert all characters in string to uppercase. 
    string = string.upper() 

    # Array to check which letters are present in the string. 
    used_chars = [False] * ALPHABET_LENGTH

    # Array to track frequencies of each letter.
    chars_count = [0] * ALPHABET_LENGTH

    # Array to hold letters that occur the most often. 
    mode_letters = []

    num_chars = 0
    num_vowels = 0

    # Track the value of the mode based on the array chars_count.
    mode = 0

    for char in string: 
        if 'A' <= char <= 'Z': 
            num_chars += 1 
            index = ord(char) - ASCII_CONVERSION

            # Letter has been used in the string.
            used_chars[index] = True
            chars_count[index] += 1

            # Tracks the value of the mode. 
            if chars_count[index] > mode: 
                mode = chars_count[index]

            if char in VOWELS: 
                num_vowels += 1

    print("\nFrequency of Letters\n")

    # Print the table of statistics.
    print(" " + "-" * len(" Character | Count | Frequency "))
    print("| Character | Count | Frequency |")
    print(" " + "-" * len(" Character | Count | Frequency "))

    for i in range(ALPHABET_LENGTH): 
        # If the character is in the string.
        if used_chars[i]: 
            # Find the character, the number of times it appears, 
            # and its percentage frequency in the string. 
            char = chr(i + ASCII_CONVERSION)
            count = chars_count[i]
            freq = round(chars_count[i] / num_chars * 100, 2) 

            print("| {:<{w_char}} | {:<{w_count}} | {:<{w_freq}}% |"
                .format(char, count, freq, w_char = len("Character"), 
                w_count = len("Count"), w_freq = len("Frequency") - 1))

    print(" " + "-" * len(" Character | Count | Frequency "))

    # If the character count of a character matches 
    # the value mode, it is a mode letter.
    for i in range(ALPHABET_LENGTH): 
        if chars_count[i] == mode: 
            mode_letters.append(chr(i + ASCII_CONVERSION))

    print("\nMode(s): ", end='')
    for letter in mode_letters: 
        print(letter, end=' ')
    print("(each appears {} time(s))".format(mode))

    print("\nPercentage of Vowels: {}% ({} vowels)\n"
        .format(round(num_vowels / num_chars * 100, 2), num_vowels))


def main():
    """Runs all the functions in the module."""

    while True:
        program = input("Birthday (b), Leap Year (ly), " 
            + "Line Segment (ls), or Letter Distribution (ld): ")
        print()

        if program == "b":
            bday = int(input('Enter your birth day: '))
            bmonth = int(input('Enter your birth month: '))
            day = int(input("Enter today's day: "))
            month = int(input("Enter today's month: "))
            birthday(bday, bmonth, day, month)

        elif program == "ly": 
            year = int(input('Enter a year: '))
            leap_year(year)

        elif program == "ls":
            line_segment() 

        elif program == "ld": 
            string = input("Enter a word to analyze: ")
            letter_distribution(string)

        else: 
            print("Good bye.")
            break


if __name__ == "__main__": 
    main()
