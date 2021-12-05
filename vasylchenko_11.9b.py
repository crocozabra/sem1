from math import factorial
N = int(input())
P =3
for n in range(2, N + 1):
    P *= (2 + 1/factorial(n))

print(P)