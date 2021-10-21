"""A module containing methods that solves each of the
questions from Exercise 2.3."""

__author__ = "Allan Zhou" 

def get_string_list(n): 
    """Ask the user for n strings and add each of them to a list, 
    which is returned.""" 

    strings = [] 

    for i in range(n): 
        strings.append(input("String {}: ".format(i + 1)))

    return strings 


def get_int_list(n): 
    """Ask the user for n integers and add each of them to a list, 
    which is returned. Ensure that the user enters integers."""

    integers = [] 

    for i in range(n): 
        # Ensure that the input is an integer. 
        while True: 
            try: 
                integers.append(int(input("Enter Integer {}: ".format(i + 1))))
                break

            except ValueError: 
                print("Not an integer. Please try again.\n")
        
    return integers


def get_float_list(n): 
    """Ask the user for n floats and add each of them to a list, 
    which is returned. Ensure that the user enters floats."""

    floats = [] 

    for i in range(n): 
        # Ensure that the input is an integer. 
        while True: 
            try: 
                floats.append(float(input("Enter Float {}: ".format(i + 1))))
                break

            except ValueError: 
                print("Not an integer. Please try again.\n")
        
    return floats


def mean(num_list): 
    """Return the mean of the list num_list and return the value."""

    total = 0

    for num in num_list: 
        total += num 

    mean = total / len(num_list)
    return mean


def lengths_of_strings(string_list): 
    """Return a list which is the lengths of each string in string_list."""
    
    string_lengths = [] 

    for string in string_list: 
        string_lengths.append(len(string)) 

    return string_lengths


def mean_length_of_strings(string_list): 
    """Return the mean length of all strings in string_list."""

    string_lengths = lengths_of_strings(string_list) 
    total = 0 

    for length in string_lengths: 
        total += length 

    mean = total / len(string_list)
    return mean 


def count(list, item): 
    """Return the number of occurrences of item in a list."""

    occurences = 0 

    for char in list: 
        if char == item: 
            occurences += 1
            
    return occurences 


def median(num_list): 
    """Return the median of a numerical list."""

    sorted = num_list.sort()
    length = len(num_list)

    # Even number of items.
    if length % 2 == 0: 
        # Take the mean of the two middle numbers. 
        median = (sorted[length / 2 - 1] + sorted[length / 2]) / 2
    else: 
        # Take the middle number. 
        median = sorted[length / 2 - 1]

    return median 
    

def median_length_of_strings(string_list): 
    """Return the median length of all strings in string_list."""

    string_lengths = lengths_of_strings(string_list)
    sorted_string_lengths = string_lengths.sort() 

    length = len(sorted_string_lengths) 

    # Even number of items.
    if length % 2 == 0: 
        # Take the mean of the two middle numbers. 
        median = (sorted[length / 2 - 1] + sorted[length / 2]) / 2
    else: 
        # Take the middle number. 
        median = sorted[length / 2 - 1]

    return median 


def class_list(num_students): 
    """Print a class list with student, followed by student ID."""

    # Store all student names and corresponding student IDs. 
    student_name = [] 
    student_ID = [] 

    # Make the student column as long as the longest name inputted.
    # The minimum width is 8, to match the length of the string 'Student'. 
    longest_name = 8

    for i in range(num_students): 
        student_name.append(input("Enter student name {}: ".format(i + 1))) 
        student_ID.append(int(input("Enter student ID {}: ".format(i + 1)))) 

        # If the inputted student name is longer than the current longest student
        # name, replace longest_name with the length of the new name. 
        if len(student_name[i]) > longest_name:
            longest_name = len(student_name[i])

    print("CLASS LIST\n" + "-" * 10)

    print("Student" + " " * (longest_name - 5) + "ID")

    for i in range(num_students): 
        print("{:{width}}  {}".format(student_name[i], student_ID[i], width=longest_name)) 


def main(): 
    class_list(2)


if __name__ == "__main__": 
    main()


