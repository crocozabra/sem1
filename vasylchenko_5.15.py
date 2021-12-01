#https://www.e-olymp.com/uk/submissions/9459737
N = int(input())
lst = [int(i) for i in input().split()]
m=min(lst)
k=max(lst)
for el in range(N):
    c=lst[el]
    if c == m :
        lst[el] =k
    if c==k:
        lst[el]=m

print(*lst)

