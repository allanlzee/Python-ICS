initial_string = input("Type a string: ")

new_string = ""

""" for i in range(len(initial_string)): 
    if i == 0 or i == len(initial_string) - 1: 
        continue 
    else: 
        new_string += initial_string[i]  """

new_string = initial_string[1:len(initial_string) - 1]

print(new_string)