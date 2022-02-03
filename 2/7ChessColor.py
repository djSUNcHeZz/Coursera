Y1 = int(input())
X1 = int(input())
Y2 = int(input())
X2 = int(input())
if ((Y1 - Y2) % 2 != 0) and ((X1 - X2) % 2 != 0):
    print('YES')
elif ((Y1 - Y2) % 2 == 0) and ((X1 - X2) % 2 == 0):
    print('YES')
else:
    print('NO')
