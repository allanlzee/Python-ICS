def fibonacci(num_terms): 
    """Prints the first num_terms of the Fibonacci sequence, where the terms
    are separated by commas."""

    first_num = 1
    second_num = 1 

    for i in range(int(num_terms)): 
        print(first_num, end=", ")

        # Temporary Value of Hold First term 
        temp_first = first_num 
        first_num = second_num 
        second_num = first_num + temp_first

    print("...")

terms = input("How many terms do you want to print: ")
fibonacci(terms)
