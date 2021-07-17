f = open('24_Calculator.txt')
a = []
for s in f:
    nn = ''
    t = ''
    i = 0
    while s[i].isdigit():
        nn += s[i]
        i += 1
    n = int(nn)
    while i < len(s)-1:
        if s[i] == '+':
            i += 1
            while s[i].isdigit():
                t += s[i]
                i += 1
            n += int(t)
            t = ''
        if s[i] == '-':
            i += 1
            while s[i].isdigit():
                t += s[i]
                i += 1
            n -= int(t)
            t = ''
        if s[i] == '*':
            i += 1
            while s[i].isdigit():
                t += s[i]
                i += 1
            n *= int(t)
            t = ''
    a.append(n)
print(max(a))
