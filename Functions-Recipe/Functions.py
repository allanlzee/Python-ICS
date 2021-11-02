<<<<<<< HEAD
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

=======
from math import sqrt 


__author__ = "Allan Zhou"
>>>>>>> 3642df07cdc4cd8de5608ffe1301c4baf94cde6b


def calculate_rectangle_area(l: float, w: float) -> float: 
    """Return the area of a rectangle with length l and width w.
    
    >>> calculate_rectangle_area(4, 6)
    24
    """

    return l * w 


def calc_triangle_perimeter(a: float, b: float, c: float) -> float: 
    """Return the perimeter of a triangle given the three sides 
    a, b, and c.
    
    >>> calc_triangle_perimeter(4, 5, 6)
    15
    """

    return a + b + c 


def calc_triangle_area(a: float, b: float, c: float) -> float: 
    """Return the area of a triangle given the three side lengths, 
    a, b, and c.
    
    >>> calc_triangle_area(2, 2, 3) 
<<<<<<< HEAD
=======

>>>>>>> 3642df07cdc4cd8de5608ffe1301c4baf94cde6b
    """

    # Heron's Formula: √ s(s - a)(s - b)(s - c), where s is the semi-perimeter
    # (a + b + c) / 2 and a, b, and c are side lengths of the triangle. 

    s = (a + b + c) / 2
    print(s)  

<<<<<<< HEAD
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
=======
    area = sqrt(s * (s - a) * (s - b) * (s - c))
>>>>>>> 3642df07cdc4cd8de5608ffe1301c4baf94cde6b
    return round(area, 2) 


def calc_factorial(num: int) -> int: 
    """Return the factorial of the positive number num.
    
    >>> calc_factorial(5)
    120 
    """

    total = 1 
    
    for i in range(2, num + 1): 
        total *= i 

    return total 


def calc_slope(p1, p2) -> float: 
    """Return the slope of a line segment given the coordinates of the 
    two points, p1 and p2.
    
    >>> calc_slope([1, 2], [2, 3]) 
    1 
    """

    if p1[0] < p2[0]: 
        x1 = p1[0]
        x2 = p2[0]
        y1 = p1[1]
        y2 = p2[1]

    else: 
        x1 = p2[0]
        x2 = p1[0]
        y1 = p2[1]
        y2 = p1[1]

    return (y2 - y1) / (x2 - x1) 


def cartesian_dist(p1, p2) -> float: 
    """Return the Cartesisn distance between two points, p1 and p2, both with
    coordinates on the x-y plane.
    
    >>> cartesian_dist([0, 0], [3, 4])
    5 
    """

    x1 = p2[0]
    x2 = p1[0]
    y1 = p2[1]
    y2 = p1[1]

<<<<<<< HEAD
    return round(math.sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2), 2)
=======
    return round(sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2), 2)
>>>>>>> 3642df07cdc4cd8de5608ffe1301c4baf94cde6b


def abs_value(num1: float, num2: float) -> bool: 
    """Return True iff num1 and num2 have the same absolute value.
    
    >>> abs_value(2.1, -2.1)
    True 
    """

    return abs(num1) == abs(num2) 


def max_of_mins(nums, values) -> float: 
    """Return the maximum of the minimums of two pairs of numbers.
    
    >>> max_of_mins([1, 2], [2, 3])
    2
    """

    return max(min(nums), min(values))


def string_to_list(string: str): 
    """Return a string as a list of single characters.
    
    >>> string_to_list("Allan")
    ['A', 'l', 'l', 'a', 'n'] 
    """

    chars = [] 
    
    for char in string: 
        chars.append(char) 

    return chars 


def factors(number: int): 
    """Return all the factors of the positive integer, number.
    
    >>> factors(12)
    [1, 2, 3, 4, 6, 12]
    """
    
    facts = []

    for i in range(1, number + 1):
        if number % i == 0: 
            facts.append(i)

    return facts 


def is_prime(number: int) -> bool: 
    """Return True iff number is a prime number.
    
    >>> is_prime(18) 
    False 
    """

    # Exclude 1 and number as factors.
    for i in range(2, number): 
        if number % i == 0: 
            return False 

    return True 


def list_of_primes(number: int): 
    """Return a list of prime numbers that are less than or equal to 
    number.
    
    >>> list_of_primes(10) 
    [2, 3, 5, 7] """

    primes = [] 

    for i in range(2, number + 1): 
        if is_prime(i): 
            primes.append(i)

    return primes 


def main(): 
    print(calc_triangle_area(2, 2, 3)) 
    print(calc_factorial(5))
    print(cartesian_dist([0, 0], [3, 4]))
    print(max_of_mins([0, 1], [2, 3]))
    print(string_to_list("Allan"))
    print(list_of_primes(10))


if __name__ == "__main__": 
<<<<<<< HEAD
    main() 
=======
    main() 
>>>>>>> 3642df07cdc4cd8de5608ffe1301c4baf94cde6b
