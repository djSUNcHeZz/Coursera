def summa():
    n = int(input())
    global s
    if n != 0:
        s += n
        summa()
    return s

s = 0
print(summa())
