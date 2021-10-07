numbers = input("Enter some numbers: ")

total = 0
for i in range(0, len(numbers), 2): 
    num = int(numbers[i:i+2])
    total += num

print(total)
        
