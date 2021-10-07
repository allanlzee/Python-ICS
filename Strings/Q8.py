numbers = input("Input some numbers: ")

total = 0

for n in numbers: 
    num = int(n) 
    total += num 

print("The sum is {}.".format(total))
