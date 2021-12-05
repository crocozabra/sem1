N = int(input())
S = 1/2
for n in range(3, N + 1):
    S += 1 / ((n-1)*n)
print(S)