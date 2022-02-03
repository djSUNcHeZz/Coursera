intList = [int(i) for i in input().split()]
minN = 1001
for n in range(len(intList)):
    if 0 < intList[n] < minN:
        minN = intList[n]
print(minN)
