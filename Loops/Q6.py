num = int(input("Enter the base of your factorial: "))

factorial = 1 

for i in range(1, num + 1): 
    factorial *= i 

print("The value of {}! is {}.".format(num, factorial)) 