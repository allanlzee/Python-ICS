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

for digit in range(len(isbn_clean)):
    isbn_total += int(isbn_clean[digit]) * (10 - digit)

check_digit = 11 - (isbn_total % 11) 

if check_digit == 10:
    check_digit = "X"

print("The check digit must be {}.".format(check_digit))


