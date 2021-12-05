#https://www.eolymp.com/uk/submissions/10049754
def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M


n,m= [int(i) for i in input().split()]
B = readMatrix(n)
B=B[-1::-1]
print(m,n)
A=[]
for i in range(m):
    l = []
    for j in range(n):
        l.append(B[j][i])
    A.append(l)
for row in A:
    for el in row:
        print(el, end = ' ')
    print()