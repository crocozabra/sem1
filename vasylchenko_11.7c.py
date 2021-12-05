from math import factorial
x = float(input('x'))
k = int(input('k'))
a = 1
for i in range(1, k+1):
    a *= (-x) * factorial((i-1)**2+(i-1)) / factorial(i**2+i)
print(a) 