n=int(input())
if n%2==0 :
    print('YES')
elif n<0 and n%2!=0:
    print("YES")
elif (n%2==0 and (n<0 and n%2!=0)) :
    print("NO")
else:
    print("NO")

n=int(input())
if n%2==0 and (n<0 and n%3==0):
	print('NO');
if (n%2!=0) and (n<0 and n%3==0):
    print('YES');
if (n%2==0) and (n<0 and n%3!=0):
	print('YES');
if n%2!=0 and (n<0 and n%3!=0):
	print('NO');