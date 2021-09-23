# Question 2: Rectangle Facts 
print("RECTANGLE FACTS")

length = float(input("Enter the length: "))
area = float(input("Enter the area: "))

# Rectangle formulas for width and perimeter 
width = area / length
perimeter = 2 * (width + length)

print("\nThe width of the rectangle is {}, and the perimeter is {}."
      .format(width, perimeter))

