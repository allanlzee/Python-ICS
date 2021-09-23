nums = int(input("Input a positive integer: "))

counter = 0
total = 0

while counter < nums:
    counter += 1
    total += counter

print("The sum of the natural numbers up to {} is {}.".format(nums, total))
    
