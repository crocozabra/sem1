#https://www.e-olymp.com/uk/submissions/9580270
s = input()
res = ""
for c in s:
    res += c
    if 'a' <= c <= 'z':
        res += c
print(res)