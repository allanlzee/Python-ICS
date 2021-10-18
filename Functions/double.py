from math import pi

def double_num(x): 
    """Print the doubled number.""" 
    print(x * 2)


def greet(name): 
    """Print a greeting to a name."""

    print("Hello " + name + "!")


def add(x, y): 
    """Add x and y together and return the sum."""
    return x + y


def circle_area(radius):
    """Return the area of a circle given the radius.""" 

    return pi * radius**2


def get_float(msg): 
    """Get a float from the user with label msg."""

    while True: 
        try:
            x = float(input(msg))
            return x 
        except ValueError: 
            print("This is not a float.")


############################    
_sum = add(4.5, 3.4)

print(_sum)

double_num(9)

greet(input("Enter your name: "))

print("{:.2f}".format(circle_area(4)))

get_float("a = ")