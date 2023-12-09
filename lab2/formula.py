import math

x=1
def f2(x, k):
    return (-1)**k * math.cos(k*x)/(k**2-1)
x1 = 1/(math.sin(math.e**x))
x2 = 1/(math.cos(math.log(x)))
x3 = math.sin(math.log(x))


for i in range(15, 36, 2):
    if(i < 20):
        print(1/(math.sin(math.e**(i/10))))
        print(f"index: {i/10}, cosec")
        
    elif(i < 30):
        print(1/(math.cos(math.log(i/10))))
        print(f"index: {i/10}, sec")
    else:
        print(math.sin(math.log(i/10)))
        print(f"index: {i/10}, sin")

#Пункт Б

sum = 0
for x in range(-100, -89, 1):
    x = x * (0.01)
    k = 2
    while(True):
        if(f2(x,k) > 0.001):
            break
        sum =+ f2(x,k)
        k=k+1
    print(f"sum is: {sum}, x = {x}")
    sum = 0




