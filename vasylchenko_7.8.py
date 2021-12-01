#https://www.e-olymp.com/uk/submissions/9738496
import math
a, b = map(int, input().split())

def gcd(p,q):
    if p==0:
        return q
    return math.gcd(q%p,p)

def count(a,b):
    i=0
    k=a*b
    for p in range(1,b+1):
        if (not(k%p) and math.gcd(p,k//p))==a:
            i+=1
    return i
res=count(a,b)
print(res)