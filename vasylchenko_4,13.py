#https://www.e-olymp.com/uk/submissions/9423179
n = int(input())
count = 0
for i in range(10, 100):
    k = n*i
    s = k // 100
    d = k // 10 % 10
    o = k % 10
    if (i // 10 + i % 10) == (s+d+o):
        count += 1

print(count)