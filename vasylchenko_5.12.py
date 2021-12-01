#https://www.e-olymp.com/uk/submissions/9460068
N = int(input())
lst = [int(i) for i in input().split()]
lst1 = []

for i in lst:
    if i not in lst1:
        lst1.append(i)

print(*lst1)