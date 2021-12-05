#https://www.eolymp.com/uk/submissions/10045664

def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M


n = int(input())
A = readMatrix(n)
r, c = [int(i) for i in input().split()]
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()