def create_list(n): 
    """Take n numbers as user input and add them to
    a list to print."""

    nums = []

    for i in range(n): 
        nums.append(int(input("Number {}: ".format(i + 1))))

    return nums


def array_sum(array): 
    """Return the sum of an array using a for loop and accumulator."""

    _sum = 0
    for num in array: 
        _sum += num 

    return _sum 


def even_array(array): 
    """Return a new array with only the even numbers of the passed array."""
    
    even_numbers = []

    for num in array: 
        if num % 2 == 0: 
            even_numbers.append(num)

    return even_numbers


def abs_large(array): 
    """Return an array with numbers from array that are larger than 10
    or smaller than -10."""

    absolutely_big = [] 

    for num in array: 
        if num > 10 or num < - 10: 
            absolutely_big.append(num) 

    return absolutely_big


def cubed(array): 
    """Return a list with all the elements of array cubed."""

    cubed_array = []
    for num in array: 
        cubed_array.append(num ** 3) 

    return cubed_array 
        

def max_element(array): 
    """Return the largest element in an array."""
    
    smallest = 1e6

    for num in array: 
        if num < smallest: 
            smallest = num 

    return smallest 


def min_element(array): 
    """Return the smallest element in an array."""

    biggest = -1e6

    for num in array: 
        if num > biggest: 
            biggest = num 

    return biggest 


n = int(input("How many numbers are you inputting: "))

input_array = create_list(n)
print("The array: {}.".format(input_array))

input_array_sum = array_sum(input_array)
print("The sum: {}.".format(input_array_sum))

input_array_total = sum(input_array) 
print("The sum (using sum()): {}.".format(input_array_total))

input_even_array = even_array(input_array) 
print("The array with only even numbers: {}.".format(input_even_array))

input_abs_big = abs_large(input_array)
print("The absolutely large array is {}.".format(input_abs_big))

# Use the list from #4 
input_cubed = cubed(input_abs_big)
print("The cubed list is {}.".format(input_cubed))

input_max = max_element(input_cubed)
print("The greatest element in the array is {}.".format(input_max))

input_min = min_element(input_cubed) 
print("The smallest element in the array is {}.".format(input_min))