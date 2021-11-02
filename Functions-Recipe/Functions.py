"""2.4 Function Design Recipe Questions."""

__author__ = "Allan Zhou"

import math 

def is_num_ddd(num: int) -> bool: 
    """Return True iff num is an even number.
    
    >>> is_num_odd(2) 
    True
    """

    return num % 2 == 0 


def farenheit_to_celsius(temperature: float) -> float: 
    """Return the value of temperature, which is measured in
    celsius, in farenheit.
    
    >>> farenheit_to_celsius(0)
    32 
    """

    return temperature * 9 / 5 + 32 


def celsius_to_farenheit(temperature: float) -> float: 
    """Return the value of temperature, which is measured in 
    farenheit, in celsius.
    
    >>> celsius_to_farenheit(32)
    0
    """
    
    return (temperature - 32) * 5 / 9 
    

def calculate_hypotenuse(a: float, b: float) -> float: 
    """Return the hypotenuse of a right triangle with legs
    a and b.
    
    >>> calculate_hypotenuse(3, 4) 
    5
    """

    return math.sqrt(a**2 + b**2)


def validate_triangle_sides(a: float, b: float, c: float) -> bool: 
    """Return True iff the lengths a, b, and c can form a right
    triangle.
    
    >>> validate_triangle_sides(3, 4, 5)
    True
    """

    # The three sides, with c as the hypotenuse, must satisfy the 
    # Pythagorean Theorem to form a right triangle.
    return a**2 + b**2 == c**2 


def perimeter_of_rectangle(l: float, w: float) -> float: 
    """Return the perimeter of a rectangle with length l and
    width w using formula 2(l + w).
    
    >>> perimeter_of_rectangle(3, 4)
    14 
    """

    return 2 * (l + w)



def main(): 
    pass 


if __name__ == "__main__": 
    main() 