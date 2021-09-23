# Question 1: Greeter 
CURRENT_YEAR = 2021

print("GREETER")

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Calculate the user's age 
age = CURRENT_YEAR - birth_year
print("\nHello {}! You are {} years old.".format(name, age))
