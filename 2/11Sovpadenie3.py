a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == c or b == c or a == b:
    print(2)
else:
    print(0)
