N = int(input())
P = 0.75
for n in range(3, N + 1):
    P *= (1 - 1/n**2)

print(P)