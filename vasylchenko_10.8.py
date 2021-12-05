#https://www.eolymp.com/uk/submissions/10045867
def readMatrix(n, elementsType=int):
    M = []
    for i in range(n):
        row = [elementsType(el) for el in input().split()]
        M.append(row)

    return M

n = int(input())
A = readMatrix(n)
sum1=0
sum2=0
for i in range(n):
    sum1+= A[i][i]
    sum2+=A[i][n-i-1]

print(sum1,sum2)