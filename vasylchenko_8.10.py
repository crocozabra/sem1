#https://www.e-olymp.com/uk/submissions/9785730
n = abs(int(input()))
li= list(range(1, n + 1))

def permutation(li):
    l = []
    if len(li) == 1:
        l.append([li[0]])
        return l
    for i in range(0, len(li)):
        for p in permutation(li[0:i] + li[i+1:]):
            p.insert(0, li[i])
            l.append(p)
    return l

for res in permutation(li):
        print(*res)

"""
n=int(input())
l = list(range(1, n + 1))
def permutList(l):
    if not l:
            return [[]]
    k = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            k.extend([[e] + r for r in permutList(temp)])

    return k
for res in permutList(l):
    print(*res)
    
****    
from itertools import permutations
def lexicographical_permutation(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        print(x)
str = '123'
lexicographical_permutation(str)
"""