GRID_WIDTH = 12

for i in range(1, GRID_WIDTH + 1): 
    for j in range(i, i * GRID_WIDTH + 1, i):
        print("{:3}".format(j), end = ' ')
    print() 
