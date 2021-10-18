def calc_speed(distance, time): 
    """Returns the speed of an object from the distance
    traveled and time passed."""

    return distance / time 


distance = float(input("Enter a distance: ")) 
time = float(input("Enter a time: "))
speed = calc_speed(distance, time)
print(speed)