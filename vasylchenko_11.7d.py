x = float(input('x'))
k = int(input('k'))
a = 1
for k in range(1, k + 1):
    a *= (k + 1) * x / k ** 2

print(a)