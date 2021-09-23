from math import pi

# Volume of a Sphere: 4/3 * pi * r ** 2

radius = float(input("Enter the radius of the sphere: "))
volume = 4 / 3 * pi * radius ** 2
print("The volume of the sphere is " + str(round(volume, 2)))
