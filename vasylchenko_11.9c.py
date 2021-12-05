N=int(input())
P=0.6
for n in range(2,N+1):
    P*=(n+1)/(n+2)
print(P)
