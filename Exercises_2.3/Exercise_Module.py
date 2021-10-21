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
        while True: 
            try: 
                integers.append(int(input("Enter Integer {}: ".format(i + 1))))
                
                break

            except ValueError: 
                print("Not an integer. Please try again.")
        
    return integers


def get_float_list(n): 
    pass 


def main(): 
    a = get_int_list(5)
    print(a)


if __name__ == "__main__": 
    main()
