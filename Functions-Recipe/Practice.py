"""A4 Practice: Lists, Functions, and the Function Design Recipe

Complete the code below as required with proper formatting.

Instructions follow the format #n.

When completed correctly, the output should appear exactly as below.

DO NOT alter the main() function, but definitely read it to aid you in
completing the function code.

<BEGIN SAMPLE OUTPUT>

    A4 Practice: Testing the code:

    A list of numbers: [5, 8, 7, 9, 1, 3, 6, 2, 4]
    The smallest value is: 1
    The index of the smallest value is: 4
    The index of the smallest value starting from index 5 is: 7
    The values at index 5 and 8 swapped are: [5, 8, 7, 9, 1, 4, 6, 2, 3]
    The list sorted is: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Congratulations! You sorted a list using Selection Sort!

<END SAMPLE OUTPUT>

"""


#1 Complete the HEADER of this function, including type contract.
def smallest(xs: list) -> float: 
    """Return the smallest value in the numerical list xs.

    >>> smallest([2, 3, 4, 5])
    2
    >>> smallest([3.14, 5.7, -1.0, 12])
    -1.0
    """

    # Assume first item is the smallest
    smallest_ = xs[0]
    
    for i in range(1,len(xs)):
        if xs[i] < smallest_:
            smallest_ = xs[i]
    return smallest_


#2 Complete the DESCRIPTION of this function.
def index_of_smallest(xs: list) -> int:
    """Return the index of the smallest value in the numerical list xs.

    >>> index_of_smallest([2, 3, 4, 5])
    0
    >>> index_of_smallest([3.14, 5.7, -1.0, 12])
    2
    """

    smallest_ = smallest(xs)
    return xs.index(smallest_)


#3 Complete the DESCRIPTION and EXAMPLES of this function.
def index_of_smallest_from(xs: list, idx: int) -> int:
    """Return the index of the smallest value from the list xs, starting
    from index idx and going to the end. 
    
    >>> index_of_smallest_from([5, 8, 7, 9, 1, 3, 6, 2, 4], 5) 
    7 
    
    >>> index_of_smallest_from([5, 8, 7, 9, 1, 3, 6, 2, 4], 2) 
    4
    """

    # Use a slice to find the smallest item from index idx to the right.
    smallest_from = smallest(xs[idx:])
    
    # Add the index offset to return the actual index of the item.
    return xs[idx:].index(smallest_from) + idx


#4 Complete the HEADER and BODY of this function.
def swap(nums: list, start: int, end: int): 
    """Swap, or exchange, the item at index i with the item at index j in
    the list xs.
    
    >>> swap([5, 8, 7, 9, 1, 3, 6, 2, 4], 1, 2) 
    [5, 7, 8, 9, 1, 3, 6, 2, 4]

    >>> swap([5, 8, 7, 9, 1, 3, 6, 2, 4], 0, 8) 
    [4, 8, 7, 9, 1, 3, 6, 2, 5]
    """

    first_num_swap = nums[start]
    second_num_swap = nums[end]
    nums[start] = second_num_swap
    nums[end] = first_num_swap


#5 Complete the HEADER (including type contract) and BODY of this function.
def selection_sort(nums: list): 
    """Sort the list xs from least to greatest.

    Use selection Sort:
    Start at index 0 of the list.
    Swap the smallest item in the list with the item at index 0.
    Move to index 1.
    Swap the smallest item to the right of index 0 with the item at index 1.
    Move to the next index and repeat until the end of the list is reached.

    >>> selection_sort([5, 8, 7, 9, 1, 3, 6, 2, 4])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> selection_sort([1, 3, 2, 7, 4, 9])
    [1, 2, 3, 4, 7, 9]
    """

    length = len(nums)

    for i in range(length): 
        index_smallest = index_of_smallest_from(nums, i) 

        swap(nums, i, index_smallest) 


#--DO NOT ALTER ANY CODE BELOW THIS LINE--#
def main():
    print('A4 Practice: Testing the code:\n')
    nums = [1, 3, 2, 7, 4, 9, 6, 10, 5]
    print('A list of numbers:', nums)
    print('The smallest value is:', smallest(nums))
    print('The index of the smallest value is:', index_of_smallest(nums))
    start = 5
    print('The index of the smallest value starting from index', start,'is:',
          index_of_smallest_from(nums, start))
    end = 8
    print('The values at indices', start, 'and', end, 'swapped are: ', end='')
    swap(nums, start, end)
    print(nums)
    print('The list sorted is: ', end='')
    selection_sort(nums)
    print(nums)
    print('Congratulations! You sorted a list using Selection Sort!')


if __name__ == '__main__':
    main()