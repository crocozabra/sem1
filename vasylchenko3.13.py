#https://www.e-olymp.com/uk/submissions/9365628
n = int(input())
count = 1
m = 1
if m!=n:
    while n!=m :
        m*=count
        count+=1
    print(count-1)
else:
    print(1)
