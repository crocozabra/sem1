#https://www.e-olymp.com/uk/submissions/9588249
s = input()
s = ''.join(s.split())
flag = 0

length = len(s)
for i in range(length//2):
    if(s[i] != s[length - i - 1]):
        flag = 1
        break

if(flag == 0):
   print("YES")
else:
   print('NO')