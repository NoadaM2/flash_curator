f = open('24_WGR.txt')
s = f.readline()
if s[0] == 'W' and s[1] == 'G':  # обрабатываем начало строки, ведь s[0] может есть только вправо (не подходит под общий алгоритм)
    s = s[:1]+s[2:]
if s[0] == 'G' and s[1] == 'R':
    s = s[:1]+s[2:]
i = 0
n = len(s)
while i < n:  # for i in range(0, len(s)) не подойдет, ведь s меняется в цикле, соответственно меняется и ее длина
    if s[i] == 'W':
        if s[i-1] == 'G':
            s = s[:i-1] + s[i:]  # удаляем символы методом среза строк
        if s[i+1] == 'G':
            s = s[:i+1] + s[i+2:]
    if s[i] == 'G':
        if s[i - 1] == 'R':
            s = s[:i - 1] + s[i:]
        if s[i + 1] == 'R':
            s = s[:i + 1] + s[i + 2:]
    n = len(s)
    i += 1
print(s.count('G'), ',', s.count('R'))
