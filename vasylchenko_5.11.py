#https://www.e-olymp.com/uk/submissions/9487862
n = int(input())
lst = [int(i) for i in input().split()]
x= lst[n-1]

for i in range(n - 1, 0, -1):
    lst[i] = lst[i - 1]

lst[0] = x
print(*lst)