#https://www.e-olymp.com/uk/submissions/9842535
n = int(input())
m = input()

def counter(s):
    counts = dict.fromkeys(s, 0)
    for i in s:
        counts[i] += 1
    return counts

counts = counter(m)
for letter, el in counts.items():
    if el % 2 !=0:
        print(letter)
        break
else:
    print("Ok")