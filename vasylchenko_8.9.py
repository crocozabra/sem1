#https://www.e-olymp.com/uk/submissions/9786745
num=int(input())
def baseN(num,b=13,numerals="0123456789ABCDEFGHIJKLMNOPRSTUVWXYZ"):
    if num==0 and numerals[0]:
        return '0'
    else:
        return (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b]) # lstrip () используется, чтобы вырезать пробелы или заданную строку символов слева.
print(baseN(num))

"""

def baseN(num,b=13,numerals="0123456789ABCDEFGHIJKLMNOPRSTUVWXYZ"):

    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
print(baseN(num))
"""
