import math
p = float(input())
x = int(input())
y = int(input())
s = (x * 100 + y) * (p / 100) + (x * 100 + y)
r = s / 100
c = s - (int(r) * 100)
print(int(r), int(c))
