intList = [int(i) for i in input().split()]
maxN = intList[0]
indexN = 0
for n in range(len(intList)):
    if intList[n] >= maxN:
        maxN = intList[n]
        indexN = n
print(maxN, indexN)
