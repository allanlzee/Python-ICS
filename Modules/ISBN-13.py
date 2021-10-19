""" This program allows the user to calculate the weighted sum and check
the validity of an ISBN-13 number. Additionally, the function 
generate_check_digit() takes a 12 digit sequence and generates a check 
digit that makes the sequence a valid ISBN-13 number. """

__author__ = "Allan Zhou"

ISBN_SYSTEM = 13 

def clean(isbn): 
    """Return the ISBN-13 number that has been stripped of non-digits."""

    # Ensure that the argument is a string. 
    isbn = str(isbn)
    isbn_clean = ""

    # Only add digits to the filtered ISBN string. 
    for char in isbn: 
        if "0" <= char <= "9": 
            isbn_clean += char

    return isbn_clean


def calc_weighted_sum(isbn): 
    """Returns the ISBN-13 weighted sum of the passed argument."""

    isbn_clean = clean(isbn)
    isbn_total = 0

    for i in range(len(isbn_clean)): 
        # Even indices are added directly to the total.
        if i % 2 == 0: 
            isbn_total += int(isbn_clean[i])

        # Odd indices are first tripled and then added to the total. 
        else: 
            isbn_total += int(isbn_clean[i]) * 3 

    return isbn_total


def is_valid(isbn): 
    """"Return whether the number passed is a valid ISBN-13 number."""

    weighted_sum = calc_weighted_sum(isbn)

    # ISBN-13 numbers must be 13 digits in length. 
    if len(clean(isbn)) != 13:
        return False
    # If the weighted sum is divisible by 10, it is a valid ISBN-13 number.
    elif weighted_sum % 10 == 0: 
        return True 
    else: 
        return False 


def generate_check_digit(isbn): 
    """Return the digit that will make the passed 12-digit sequence a valid
    ISBN-13 number."""

    isbn_total = calc_weighted_sum(isbn) 

    # Find the digit that makes the weighted sum of the 12 digits divisible 
    # by 10. Note that the last indice is 12, so the value is not tripled.
    check_digit = str((10 - isbn_total % 10) % 10)

    return check_digit


def main(): 
    print("\nISBN-13 PROGRAM")

    while True: 
        user_input = input("\nHi there! Would you like to " +  
            "(v)erify or (g)enerate an ISBN-13 Number?")

        if user_input == "v" or user_input == "verify": 
            isbn_initial = input("Enter a 13 digit ISBN-13 number: ")
            
            result = is_valid(isbn_initial)

            if result: 
                print("\nThis is a valid ISBN-13 number.")
            else: 
                print("\nThis is not a valid ISBN-13 number.")
        
        elif user_input == "g" or user_input == "generate": 
            # Ensure the input is 12 digits long.
            while True: 
                isbn_initial = input("Enter a 12 digit number: ")

                if len(isbn_initial) != 12: 
                    print("This is not a valid input. Please try again.\n")

                else:
                    break

            check_digit = generate_check_digit(isbn_initial)
            print("The check digit is {}. The valid ISBN-13 is {}{}."
                .format(check_digit, isbn_initial, check_digit))

        else: 
            print("Thanks for using ISBN-13 program. Bye!\n")
            break 


if __name__ == "__main__": 
    main() 
