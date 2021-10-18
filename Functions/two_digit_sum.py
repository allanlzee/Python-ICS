def two_digit_sum(number): 
    """Returns the sum of the digits of a string grouped as 
    2-digit numbers. If there is an odd number of digits, the
    last digit is taken by itself."""

    two_digit = ""; 
    total_sum = 0

    curr_digit = ""

    for i in range(len(number)): 
        # Strings 
        curr_digit = number[i]
        two_digit += curr_digit

        if i % 2 == 1: 
            total_sum += int(two_digit)
            two_digit = ""
            curr_digit = ""

    # Adds the last digit in case there is an odd number of digits. 
    total_sum += int(curr_digit)

    return total_sum 

input_num = input("Enter a number: ")
print("The two-digit sum of the number is {}."
.format(two_digit_sum(input_num)))