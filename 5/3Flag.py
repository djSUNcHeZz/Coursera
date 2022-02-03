n = int(input())
print(n * '+___ ', sep='', end='\n')
for i in range(n):
    print('|' + str(i + 1) + ' / ', end='')
print(sep='')
print(n * '|__\ ', sep='', end='\n')
print(n * '|    ', sep='', end='\n')
