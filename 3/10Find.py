s = input()
s1 = s.find('f')
s = s[::-1]
s2 = len(s) - s.find('f') - 1
if s1 != -1:
    print(s1)
    if s2 != s1:
        print(s2)
