n = float(input())
i = 1
s = 0
while i <= n:
    s += (1 / (i ** 2))
    i += 1
print('{0:.5f}'.format(s))
