def my_max(a, b): 
    """Return the larger of a and b."""

    if a > b: 
        return a
    elif a < b:
        return b 
    # The numbers are equal. 
    else:
        return a


def my_min(a, b):
    """Return the smalle of a and b."""

    if a > b:
        return b
    elif a < b:
        return a
    # The numbers are equal.
    else:
        return a
    

print(my_max(9, 2))