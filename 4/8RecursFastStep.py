def stepen(a, n):
    if a % 2 == 0:
        return (a ** 2) ** (n / 2)
    else:
        return a * a ** (n - 1)
a = float(input())
n = int(input())
print(stepen(a, n))
