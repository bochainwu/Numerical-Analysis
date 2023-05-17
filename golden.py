import math

def golden_section_search(f, xu, xl, epsilon=1e-6):
    """
    Golden-Section Search algorithm to find the minimum of a function.
    
    Arguments:
    f -- the function to be minimized
    xu -- the lower bound of the interval
    xl -- the upper bound of the interval
    
    Returns:
    x -- the value of x that minimizes the function f(x)
    """
    # Calculate the golden ratio
    phi = (1 + math.sqrt(5)) / 2
    #calculate the distance d
    d = (phi - 1)*(xu - xl)
    # Calculate the initial points x1 and x2
    x1 = xl + d
    x2 = xu - d
    
    for i in range(1):
        print(round(xl,4),round(f(xl),4),round(x2,4),round(f(x2),4),round(x1,4), round((f(x1)),4),round(xu,4),round(f(xu),4))
        # Calculate the new points x1 and x2
        if f(x2) < f(x1):
            xu = x1
            x1 = x2
            d  = (phi - 1)*(xu - xl)
            x2 = xu - d
        else:
            xl = x2
            x2 = x1
            d = (phi - 1)*(xu - xl)
            x1 = xl + d
        
    print(round(xl,4),round(f(xl),4),round(x2,4),round(f(x2),4),round(x1,4), round((f(x1)),4),round(xu,4),round(f(xu),4))
    # Return the midpoint of the final interval as the minimum
    if(f(x1)>f(x2)):
        return x2
    else:
        return x1
def f(x):
    return (x**2)*0.5 - 10*math.sin(x)

# Set the initial interval [a, b]
xu = 2
xl = 1

# Call the Golden-Section Search algorithm
minimum = golden_section_search(f, xu, xl)

# Print the result
print( minimum, f(minimum))