def pythagorean(max_length): 
    """Prints all Pythagorean triples where the longest member is
    less than or equal to max_length. 
    Time Complexity: O(n^4), where n is c."""

    for c in range(1, max_length + 1): 
        hyp_squared = c**2

        # Find triangle legs that satisfy a^2 + b^2 = c^2
        # Find all possible combinations of a and b. 
        for b in range(1, c): 
            for a in range(1, b + 1): 
                # Triple satisfies a^2 + b^2 = c^2. 
                if a**2 + b**2 == hyp_squared:
                    multiple_check(a, b, c)


def multiple_check(a, b, c): 
    """Checks if a Pythagorean triple is a multiple of a lower triple.""" 

    # If a and b have a common divisor greater than 1, it 
    # will be a multiple of a previous triple. 
    for div in range(2, c):

        # Common divisor with a and b, do not print triple.
        if a % div == 0 and b % div == 0: 
            break

        # There are no common divisors after all tests. 
        elif div == c - 1: 
            print("({}, {}, {})".format(a, b, c))


n = int(input("Enter a positive integer: "))
pythagorean(n)
