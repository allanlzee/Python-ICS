total_chars = 0

for i in range(10): 
    string = input("Enter String {}: ".format(i + 1))
    total_chars += len(string)

print("Total Characters: {}".format(total_chars))
print("Average Number of Characters: {}".format(total_chars / 10))
