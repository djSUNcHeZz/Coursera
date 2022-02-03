s = input()
s1 = s.find('f')
s = s[s1 + 1::]
s2 = s.find('f') + s1 + 1
if s1 == -1:
    print(-2)
elif s2 == s1:
    print(-1)
elif s2 != s1:
    print(s2)
