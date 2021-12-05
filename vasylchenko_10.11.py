#https://www.eolymp.com/uk/submissions/10046527
def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M

n, m = [int(i) for i in input().split()]
Aseats = readMatrix(n)
input()
Asold = readMatrix(n)

s = 0
for i in range(n):
    for j in range(m):
        if Asold[i][j] == 1:
            s += Aseats[i][j]

print(s)