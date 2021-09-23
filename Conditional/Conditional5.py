num = int(input("Enter the first number: "))
num2 =  int(input("Enter the second number: "))

if (num > num2):
    print("{} is greater than {}.".format(num, num2))
elif (num < num2):
    print("{} is less than {}.".format(num, num2))
else:
    print("The numbers are equal.")
    
