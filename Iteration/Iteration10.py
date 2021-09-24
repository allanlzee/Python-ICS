print("Enter a series of positive numbers. Input -1 to stop. ")

STOP = -1

largest = 0
smallest = 1e500
total = 0
counter = 0

while True:
    num = int(input("Number: "))

    if (num == STOP):
        break

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total += num
    counter += 1 

print("Total numbers: {}.".format(counter))
print("Total sum of numbers: {}.".format(total))
print("Largest value: {}.".format(largest))
print("Smallest value: {}.".format(smallest))
print("Average value: {}.".format(total / counter))

    
