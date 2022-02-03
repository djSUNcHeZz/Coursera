N = int(input())
a = [int(i) for i in input().split()]
x = int(input())
minB = 2000
indexA = 0
for r in range(N):
    B = abs(x - a[r])
    if B < minB:
        minB = B
        indexA = r
print(a[indexA])
