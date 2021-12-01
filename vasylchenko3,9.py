#https://www.e-olymp.com/uk/submissions/9365469
n=int(input())
x=1
k=1
while k<=n:
	if x%2!=0 and x%3!=0 and x%5!=0:
		print(x, end = ' ')
		x+=1
		k+=1
	else:
		x+=1