SUM_OF_ANGLES = 180 

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

sum = angle1 + angle2 + angle3

is_triangle = False 

if (sum == SUM_OF_ANGLES):
    is_triangle = True 

if is_triangle: 
    if (angle1 == angle2) and (angle2 == angle3):
        print("Equilateral")
    elif (angle1 == angle2) or (angle2 == angle3) or (angle1 == angle3): 
        print("Isosceles")
    else:
        print("Scalene")
else: 
    print("Not a triangle")




