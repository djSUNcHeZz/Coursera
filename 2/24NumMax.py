N = -1
P = -1
Q = 1
S = 1
while N != 0:
    N = int(input())
    if N == P:
        S += 1
    if N != P:
        P = N
        if Q < S:
            Q = S
        S = 1
print(max(S, Q))
