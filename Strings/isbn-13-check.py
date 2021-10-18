ISBN_SYSTEM = 13 

print("ISBN-13 Verifier\n")

isbn_temp = input("Enter the first 12 digits of an ISBN-13 number: ")
isbn_clean = "" 
isbn_total = 0

# Filter out all non-digit characters, there are no letters
for char in isbn_temp: 
    if "9" >= char >= "0": 
        isbn_clean += char 

# Calculate the weighted sum of the first 12 digits of the ISBN-13 number
for i in range(ISBN_SYSTEM - 1): 
    if i % 2 == 0: 
        isbn_total += int(isbn_clean[i]) * 1
    else: 
        isbn_total += int(isbn_clean[i]) * 3 

# Find the check digit of the ISBN-13 number. Mod by 10 twice
# to handle check digits of 0. 
check_digit = str((10 - isbn_total % 10) % 10)

# Add the check digit to the initial ISBN-13 to get a valid number. 
isbn = isbn_temp + check_digit

print("\nThe check digit is {}.".format(check_digit))
print("The ISBN-13 number is {}.".format(isbn))

