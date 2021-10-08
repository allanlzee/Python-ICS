lower = input("Enter a string: ")

upper = ""

for letter in lower: 
    if ord(letter) < 97: 
        upper += letter
    else:
        upper += chr(ord(letter) - 32)

print(upper)
    
