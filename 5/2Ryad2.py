a = int(input())
b = int(input())
if a < b:
    print(*tuple(range(a, b + 1)))
else:
    print(*tuple(range(a, b - 1, -1)))
