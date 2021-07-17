f = open('24_FLASH.txt')
mf = 0
for s in f:
    c = 0
    for i in range(0,len(s)-6):
        if s[i] != 'X' and s[i+1] == 'F' and s[i+2] == 'L' and s[i+3] == 'A' and s[i+4] == 'S' and s[i+5] == 'H' and s[i+6] != 'X':
            c += 1
        mf = max(mf,c)
f.close()
f = open('24_FLASH.txt')
ans = 10000
for s in f:
    c = 0
    for i in range(0, len(s) - 6):
        if s[i] != 'X' and s[i + 1] == 'F' and s[i + 2] == 'L' and s[i + 3] == 'A' and s[i + 4] == 'S' and s[
            i + 5] == 'H' and s[i + 6] != 'X':
            c += 1
    if c == mf:
        ans = min(ans,s.count('A'))
print(ans)
