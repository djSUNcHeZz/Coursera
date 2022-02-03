a, b, c = int(input()), int(input()), int(input())
if a > b:
    (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
if c < b:
    (b, c) = (c, b)
    if b < a:
        (a, b) = (b, a)
if a > b:
    (a, b) = (b, a)
print(a, b, c)
