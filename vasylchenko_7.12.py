#https://www.e-olymp.com/uk/submissions/9705089
n, m = map(int, input().split())
def diff4(i):

    return len(str(i)) == len(set(str(i)))
for i in range(n, m+1):
    if diff4(i):
        print(i, end = ' ')

"""   # `set` will only record unique elements.
    # We convert to a string and check if the unique
    # elements are the same number as the original elements."""