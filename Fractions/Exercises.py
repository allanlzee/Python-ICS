from fractions import Fraction 

a = Fraction(1, 2)
b = Fraction(2, 3)
c = Fraction(4, 5)
d = Fraction(3, 7)

print(a + b) 
print(c - d) 
print(b ** 2)
print(c * b)
print(b / a)
print((a + b) * (c - d)) 


def get_frac(prompt: str) -> Fraction: 
    """Get user input and create a fraction object."""

    while True: 
        try: 
            x = input(prompt)
            frac = Fraction(x).limit_denominator()
            return frac 
        except ValueError: 
            print("Invalid input.")


print(get_frac("Enter a value to convert to a fraction: ")) 


FIRST_PROMPT = "Enter first fraction: "
SECOND_PROMPT = "Enter second fraction: "


def calculator(): 
    while True: 
        print("\n1. Add.")
        print("2. Subtract.")
        print("3. Multiply.")
        print("4. Divide.")
        print("5. Exit.\n")

        choice = input("What would you like to do: ")

        if choice == "5": 
            print("Good bye.")
            break 
        
        a = get_frac(FIRST_PROMPT) 
        b = get_frac(SECOND_PROMPT)

        if choice == "1": 
            print(a + b)

        elif choice == "2": 
            print(a - b)

        elif choice == "3": 
            print(a * b)

        elif choice == "4": 
            print(a / b)


calculator()