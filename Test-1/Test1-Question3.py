# Question 3: Pythagoras 
from math import sqrt

print("PYTHAGORAS")

first_leg = float(input("Enter the first length: "))
second_leg = float(input("Enter the second length: "))

# Pythagorean Theorem for Hypotenuse and Area Formula 
hyp = sqrt(first_leg ** 2 + second_leg ** 2)
area = first_leg * second_leg / 2

print("\nThe hypotenuse is {}.".format(hyp))
print("The area is {}.".format(area))

