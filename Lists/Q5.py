def sum_list(array): 
    """Find the sum of all elements in an array."""

    sum = 0
    for i in range(len(array)): 
        sum += array[i] 

    return sum 


input_array = [] 

num_elements = int(input("How many numbers are you inputting: "))

for i in range(num_elements): 
    input_array.append(int(input("Number {}: ".format(i + 1))))

_sum = sum_list(input_array)

print("The sum of the elements in the array is {}.".format(_sum))