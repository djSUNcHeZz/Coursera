def sum(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return a + sum(1, b - 1)
a = int(input())
b = int(input())
print(sum(a, b))
