def f(x):
    return 2*x**2+5*x-8.5
delta = 0.01
x0, x1 = 1.5, 0

for i in range(3):
    x1 =x0 - delta*x0*f(x0)/(f(x0+delta*x0)-f(x0))
    print(round(x0, 5), round(x1, 5))
    print(abs((x1-x0)/x1)*100,"%")
    x0 = x1
