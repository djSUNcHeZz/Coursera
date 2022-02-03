s = input()
s1 = s.find('h')
s = s[::-1]
s2 = len(s) - s.find('h')
s = s[::-1]
print(s[:s1] + s[s2::])
