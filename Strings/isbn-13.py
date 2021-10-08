ISBN_SYSTEM = 13 

print("ISBN-13 Verifier\n")

isbn_temp = input("Enter an ISBN-13 number: ")
isbn_clean = "" 
isbn_total = 0

# Filter out all non-digit characters, there are no letters

for char in isbn_temp: 
    if "9" >= char >= "0": 
        isbn_clean += char 

for i in range(ISBN_SYSTEM): 
    if i % 2 == 0: 
        isbn_total += int(isbn_clean[i]) * 1
    else: 
        isbn_total += int(isbn_clean[i]) * 3 

if isbn_total % 10 == 0: 
    print("This is a valid ISBN-13 number.")
else: 
    print("This is an invalid ISBN-13 number.") 
