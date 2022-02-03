intList = [int(i) for i in input().split()]
for n in range(len(intList) - 1):
    if intList[n + 1] > intList[n]:
        print(str(intList[n + 1]) + ' ', end='')
