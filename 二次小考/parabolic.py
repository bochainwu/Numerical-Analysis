import math
def parabolic_interpolation(f, x1, x2, x3, epsilon=1e-6, max_iterations=2):
    """
    Parabolic Interpolation algorithm to find the minimum of a function.
    
    Arguments:
    f -- the function to be minimized
    a -- the lower bound of the interval
    b -- the upper bound of the interval
    epsilon -- the desired accuracy (default 1e-6)
    max_iterations -- the maximum number of iterations (default 100)
    
    Returns:
    x -- the value of x that minimizes the function f(x)
    """
    # Initial points
    
    for i in range(max_iterations):
        x4 = x2 - 0.5*((((x2-x1)**2)*(f(x2)-f(x3))-((x2-x3)**2)*(f(x2)-f(x1)))/((x2-x1)*(f(x2)-f(x3))-(x2-x3)*(f(x2)-f(x1))))
        print(round(x1, 5), round(x2, 5), round(x3,5), round(x4, 5))
        print(round(f(x1), 5),round(f(x2), 5),round(f(x3), 5),round(f(x4), 5))
        if x4 < x2:
            if f(x4) < f(x2):
                x3 = x2
                x2 = x4
            else:
                x1 = x4
        else:
            if f(x4) < f(x2):
                x1 = x2
                x2 = x4
            else:
                x3 = x4
        
        # Check for convergence
        if abs(x3 - x1) < epsilon:
            break
    
    # Return the x-coordinate of the vertex as the minimum
    x = x4
    return x

# Define the function you want to minimize
def f(x):
    return 4*x -1.8*(x**2) +1.2*(x**3)-0.3*(x**4)

# Set the initial interval [a, b]
x1 = 1.75
x2 = 2
x3 = 2.5

# Call the Parabolic Interpolation algorithm
minimum = parabolic_interpolation(f, x1, x2, x3)

# Print the result
print(round(minimum, 5), round(f(minimum),5))
