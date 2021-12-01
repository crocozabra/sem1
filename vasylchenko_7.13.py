#https://www.e-olymp.com/uk/submissions/9703795
import math
x1, y1, z1, x2, y2, z2, x3, y3, z3 = [int(i) for i in input().split()]

A = (x1, y1, z1)
B = (x2, y2, z2)
C = (x3, y3, z3)

def length(A,B):
    return (sum((B[i] - A[i]) ** 2 for i in range(len(A)))) ** 0.5

def vpcircle(a, b, c):
    p = (a + b + c)/2
    r = (((p - a)*(p - b)*(p - c))/p)**0.5
    return math.pi*r**2
def opcircle(a: float, b: float, c: float) -> float:
    p = (a + b + c)/2
    R = (a*b*c)/(4*(p*(p - a)*(p - b)*(p - c))**0.5)
    return math.pi*R**2

a = length(A, B)
b = length(B, C)
c = length(A, C)
p = (a+b+c)/2

k = vpcircle(a,b,c)/opcircle(a,b,c)
if ('%.3f' % k) == 0:
    print('Zero!')
else:
    print('%.3f' % k)