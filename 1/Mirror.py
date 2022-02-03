A = int(input())
A1 = A // 1000
A2 = A // 100 % 10
A3 = A // 10 % 10
A4 = A % 10
print(((A1 - A4) ^ 2) // ((A3 - A2) ^ 2))
