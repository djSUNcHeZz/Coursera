M = int(input())
N = int(input())
K = int(input())
if (K < M * N) and (K >= M or K >= N) and (K % M == 0 or K % N == 0):
    print('YES')
else:
    print('NO')
