n = int(input())


def MinDivisor(n):
    import math
    i = 2
    while i <= (math.sqrt(n)):
        if n % i == 0:
            return (i)
        i += 1
    return (n)

print(MinDivisor(n))
