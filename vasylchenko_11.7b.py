x = float(input('x'))
k = int(input('k'))
a = -x
for i in range(2, k + 1):
    a *= -((k - 1) * x) / k
print(a)