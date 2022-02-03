s = input()
s1 = s.find(' ')
print(s[s1 + 1:] + s[s1] + s[:s1])
