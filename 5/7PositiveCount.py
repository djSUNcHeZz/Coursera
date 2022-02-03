def ctn(intList):
    return intList > 0


intList = [int(i) for i in input().split()]
s = list(filter(ctn, intList))
print(len(s))
