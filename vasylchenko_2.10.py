#https://www.e-olymp.com/uk/submissions/9293364
a=int(input())
s = a // 100
o = a % 10
if s>o:
    print(s)
elif s==o:
    print('=')
elif o>s:
    print(o)
