input_string = input("Enter a string: ") 

""" solution = "" 

for i in range(len(input_string), 0, -1): 
    solution += input_string[i - 1] """ 

solution = input_string[::-1]

print(solution)