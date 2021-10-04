# Times Tables
# Generates a multiplication table from two integers, given by the user. 
# The maximum number of rows is 20 and the maximum number of columns is
# 15. 

print("TIMES TABLE\n")

MAX_ROWS = 20 
MAX_COLUMNS = 15
PADDING = 5

# Ensure that the user enters an integer. Keep asking for input until 
# user enters integer. 
while True: 
    try: 
        rows = int(input("Enter the number of rows (maximum is 20): "))
        columns = int(input("Enter the number of columns (maximum is 15): "))

        # Check if numbers are within the dimension boundaries (maximum
        # 20 rows, 15 columns)
        if rows > MAX_ROWS and columns > MAX_COLUMNS: 
            print("Please lower the number of rows and columns.\n") 
            continue 
        elif rows > MAX_ROWS:
            print("Please lower the number of rows.\n") 
            continue 
        elif columns > MAX_COLUMNS:
            print("Please lower the number of columns.\n")
            continue
        else: 
            break 

    except ValueError: 
        print("Not an integer! Try again. \n")

print() 

# Each column has a width of 5. These spaces align the row of dashes
# with the columns of numbers. 
print(" " * PADDING, end = '') 

# Print the numbers 1 to columns, including columns itself. 
for i in range(1, columns + 1): 
    print("{:{width}}".format(i, width = PADDING), end = '')

# Print 5 dashes per number on the line below, since each column 
# has a width of 5. 
print("\n    ", "-" * PADDING * columns) 

# Print the row number and all the multiples of it up to the nth 
# multiple, where n is columns, all with a width of 5. 
for i in range(1, rows + 1): 
    # Use width = PADDING - 2, since there is a " |" after the row number. 
    print("{:{width}} |".format(i, width = PADDING - 2), end = '')

    for j in range(1, columns + 1):
        print("{:{width}}".format(j * i, width = PADDING), end = '')

    print() # Move to next row of numbers.

print()