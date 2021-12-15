def my_min(my_list: list) -> float: 
    """Return the smallest value in my_list."""

    if len(my_list) > 0: 
        smallest = my_list[0]

    for num in my_list: 
        if num < smallest: 
            smallest = num 

    return num 


def search(my_list: list, searched_value) -> bool: 
    """Return true if the item searched_value is in my_list."""

    for item in my_list: 
        if item == searched_value:
            return True 

    return False 


def max_value(my_list: list): 
    """Print the index and value of the largest value of a list."""

    if len(my_list) > 0: 
        largest = my_list[0]
        index = 0 

    for i in range(len(my_list)): 
        if my_list[i] > largest: 
            largest = my_list[i]
            index = i 

    print("The index and value of the largest item in the list are {} and {}, respectively."
        .format(index, largest))


def sorted_insert(new_value, sorted_list: list): 
    """Insert new_value into sorted_list."""

    for i in range(len(sorted_list)):
        if new_value < sorted_list[i]:
            sorted_list.insert(i, new_value)
        
    sorted_list.insert(len(sorted_list), new_value)
    return sorted_list
    
def linear_search_occurences(searched_value, search_list: list) -> int: 

    num_times = 0 

    for item in search_list: 
        if item == searched_value: 
            num_times += 1 
    
    return num_times 


def linear_search_first(searched_value, search_list: list) -> int: 

    for i in range(len(search_list)): 
        if search_list[i] == searched_value: 
            return i 

    return -1 


print(sorted_insert(6, [1, 3, 5, 7, 10])) 