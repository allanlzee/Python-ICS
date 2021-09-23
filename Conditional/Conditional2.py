num = int(input("Enter a number: "))

if 0 < num < 100:
    print("High.")
elif -100 < num < 0:
    print("Low.")
elif num == 0:
    print("Zero.")
else:
    print("Outside.")

