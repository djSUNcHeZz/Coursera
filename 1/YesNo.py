A = int(input())
B = int(input())
N = A % B
print('YES' * (0 ** N), 'NO' * (1 - 0 ** N), sep='')
