#https://www.e-olymp.com/uk/submissions/9738911
k = int(input())
n=1
def prime(n):
    for i in range(2, (int)(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_happy_prime(n):
    reversed_n = int(str(n)[::-1])
    if prime(n):
        if prime(reversed_n) and n != reversed_n:
            return True
    return False
while k > 0:
    if is_happy_prime(n):
        k -= 1
        if k != 0:
            n += 1
    else:
        n += 1

if n <= 10 ** 6:
    print(n)
else:
    print('-1')