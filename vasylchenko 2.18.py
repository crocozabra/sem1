#https://www.e-olymp.com/uk/submissions/9294775
x, y, x1, y1, x2, y2 = [int(d) for d in input().split()]
if x1<=x<=x2 and y1<=y<=y2 :
    print('1')
elif x1<=x<=x2 and y2<=y<=y1:
    print('1')
elif x2<=x<=x1 and y1<=y<=y2:
    print('1')
elif x2<=x<=x1 and y2<=y<=y1:
    print('1')
else:
	print('0')