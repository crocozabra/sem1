def P(k):
    if k == 0 or k == 1 or k == 2:
        return 1
    else:
        return (P(k -2) + P(k -3))

n =int(input('n = '))
if P(n) == P(n-2) +P(n-4)+P(n-8):
    print('P(n) = ',P(n))
    print('P(n-2) + P(n-4)+P(n-8) =',P(n-2)+P(n-4)+P(n-8))
    print('Задовольняє')
else:
    print('P(n) = ',P(n))
    print('P(n-2) + P(n-4)+P(n-8) =',P(n-2) +P(n-4)+P(n-8))
    print('Не Задовольняє')