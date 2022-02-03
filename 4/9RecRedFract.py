def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def ReduceFraction(n, m):
    p = n // gcd(n, m)
    q = m // gcd(n, m)
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
