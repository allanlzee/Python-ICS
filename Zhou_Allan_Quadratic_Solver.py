# Quadratic Solver
# Solves for the roots of the standard quadratic equation, ax² + bx + c = 0    #
# using the quadratic formula to solve for the roots and the discriminant to 
# determine the number of roots the equation has.
# Author: Allan Zhou 

from math import sqrt 

print("QUADRATIC SOLVER")

# Until run == 'n', the program will keep running. 
run = "y"

while run == "y" or run == "yes": 
    print("\nEnter the values of a, b, and c from a quadratic equation", \
    "ax² + bx + c = 0:")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print()

    # Calculate the discriminant using b² - 4ac. If it is greater than 0, 
    # there will be 2 real roots. If it is equal to 0, there is 1 real root.
    # Otherwise, there are no real roots. 

    discriminant = b ** 2 - 4 * a * c 

    if discriminant > 0: 
        print("There are two solutions.")
        # The quadratic formula with a discriminant greater 0 has two roots: 
        # -b + sqrt(b**2 - 4*a*c) / (2 * a) 
        # -b - sqrt(b**2 - 4*a*c) / (2 * a)
        first_root = (-b + sqrt(discriminant)) / (2 * a)
        second_root = (-b - sqrt(discriminant)) / (2 * a)

        print("The roots are {:.2f} and {:.2f}."
            .format(first_root, second_root))

    elif discriminant == 0: 
        print("There is one solution.")

        # The quadratic formula with a discriminant of 0 returns one root, 
        # -b / (2 * a) 
        first_root = -b / (2 * a) 
        print("The root is {:.2f}.".format(first_root))

    else: 
        # When the discriminant is negative, we get an imaginary root. 
        print("There are no (real) solutions.")

    run = input("\nAnother? (y)es or (n)o: ")

print("\nThanks for using QUADRATIC SOLVER.\nGood-bye!\n")