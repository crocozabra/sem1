#https://www.e-olymp.com/uk/submissions/9760086
a, b = map(int, input().split())

def count(a,b):
    s=0
    for i in range(a, b + 1):
        s += ones(i)
    return s

def ones(i):
    return bin(i).count('1')

res=count(a,b)
print(res)

"""
a, b = map(int, input().split())
f=lambda a,b:''.join(map(bin,range(a,b+1))).count('1')
print(f(a,b))
"""
#print(sum(1 for i in bin(n)[2:] if i == '1'))
