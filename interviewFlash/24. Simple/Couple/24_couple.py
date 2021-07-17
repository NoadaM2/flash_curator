f = open('24_couple.txt')
s = f.readline()
posD = 0
m = posK = 10000
for i in range(0, len(s)):
    if s[i] == 'D':
        posD = i
    if s[i] == 'K':
        posK = i
    m = min(m,abs(posD-posK)-1)
print(m)