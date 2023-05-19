def f(x):
    return x**3-6*x**2+10*x-6

x0 ,x1 = 2.5, 3.5

for i in range(2):
    x2 = x1 - (f(x1)*(x0-x1)/(f(x0)-f(x1)))
    print(x0, x1, round(x2, 5), abs((x2-x1)/x2)*100,"%")
    x0 = x1
    x1 = x2