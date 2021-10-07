input_string = input("Enter a string: ") 

solution = "" 

""" for i in range(1, len(input_string) + 1, 3): 
    solution += input_string[i]  """

solution = input_string[1:len(input_string):3]
print(solution)