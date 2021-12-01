#https://www.e-olymp.com/uk/submissions/9802216

def main():
    while True:
        try:
            n, m = [int(i) for i in input().split()]
        except:
            break
        res = getFib(gcd(n, m)) % 10 ** 8

        print(res)

def getFib(n):
    f = [0] * (n + 2)
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

if __name__ == "__main__":
    main()