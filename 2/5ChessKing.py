Y1 = int(input())
X1 = int(input())
Y2 = int(input())
X2 = int(input())
if Y2 == Y1 and (X2 == X1 + 1 or X2 == X1 - 1):
    print('YES')
elif X2 == X1 and (Y2 == Y1 + 1 or Y2 == Y1 - 1):
    print('YES')
elif Y2 == Y1 - 1 and (X2 == X1 + 1 or X2 == X1 - 1):
    print('YES')
elif Y2 == Y1 + 1 and (X2 == X1 + 1 or X2 == X1 - 1):
    print('YES')
else:
    print('NO')
