a = [int(i) for i in input().split()]
minA = a[0] + 1
maxA = a[0] - 1
for n in range(len(a)):
    if a[n] < minA:
        minA = a[n]
        min = n
    if a[n] > maxA:
        maxA = a[n]
        max = n
a[min], a[max] = a[max], a[min]
print(*a)
