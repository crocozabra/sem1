#https://www.e-olymp.com/uk/submissions/9579917
s = input()
l=['+','-','/','*','%']
counter = 0
for i in range(1,len(s)):
    if s[i] in l and s[i-1] not in l :

        counter += 1

print(counter)