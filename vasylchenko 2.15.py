#https://www.e-olymp.com/uk/submissions/9294754
a, b, c = [int(d) for d in input().split()]
d=b**2-4*a*c
if d<0:
 print('No roots')
elif d==0:
 print('One root:', int(-b/(2*a)))
elif d>0:
    if a>0:
        print('Two roots:',int((-b-(d)**0.5)/(2*a)),int((-b+(d)**0.5)/(2*a)))
    else:
     print('Two roots:',int((-b+(d)**0.5)/(2*a)),int((-b-(d)**0.5)/(2*a)))