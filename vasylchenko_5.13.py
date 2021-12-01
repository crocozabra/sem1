#https://www.e-olymp.com/uk/submissions/9459041
N = int(input())
lst = [float(i) for i in input().split()]

suma = 0
counter = 0
for i in lst:
    if i > 0:
        suma += i
        counter += 1
if counter!=0:
    x=suma/counter
    print( "%0.2f" % x)
else:
    print('Not Found')

