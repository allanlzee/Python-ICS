"""This program uses the Factor Theorem to find the linear factors of a 
polynomial entered by the user by calculating the degree and possible factors
for the polynomial."""


__author__ = "Allan Zhou"


from fractions import Fraction 


def get_user_choice() -> str: 
    """Return the user's choice between calculating linear factors (1) 
    or exiting the program (2)."""

    while True: 
        program = input("> ").strip()

        # Ensure user enters valid choice.
        if program == "1" or program == "2": 
            return program
        else: 
            print("Invalid choice. \n")


def get_coefficients() -> list: 
    """Get a string of polynomial coefficients from the user, separated by 
    spaces and return them as a list of integers. Ensure that the user enters
    valid coefficients. """

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
    
    # Find index of first non-zero integer in coefficients.
    while coefficients[index] == 0: 
        index += 1 

    return coefficients[index:]


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


def calculate_degree(coefficients: list) -> int: 
    """Return the degree of the polynomial represented by integer coefficients
    in list coefficients. Note that the last coefficient represents a constant. 
    
    >>> get_degree([1, 0, 1])
    2 
    >>> get_degree([1, 2, 7, 0])
    3
    """
    
    # Calculate the degree of the polynomial, which is the highest degree of 
    # all the monomial terms with non-zero coefficients. 
    degree = len(coefficients) - 1

    return degree 


def determine_polynomial(coefficients: list, degree: int) -> str: 
    """Print a polynomial represented by list coefficients.
    
    >>> determine_polynomial([1, 0, 7, 6, 2], 4) 
    x^4 + 7x^2 + 6x + 2

    >>> determine_polynomial([2, 3, -1, 0], 3)
    2x^3 + 3x^2 + -x 
    """
    
    polynomial = "" 

    # Remove leading and trailing zeros from the coefficients list.
    coefficients = simplify_polynomial(remove_leading_zeros(coefficients)) 

    for index in range(len(coefficients)): 
        current_coefficient = coefficients[index]

        # There is no term to add to the polynomial.
        if current_coefficient == 0:
            degree -= 1
            continue 
        
        # Add the constant term without any x variable.
        elif degree == 0: 
            polynomial += str(current_coefficient)
            break
        
        # If the coefficient is -1, it is represented by a - sign.
        elif current_coefficient == -1:
            polynomial += "-"

        # If the coefficient is 1, it does not have to be included.
        elif current_coefficient != 1:
            polynomial += str(current_coefficient)

        # Add the variable x and exponents to the polynomial.
        # nx^1 will be written as nx. 
        if index != len(coefficients) - 1 and degree > 1: 
            polynomial += "x^" + str(degree) + " + "
        
        # The polynomial ends with a non-constant term with an exponent 
        # greater than 1.
        elif degree > 1: 
            polynomial += "x^" + str(degree)

        # Deals with the term with an exponent of 1 (not as the last term). 
        elif index != len(coefficients) - 1: 
            polynomial += "x + "

        # The polynomial's last term is nx, where n is the coefficient.
        else: 
            polynomial += "x"

        degree -= 1
        
    return polynomial


def calculate_polynomial(coefficients: list, degree: int, 
                        input: Fraction) -> Fraction: 
    """Calculate the value of the polynomial represented by coefficients
    when x is equal to input. 

    >>> calculate_polynomial([6, -17, 11, -2], 3, Fraction(1, 3))
    0

    >>> calculate_polynomial([6, -17, 11, -2], 3, Fraction(1, 6))
    -11/18
    """

    polynomial_value = 0 

    for num in coefficients: 
        polynomial_value += num * input ** degree 
        degree -= 1 

    return polynomial_value


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

    # Find all factors of constant and leading. 
    for constant_factor in range(1, constant + 1): 
        if constant % constant_factor != 0: 
            continue

        for leading_factor in range(1, leading + 1): 
            if leading % leading_factor != 0: 
                continue
            
            # Possible factor p/q, where p divides into the polynomial
            # constant and q divides into the leading coefficient.
            factor = Fraction(constant_factor, 
                leading_factor).limit_denominator()

            # Prevent duplicates of possible factors. 
            if factor not in possible_factors: 
                possible_factors.append(factor)
                possible_factors.append(-factor)

    return possible_factors


def format_linear_factor(x_coefficient: int, constant: int, add=True) -> str: 
    """Return the linear factor, qx - p, as a string, given x_coefficient for 
    q and constant for p, which is never passed as 0.
    
    >>> format_linear_factor(2, 1) 
    2x + 1

    >>> format_linear_factor(-3, 1, False) 
    -3x - 1
    """

    # constant is negative, linear factor should have format qx + p.
    if add: 
        if x_coefficient != 1:
            linear_factor = str(x_coefficient) + "x + " + str(abs(constant))

        elif constant != 0:
            linear_factor = "x + " + str(abs(constant))

    # constant is positive, linear factor should have format qx - p.
    else: 
        if x_coefficient != 1:
            linear_factor = str(x_coefficient) + "x - " + str(constant)

        elif constant != 0: 
            linear_factor = "x - " + str(constant)

    return linear_factor


def determine_linear_factors(coefficients: list, degree: int, factored=False): 
    """Calculate the value of the polynomial represented by coefficients for
    each of its possible factors. Find all the linear factors for the 
    polynomial and print them."""
    
    possible_factors = determine_possible_factors(coefficients)

    linear = [] 

    print("\nComputations")

    # If x^n has been factoed out of the polynomial, x will be a factor.
    if factored: 
        linear.append(0) 
        print("f(0) = 0")

    # Print each of the values of the polynomial with the input of its 
    # possible factor. 
    for factor in possible_factors: 
        value = calculate_polynomial(coefficients, degree, factor)

        print("f({}) = {}".format(factor, value))

        if value == 0: 
            linear.append(factor)

    print("\nResults")

    if len(linear) == 0:
        print("The polynomial has no linear factors.\n")
        return
    else:
        print("The polynomial has linear factors: ")

    linear_factors = [] 

    for factor in linear: 
        # The linear factor qx - p comes from p/q, where f(p/q) = 0.
        x_coefficient = factor.denominator
        constant = factor.numerator

        # Linear factor will have form qx + p. 
        if factor > 0: 
            linear_factor = format_linear_factor(x_coefficient, constant, False)

        # Linear factor will have form qx - p. 
        elif factor < 0: 
            linear_factor = format_linear_factor(x_coefficient, constant)

        else:
            linear_factor = "x"

        linear_factors.append(linear_factor)

    # Print all linear factors, separated by commas. 
    for i in range(len(linear_factors) - 1): 
        print(linear_factors[i] + ", ", end = "")
        
    # Print the last linear factor without a trailing comma.
    print(linear_factors[-1] + "\n")
        

def main_menu(): 
    """The main menu for the Factor Theorem program."""

    print("Factor Theorem")
    print("-" * len("Factor Theorem"))
    
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

        # x^n is factored out of the polynomial to use the Factor Theorem.
        if trailing_zeros(coefficients): 
            coefficients = simplify_polynomial(coefficients)
            determine_linear_factors(coefficients, poly_degree, True)

        else: 
            determine_linear_factors(coefficients, poly_degree)


if __name__ == "__main__": 
    main_menu() 
