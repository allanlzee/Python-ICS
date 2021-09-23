# n factorial program

nums = int(input("Input a positive integer: "))

counter = 0
total = 1

while counter < nums:
    counter += 1
    total *= counter

print("The product of the natural numbers up to {} is {}.".format(nums, total))
    

