#https://www.e-olymp.com/uk/submissions/9803415
n = (int(input()))
def to_bin(n):
    if n == 0:
        return []
    return to_bin(n // 2) + [n % 2]

def to_s_sx(l):
    s = ''
    for i in range(0, len(l)):
        if l[i] == 1:
            del l[i]
            break

    for el in l:
        if el == 1:
            s += "SX"
        else:
            s += "S"
    return s
res=to_s_sx(to_bin(n))
print(res)
