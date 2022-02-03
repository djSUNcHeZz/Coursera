a = float(input())
b = float(input())


def IsPointInSquare(a, b):
    return (-1 <= a <= 1) and (-1 <= b <= 1)

if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')
