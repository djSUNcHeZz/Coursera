Num = int(input())
MaxNum = Num
while Num != 0:
    if Num > MaxNum:
        MaxNum = Num
    Num = int(input())
print(MaxNum)
