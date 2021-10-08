isbn_temp = input("Enter the first 9 digits of an ISBN number: ") 
isbn_clean = "" 
isbn_total = 0 

ISBN_SYSTEM = 10 

# Filter out all characters except for digits. 
for char in isbn_temp: 
    # 48 <= ord(char) <= 57 
    if "9" >= char >= "0": 
        isbn_clean += char 
    
    # In ISBN-10, X represents 10 
    elif char == "X": 
        isbn_clean += char 

# Calculate weighted sum 
for digit in range(len(isbn_clean)):
    isbn_total += int(isbn_clean[digit]) * (10 - digit)

# Calculate the digit that will make the isbn_total a multiple of 11. 
# Mod by 11 again to handle check digit of 0. 
check_digit = str((11 - isbn_total % 11) % 11)

# Special case of check_digit for ISBN-10 system  
if check_digit == "10":
    check_digit = "X"

isbn = isbn_temp + check_digit 

print("The check digit must be {}.".format(check_digit))
print("The valid ISBN number is {}.".format(isbn))
