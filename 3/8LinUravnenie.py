a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if (a * d - b * c) != 0:
    x = (d * e - b * f) / (a * d - b * c)
    y = (a * f - c * e) / (a * d - b * c)
elif a != 0 and ((c * b / a) - d) != 0:
    y = ((c * e / a) - f) / ((c * b / a) - d)
    x = (e - b * y / a)
elif c != 0 and (b - a * d / c) != 0:
    y = (e - a * f / c) / (b - a * d / c)
    x = (f - d * y / c)
print(x, y)
