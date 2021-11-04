"""Questions using the library random.

random.random() -> returns a float between 0.0 and 1.0.

random.randrange(start, stop, step) -> returns a number between 
start and stop, with an incrementation of step. 

"""

__author__ = "Allan Zhou"


import random


def random_even(): 
    """Return a random even integer between 1 and 1000."""
    
    rand_int = random.randrange(2, 1000, 2)
    return rand_int 


def multiple_seven(): 
    """Return a random multiple of 7 between 1 and 1000.""" 

    rand_int = random.randrange(7, 1000, 7) 
    return rand_int  


def random_floats(x: int, y: int): 
    """Print 10 random floating-point numbers between x and y, excluding y."""

    for i in range(10): 
        rand_int = (random.random() * abs(y - x)) + x 
        print(rand_int)


def number_guessing(lower_bound: int, upper_bound: int): 
    """A number guessing game, where the user guesses numbers between 
    a and b. The program provides a hint as to whether the guess is low 
    or high. Once the user has guessed TOTAL_GUESSES guesses, the program 
    stops and prints the correct number."""

    TOTAL_GUESSES = 3 

    print("I'm thinking of a number between 1 and 10.")
    number = random.randint(1, 10)

    for i in range(TOTAL_GUESSES): 
        guess = int(input('Enter a guess: '))
        if guess == number:
            print('\nCorrect! The number was {}.'.format(number))
            return 
        elif guess < number:
            print('The number is higher.')
        else: 
            print('The number is lower.')

    print("\nYou have no more guesses. \nThe number was {}.".format(number))


def dice_roll(): 
    """Roll the die to get a value from 1 to 6. Keep rolling until 
    you get the same value and count how many rolls it takes."""

    program = "y"

    while program == "y": 
        program = input("Would you like to play the dice game? (y)es or (n)o: ")

        first_roll = random.randint(1, 6) 

        num_rolls = 0 

        while True: 
            next_roll = random.randint(1, 6) 

            if next_roll == first_roll: 
                break 
            else: 
                num_rolls += 1 

        print("You get {} points.".format(num_rolls)) 

    print("Thanks for playing dice game.")


def computer_guessing(lower: int, upper: int): 
    """Guess the user's number using the binary search algorithm, with time
    complexity of O(log n). For the numbers 1 to 10, the algorithm should 
    take at most 4 guesses."""

    num_guesses = 0 
    lower_bound = lower
    upper_bound = upper

    user_number = int(input("Enter a number for the computer to guess: "))

    while True: 
        computer_number = (lower_bound + upper_bound) // 2 
        
        print("The computer guesses {}.".format(computer_number))
        num_guesses += 1 
        result = input("Is the computer's number (c)orrect, (h)igher, or (l)ower: ")

        if result == "c" or result == "correct": 
            print("\nI guessed your number in {} guess(es).".format(num_guesses))
            print("Your number was {}.".format(user_number))
            break
        elif result == "l" or result == "lower": 
            lower_bound = computer_number + 1
        else: 
            upper_bound = computer_number 


def main(): 
    # dice_roll()
    computer_guessing(1, 1000) 

if __name__ == "__main__": 
    main() 

