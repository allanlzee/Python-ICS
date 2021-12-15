from fractions import Fraction 
from math import pi
from math import cos 

f = Fraction(1, 2) 
print(f)

g = Fraction(3, 5)
print(g)

h = f + g 
print(h)

i = cos(pi/3)
i = Fraction(i).limit_denominator()
print(i)