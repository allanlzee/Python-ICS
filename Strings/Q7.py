upper = input("Enter a string: ")

lower = ""

for letter in upper: 
    if ord(letter) > 64 and ord(letter) < 91:
        lower += chr(ord(letter) + 32)
    else: 
        lower += letter

print(lower)
