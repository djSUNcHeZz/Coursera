X = int(input())
Y = int(input())
if Y % (Y + 1 - X) == 0:
    print('YES')
else:
    print('NO')
