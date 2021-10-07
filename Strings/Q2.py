initial_string = input("Enter a string: ")

new_string = ""
""" 
for i in range(len(initial_string), 0, -1):
    new_string += initial_string[i - 1] """

new_string = initial_string[::-1]

print(new_string)
