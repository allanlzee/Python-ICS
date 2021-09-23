month = int(input("Enter the number of a month: "))

# 31 Days: Jan, Mar, May, July (7), Aug, Oct, Dec

# Feb
if (month == 2):
    days = 28
# Jan, Mar, May, July
elif (month <= 7 and month % 2 == 1): 
    days = 31
elif (month <= 7 and month % 2 == 0):
    days = 30
elif month % 2 == 0:
    days = 31
else:
    days = 30

print("There are {} days in the month.".format(days))


