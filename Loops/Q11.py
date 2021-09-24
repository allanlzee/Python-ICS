size = int(input("Triangle size: "))

for i in range(1, size + 1): 
    # Print spaces to align * in the middle 
    print(" "*(size - i), end = '')
    print('* '*(i))

def pyramid(size): 
    for i in range(1, size + 1): 
        # Print spaces to align * in the middle 
        print(" "*(size - i), end = '')
        print('* '*(i))

pyramid(size)
