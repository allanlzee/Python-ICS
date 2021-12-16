"""This program uses the Factor Theorem to find the linear factors of a 
polynomial entered by the user by calculating the degree and possible factors
for the polynomial."""


__author__ = "Allan Zhou"


from fractions import Fraction 


def get_user_choice() -> str: 
    """Return the user's choice between calculating linear factors (1) 
    or exiting the program (2)."""

    while True: 
        try:
            program = input("> ").strip()
            if program == "1" or program == "2": 
                break
            else: 
                print("Invalid choice. \n")
        except ValueError: 
            print("Invalid input. \n")

    return program


def get_coefficients() -> list: 
    """Get a string of polynomial coefficients from the user, separated by 
    spaces and return them as a list of integers. Ensure that the user enters
    valid coefficients."""

    # Remove leading and trailing whitespace and separate coefficients.
    input_coefficients = input("Coefficients: ").strip().split(" ")

    coefficients = [] 

    # Ensure that all coefficients are integers.
    for num in input_coefficients: 
        try: 
            coefficients.append(int(num))
        except ValueError: 
            print("Invalid input, all coefficients must be integers.")
            print()
            return None 

    return coefficients 


def remove_leading_zeros(coefficients: list) -> list: 
    """Remove leading zeros from the list coefficients and return the 
    new list.
    
    >>> remove_leading_zeros([0, 0, 0, 1, 1])
    [1, 1]

    >>> remove_leading_zeros([0, 1, 2, 7, 0])
    [1, 2, 7, 0]
    """

    index = 0 
    
    while coefficients[index] == 0: 
        index += 1 

    return coefficients[index:]


def calculate_degree(coefficients: list) -> int: 
    """Return the degree of the polynomial represented by integer coefficients
    in list coefficients.
    
    >>> get_degree([1, 0, 1])
    2 
    >>> get_degree([1, 2, 7, 0])
    3
    """
    
    # Calculate the degree of the polynomial. Note that the last 
    # coefficient represents a constant. 
    degree = len(coefficients) - 1

    return degree 


def determine_polynomial(coefficients: list, degree: int) -> str: 
    """Print a polynomial with coefficients coefficients and degrees.
    
    >>> determine_polynomial([1, 0, 7, 6, 2], 4) 
    x^4 + 7x^2 + 6x + 2

    >>> determine_polynomial([2, 3, 1, 0], 3)
    2x^3 + 3x^2 + x 
    """
    
    polynomial = "" 

    coefficients = simplify_polynomial(remove_leading_zeros(coefficients)) 

    for index in range(len(coefficients)): 
        # There is no term to add to the polynomial.
        if coefficients[index] == 0: 
            degree -= 1
            continue 
        
        # Add the constant term without any x variable.
        elif degree == 0: 
            polynomial += str(coefficients[index])
            break
        
        # If the coefficient is 1, it does not have to be included.
        elif coefficients[index] != 1: 
            polynomial += str(coefficients[index])

        # Add the variable x and exponents to the polynomial.
        # degree > 1 ignores the term with x^1 and constants.
        if index != len(coefficients) - 1 and degree > 1: 
            polynomial += "x^" + str(degree) + " + "
        
        # The polynomial ends with a non-constant term.
        elif degree > 1: 
            polynomial += "x^" + str(degree)

        # Deals with the term with an exponent of 1 (not as the last term). 
        elif index != len(coefficients) - 1: 
            polynomial += "x + "

        degree -= 1
        
    return polynomial


def calculate_polynomial(coefficients: list, input: Fraction) -> Fraction: 
    """Calculate the value of the polynomial represented by coefficients
    when x is equal to input. 

    >>> calculate_polynomial([6, -17, 11, -2], 3, Fraction(1, 3))
    0

    >>> calculate_polynomial([6, -17, 11, -2], 3, Fraction(1, 6))
    -11/18

    >>> calculate_polynomial([6, -17, 11, -2], 3, Fraction(2))
    0
    """

    polynomial_value = 0 
    degree = calculate_degree(coefficients)

    for num in coefficients: 
        polynomial_value += num * input ** degree 
        degree -= 1 

    return polynomial_value


def trailing_zeros(coefficients: list) -> bool: 
    """Return True if the list of coefficients has trailing zeros, meaning
    that x^n (n >= 1) can be factored out from the polynomial. Otherwise, 
    return False.
    
    >>> trailing_zeros([2, 5, 3, 0, 0]) 
    True
    """

    if coefficients[-1] == 0:
        return True 
    
    return False 


def simplify_polynomial(coefficients: list) -> list:
    """Factor out x^n from the polynomial represented by the list, 
    coefficients and return the factored list of coefficients.
    
    >>> simplify_polynomial([2, 5, 3, 0, 0])
    [2, 5, 3] 
    """ 

    last_term = -1

    while coefficients[last_term] == 0:
        last_term -= 1

    # Get the index of the last non-zero term.
    last_term = len(coefficients) + last_term

    return coefficients[:last_term + 1]


def determine_possible_factors(coefficients: list) -> list: 
    """Determine all possible factors p/q for the polynomial represented by
    coefficients. For p/q, p divides into the constant and p divides into the
    leading coefficient. 
    
    >>> determine_possible_factors([1, 2, 7, 0, 6]) 
    [1, -1, 2, -2, 3, -3, 6, -6]
    """

    leading = abs(coefficients[0])
    constant = abs(coefficients[-1])

    possible_factors = [] 

    for constant_factor in range(1, constant + 1): 
        if constant % constant_factor != 0: 
            continue

        for leading_factor in range(1, leading + 1): 
            if leading % leading_factor != 0: 
                continue

            factor = Fraction(constant_factor, 
                leading_factor).limit_denominator()

            if factor not in possible_factors: 
                possible_factors.append(factor)
                possible_factors.append(-factor)

    return possible_factors


def determine_linear_factors(coefficients: list): 
    """Calculate the value of the polynomial represented by coefficients for
    each of its possible factors. Find all the linear factors for the 
    polynomial and print them. 
    """
    
    possible_factors = determine_possible_factors(coefficients)

    linear = [] 

    print("\nComputations")

    for factor in possible_factors: 
        value = calculate_polynomial(coefficients, factor)

        print("f({}) = {}".format(factor, value))

        if value == 0: 
            linear.append(factor)

    print("\nResults")

    if len(linear) == 0:
        print("The polynomial has no linear factors.")
        return
    else:
        print("The polynomial has factors: ")

    linear_factors = [] 

    for factor in linear: 
        x_coefficient = factor.denominator
        constant = factor.numerator 

        if x_coefficient != 1: 
            linear_factor = str(x_coefficient) + "x + " + str(constant)
        else: 
            linear_factor = "x + " + str(constant)

        linear_factors.append(linear_factor)

    for i in range(len(linear_factors)): 
        if i != len(linear_factors) - 1: 
            print(linear_factors[i] + ", ", end = "")
        else: 
            print(linear_factors[i] + "\n")
        

def main_menu(): 
    print("Factor Theorem")
    print("_" * len("Factor Theorem"))
    
    print("Finds all the linear factors of a polynomial " + 
        "(degree 2 or greater) with integer coefficients. " +
        "Enter the coefficients in order of descending power, " +
        "separated by spaces.\n")

    while True: 
        print("1. Calculate linear factors of polynomial.\n" +
            "2. Exit.")

        program = get_user_choice()
        print()

        if program == "2": 
            print("Thanks for using Factor Theorem.")
            break 

        coefficients = None 

        while coefficients == None: 
            coefficients = get_coefficients()

        coefficients = remove_leading_zeros(coefficients)

        poly_degree = calculate_degree(coefficients)

        print("\nThe polynomial has a degree of {}.".format(poly_degree))

        polynomial = determine_polynomial(coefficients, poly_degree)

        print("\nThe polynomial is: f(x) = {}.".format(polynomial))

        if trailing_zeros(coefficients): 
            coefficients = simplify_polynomial(coefficients)

        determine_linear_factors(coefficients)


if __name__ == "__main__": 
    main_menu() 
