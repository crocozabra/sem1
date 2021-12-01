#https://www.e-olymp.com/uk/submissions/9369366
import math
n= int(input())
fact = 1
i = 0
k=0
while i < n:
    i += 1
    fact *= i
    k = int(math.log10(fact)) + 1
print(k)

