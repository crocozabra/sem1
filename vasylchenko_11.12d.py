def P(k):
    if k == 0 or k == 1 or k == 2:
        return 1
    else:
        return (P(k -2) + P(k -3))

n =int(input('n = '))
if P(n) == 4*P(n-5)+P(n-14):
    print('P(n) =',P(n))
    print('4*P(n-5) +P(n-14) =',4*P(n-5)+P(n-14))
    print('Задовольняє')
else:
    print('P(n) = ',P(n))
    print('4*P(n-5) + P(n-14) =',4*P(n-5)+P(n-14))
    print('Не Задовольняє ')