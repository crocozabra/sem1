#https://www.e-olymp.com/uk/submissions/9465845
N = int(input())
lst = [int(i) for i in input().split()]
M= int(input())
lst1 = [int(i) for i in input().split()]

lstx=[]
for i in lst:
    if i not in lst1:
        lstx.append(i)

print(len(lstx))
print(*lstx)



