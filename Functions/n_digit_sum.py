def n_digit_sum(number, group): 
    """Returns the sum of the digits of a string grouped as 
    "group"-digit numbers. If there are leftover digits, they 
    are added regardless of the grouping."""

    digit_group = ""
    total_sum = 0

    for i in range(len(number)):
        # Add digit to temporary group of digits. 
        digit_group += number[i]

        # A full group of digits is formed, so it can be added to the sum.
        if len(digit_group) % int(group) == 0: 
            total_sum += int(digit_group) 
            digit_group = ""

    # Left over numbers 
    if len(number) % int(group) != 0:
        total_sum += int(digit_group)

    return total_sum 


input_num = input("Enter a number: ")
input_group = int(input("Enter a digit grouping: "))

print("\nThe grouped digit sum of the number is {}."
.format(n_digit_sum(input_num, input_group)))