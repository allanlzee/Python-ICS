num = int(input("Enter a number: "))

# Total sum of all the digits 
total = 0

# The number used to isolate each digits using mod 
divisor = 10

# The previous mod calculation 
mod = 0 

while num % (divisor / 10) != num:
    # Isolate the number using the current mod - previous mod
    # Then remove all place holder tens 
    div = (num % divisor - mod) / (divisor / 10)
    
    mod = num % divisor
    
    total += div
    divisor *= 10

print("The sum of digits is {}.".format(round(total, 0))) 
    
