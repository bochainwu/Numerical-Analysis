def f1(x):
    return 3*x**2-12*x+10
def f2(x):
    return x**3-6*x**2+10*x-6
x0 = 3.5

for i in range(10):
    a = round(x0 - f2(x0)/f1(x0), 5)
    print(a)
    if(i==9):
        print(abs((a-x0)/a)*100)
    else:
        x0 = a