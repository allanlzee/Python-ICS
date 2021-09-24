num = int(input("Input a positive integer: "))

for i in range(1, 13): 
    multiple = num * i 
    print("{} x {} = {}".format(num, i, multiple)) 