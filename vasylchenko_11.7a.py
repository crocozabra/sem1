x = float(input('x'))
k = int(input('k'))
a = x
for i in range(1, k+1):
    a *= x**2/((2*k)*(2*k+1))

print(a)