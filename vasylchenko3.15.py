#https://www.e-olymp.com/uk/submissions/9371801
k=int(input())
n=int(input())
x = 0
i = 1
while n!=0:
    m = n%10
    x = x + (m*i)
    i = i*k
    n = n//10
print(x)

