#https://www.e-olymp.com/uk/submissions/9369892
n = int(input())
count = 0
x = 0
k=0
while n != 0:
    k=n%10
    if (k) % 2 == 0:
        k += 1
        x += 10 ** count*k
        n //= 10
    else:
        k-= 1
        x = x + 10 ** count *k
        n = n // 10
    count += 1
print(x)
