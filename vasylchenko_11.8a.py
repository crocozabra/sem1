N = int(input())
S = 1
for n in range(2, N + 1):
    S += ((-1)**(n+1))*(n)
print(S)