def f(x):
    return 2*x**2+5*x-8.5

x0 ,x1 = 0.5, 1.5

for i in range(1):
    x2 = x1 - (f(x1)*(x0-x1)/(f(x0)-f(x1)))
    print(x0, x1, x2, abs((x2-x1)/x2)*100,"%")
    x0 = x1
    x1 = x2