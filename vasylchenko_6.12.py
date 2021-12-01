#https://www.e-olymp.com/uk/submissions/9587668
s = input()
k = int(input())
res=""
for i in s:

    res += chr(65 + (((ord(i) - 65) - k) % 26))

print(res)

