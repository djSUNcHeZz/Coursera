n = int(input())


def IsPrime(n):
    import math
    i = 2
    while i <= (math.sqrt(n)):
        if n % i == 0:
            return ('False')
        i += 1
    return ('True')

if IsPrime(n) == 'True':
    print('YES')
else:
    print('NO')
