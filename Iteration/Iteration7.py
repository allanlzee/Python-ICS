# get n numbers, calculate the average

counter = 0 
nums = int(input("Enter the number of numbers to calculate: "))
total = 0 

while counter < nums:
    num = int(input("Enter a number: "))
    total += num
    counter += 1

avg = total / nums
print(avg)

