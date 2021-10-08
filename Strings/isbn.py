isbn_temp = input("Enter an ISBN number: ") 
isbn_clean = "" 
isbn_total = 0 

ISBN_SYSTEM = 10 

# Boolean to state whether ISBN number contains X 
isbn_with_x = False

# Temporary Digits-Only Length of ISBN
length = 10  

# Filter out all characters except for digits. 
for char in isbn_temp: 
    # 48 <= ord(char) <= 57 
    if "9" >= char >= "0": 
        isbn_clean += char 
    
    # In ISBN-10, X represents 10 
    elif char == "X": 
        isbn_clean += char 

# Calculate weighted sum for ISBN-10 Number
weight = ISBN_SYSTEM 

if isbn_clean[ISBN_SYSTEM - 1] == "X": 
    isbn_total += 10 
    length = 9

for i in range(length): 
    isbn_total += int(isbn_clean[i]) * weight 
    weight -= 1 
    
if isbn_total % 11 == 0: 
    print("The ISBN number is valid.")
else: 
    print("This is not an ISBN number.")
