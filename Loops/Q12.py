size = int(input("Triangle size: "))

def pyramid(size): 
    print()
    for i in range(1, size + 1): 
        # Print spaces to align * in the middle 
        print(" "*(size - i), end = '')
        print('* '*(i))
    print(" " * (size - 1) + "*")

pyramid(size)
