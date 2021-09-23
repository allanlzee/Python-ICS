total = 0
total_nums = int(input("How many numbers: "))

for i in range(0, total_nums):
    num = int(input("Enter number {}: ".format(i + 1)))
    total += num

avg = total / total_nums
print("The average is {}.".format(avg))
    
