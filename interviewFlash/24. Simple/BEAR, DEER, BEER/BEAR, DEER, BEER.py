f = open('BEAR, DEER, BEER.txt')
c = 0
for s in f:
    if s.count('DEER') < s.count('BEAR') < s.count('BEER'):
        c += 1
print(c)