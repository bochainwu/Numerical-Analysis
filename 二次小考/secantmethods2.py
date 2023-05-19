def f(x):
    return x**3-6*x**2+10*x-6

delta = 0.01
x0, x1 = 3.5, 0

for i in range(2):
    x1 =x0 - delta*x0*f(x0)/(f(x0+delta*x0)-f(x0))
    print(round(x0, 5), round(x1, 5))
    print(abs((x1-x0)/x1)*100,"%")
    x0 = x1
