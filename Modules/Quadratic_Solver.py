"""This program allows the user to find the different 
features of the standard quadratic equation ax² + bx + c = 0.
There are functions to calculate the discriminant, b² - 4ac,
the number of solutions, and the roots."""

__author__ = "Allan Zhou" 

from math import sqrt 

def discriminant(a, b, c): 
    """Calculate the discriminant, b² - 4ac, where a, b, and c
    are floats; return the value."""\

    a = get_float(a)
    b = get_float(b)
    c = get_float(c)

    d = b**2 - 4*a*c 

    return d 


def num_solutions(a, b, c): 
    """Return the number of solutions that a standard quadratic 
    equation has."""

    discrim = discriminant(a, b, c)

    # The quadratic formula with a discriminant greater than 0 has two 
    # distinct roots: -b + √(b² - 4ac) / (2a) and -b - √(b² - 4ac) / (2a)
    if discrim > 0: 
        solutions = 2 

    # The quadratic formula with a discriminant of 0 returns one root, 
    # -b / (2a), since the square root of 0 is 0. 
    elif discrim == 0: 
        solutions = 1

    # When the discriminant is negative, we get imaginary roots, 
    # which returns a math domain error in Python. 
    else: 
        solutions = 0 

    return solutions 


def solve(a, b, c): 
    """Solve for the roots of a quadratic equation and print the 
    roots."""

    a = get_float(a)
    b = get_float(b)
    c = get_float(c)

    discrim = discriminant(a, b, c)
    solutions = num_solutions(a, b, c)

    if solutions == 2: 
        first_root = (-b + sqrt(discrim)) / (2 * a)
        second_root = (-b - sqrt(discrim)) / (2 * a)
        print("The two solutions are {:.2f} and {:.2f}.".format(
            first_root, second_root))

    elif solutions == 1: 
        first_root = -b / (2 * a) 
        print("The root is {:.2f}.".format(first_root))

    else: 
        print("There are no real solutions.")


def get_float(str): 
    """Return the float value of a string argument."""

    return float(str)


def main(): 
    print("QUADRATIC SOLVER\n")
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")
    c = input("Enter the value of c: ")

    print("\nThe discriminant is {}.".format(discriminant(a, b, c)))
    print("\nThere are {} roots.".format(num_solutions(a, b, c)))
    solve(a, b, c)


if __name__ == "__main__": 
    main() 
    