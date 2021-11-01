def celsius_to_kelvin(temp: float) -> float: 
    """Return the Kelvin temperature value of the celsius
    temperature temp.
    
    >>> celsius_to_kelvin(0) 
    273.15 
    """

    CONVERSION = 273.15 

    return temp + CONVERSION 


print(celsius_to_kelvin(-273.15))