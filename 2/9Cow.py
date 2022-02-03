N = int(input())
if 4 < N%100 < 20 or 4 < N%10 < 10 or N%10 == 0:
    print(N, 'korov')
elif N % 10 == 1:
    print(N, 'korova')
else:
    print(N, 'korovy')
