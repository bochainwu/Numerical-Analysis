def f1(x):
    return 4*x +5
def f2(x):
    return 2*x**2+5*x-8.5
x0 = 1.5

for i in range(3):
    a = round(x0 - f2(x0)/f1(x0), 5)
    print(a)
    if(i==2):
        print(abs((a-x0)/a)*100)
    else:
        x0 = a