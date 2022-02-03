N = 1
M = 1
S = 1
while N != 0:
    N = int(input())
    if N > M:
        S = M
        M = N
    elif N <= M and S <= N:
        S = N
print(S)
