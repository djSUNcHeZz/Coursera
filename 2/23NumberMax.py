N = -1
M = -1
S = 1
while N != 0:
    N = int(input())
    if N == M:
        S += 1
    if N != 0 and N > M:
        M = N
        S = 1
print(S)
