#https://www.e-olymp.com/uk/submissions/9422460
counter = 0
while True:
    a = int(input())
    if a != 0:
        if a%2==0:
            counter += a
    else:
        break

print(counter)