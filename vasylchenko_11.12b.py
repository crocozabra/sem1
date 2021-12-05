def P(k):
    if k == 0 or k == 1 or k == 2:
        return 1
    else:
        return (P(k -2) + P(k -3))

n =int(input('n = '))
if P(n) == 2*P(n-2) - P(n-7):
    print('P(n) = ',P(n))
    print('2*P(n-2)- P(n-7)=',2*P(n-2)-P(n-7))
    print('Задовольняє')
else:
    print('P(n) = ',P(n))
    print('2*P(n-2)+P(n-7)=',2*P(n-2)-P(n-7))
    print('Не Задовольняє')