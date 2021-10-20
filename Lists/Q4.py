squares = [] 

for i in range(1, 11): 
    squares.append(i ** 2)

odd_squares = []
# Print only odd squares 
for i in range(len(squares)): 
    if squares[i] % 2 == 1: 
        odd_squares.append(squares[i])

print(odd_squares)