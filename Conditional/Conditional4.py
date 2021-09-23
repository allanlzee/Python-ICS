num = int(input("Enter a number: "))

# even_odd is 1 (true) when odd, otherwise it is 0 (false) 
even_odd = num % 2;

if (num == 0):
    result = "zero."
elif (even_odd and num > 0):
    result = "odd and positive."
elif (even_odd and num < 0):
    result = "odd and negative."
elif (not(even_odd) and num > 0):
    result = "even and positive."
else:
    result = "even and negative."

print("The number {} is {}".format(num, result))

