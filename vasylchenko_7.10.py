#https://www.e-olymp.com/uk/submissions/9768530
m, k = [int(i) for i in input().split()]
num_base_m = input()

def to_decimal(num_base_m: str, base_m: str = 2) -> str:
    num_base_10 = 0
    for power, digit in enumerate(num_base_m[::-1]):
        num_base_10 += digit_to_number(digit) * base_m**power
    return num_base_10


def from_decimal(num_base_10: str, base_m: str = 2) -> str:
    num_base_m = ""
    n = int(num_base_10)
    if n == 0:
        return '0'
    while n > 0:
        num_base_m += number_to_digit(n % base_m)
        n //= base_m
    return num_base_m[::-1]


def digit_to_number(digit: str) -> int:
    if digit.isdigit(): # 1, 2, ..., 9
        return int(digit)
    else: # Then it's a letter: A, B, C, ...
        return ord(digit) - 55 # where - 55 = - 65 + 10


def number_to_digit(number: int) -> str:
    if number <= 9:
        return str(number)
    else:
        return chr(number + 55) # where + 55 = -10 + 65

d = from_decimal(to_decimal(num_base_m, m), k)
print(d)

