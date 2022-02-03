a = [int(i) for i in input().split()]
for n in range(0, len(a), 2):
    if n != (len(a) - 1):
        a[n], a[n + 1] = a[n + 1], a[n]
print(*a)
