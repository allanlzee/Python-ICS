from fractions import Fraction 


def get_coefficients() -> list: 
    # Remove leading and trailing whitespace and separate coefficients.
    input_coefficients = input("coefficients: ").strip().split(" ")

    coefficients = [] 

    # Ensure that all coefficients are integers.
    for num in input_coefficients: 
        try: 
            coefficients.append(int(num))
        except ValueError: 
            print("Invalid input, one of the coefficients is not an integer.")
            print()
            return None 

    return coefficients 


def remove_leading_zeros(coefficients: list) -> list: 
    """Remove leading zeros from the list coefficients."""

    index = 0 
    
    while coefficients[index] == 0: 
        index += 1 

    return coefficients[index:]



def get_degree(coefficients: list) -> int: 
    """Return the degree of the polynomial represented by integer coefficients
    in list coefficients."""
    
    # Calculate the degree of the polynomial. Note that the last 
    # coefficient represents a constant. 
    degree = len(coefficients) - 1

    return degree 


def determine_polynomial(coefficients: list, degree: int) -> str: 
    
    polynomial = "" 

    negative_coefficient = False 

    coefficients = remove_leading_zeros(coefficients) 

    for index in range(len(coefficients)): 
        # There is no term to add to the polynomial.
        if coefficients[index] == 0: 
            degree -= 1
            continue 
        
        # Add the constant term without any x variable.
        if degree == 0: 
            polynomial += str(coefficients[index])
            continue
        
        # If the coefficient is 1, it does not have to be included.
        if coefficients[index] != 1: 
            polynomial += str(coefficients[index])

        # Add the variable x and exponents to the polynomial.
        # degree != 1 ensures that there is no trailing + sign.
        if index != len(coefficients) - 1 and degree != 1: 
            polynomial += "x^" + str(degree) + " + "
        
        # The term with x to the power of 1 does not require an exponent.
        elif degree == 1: 
            polynomial += "x + "

        degree -= 1
        
    return polynomial


def determine_possible_factors(coefficients: list) -> list: 

    leading_co = coefficients[len(coefficients) - 1] 
    constant = coefficients[0] 

    # Calculate all possible factors using leading_co / constant.


def find_linear_factors(): 
    pass 


def main_menu(): 
    print("Factor Theorem")
    print("_" * len("Factor Theorem"))
    
    print("Finds all the linear factors of a polynomial " + 
        "(degree 2 or greater) with integer coefficients. " +
        "Enter the coefficients in order of descending power, " +
        "separated by spaces.\n")

    coefficients = None 

    while coefficients == None: 
        coefficients = get_coefficients()

    coefficients = remove_leading_zeros(coefficients)

    poly_degree = get_degree(coefficients)

    print("\nThe polynomial has degree {}.".format(poly_degree))

    polynomial = determine_polynomial(coefficients, poly_degree)

    print("\nThe polynomial is: f(x) = {}.".format(polynomial))

if __name__ == "__main__": 
    main_menu() 

