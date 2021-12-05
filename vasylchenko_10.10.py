#https://www.eolymp.com/uk/submissions/10046121
##https://www.eolymp.com/uk/submissions/10046137
def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M

x = int(input())
n = int(input())
A = readMatrix(n)

good_cols_indices = []
for j in range(n):
    for i in range(n):
        if x == A[i][j]:
            good_cols_indices.append(j)

    if j in good_cols_indices:
        print("YES")
    else:
        print("NO")

"""
for j in range(n):
    colx=0
    for i in range(n):
        if x == A[i][j]:
            colx+=1

    if colx!=0:
        print("YES")
    else:
        print("NO")
"""



