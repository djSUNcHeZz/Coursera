def ctn(intList):
    return intList % 2 == 0


intList = [int(i) for i in input().split()]
print(*list(filter(ctn, intList)))
