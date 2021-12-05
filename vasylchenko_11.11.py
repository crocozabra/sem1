def prime(n):
    for i in range(2, (int)(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

f1 = 0  
f2 = 1

for i in range(2, n + 1):
    f1, f2 = f1 + f2, f1
    print(i, f1)
    if i != 4 and prime(f1) and not prime(i):
        print(i, f1)
        break
else:
    print("Задовільняє")