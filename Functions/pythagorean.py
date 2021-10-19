def pythagorean(max_length): 
    """Prints all Pythagorean triples where the longest member is
    less than or equal to max_length. 
    Time Complexity: O(n^3)"""

    for c in range(1, max_length + 1): 
        hyp_squared = c**2

        # Find triangle legs that satisfy a^2 + b^2 = c^2
        # Find all possible combinations of a and b. 
        for b in range(1, c): 
            for a in range(1, b + 1): 

                # Valid Pythagorean Triple. 
                if a**2 + b**2 == hyp_squared: 

                    # Do not print repeats. If a and b have a common 
                    # divisor greater than 1, it will be a multiple of a 
                    # previous triple. 

                    for div in range(2, c): 
                        if a % div == 0 and b % div == 0: 
                            break

                        # There are no common divisors. 
                        elif div == c - 1: 
                            print("({}, {}, {})".format(a, b, c))

    print()

                
n = int(input("Enter a positive integer: "))
pythagorean(n)
