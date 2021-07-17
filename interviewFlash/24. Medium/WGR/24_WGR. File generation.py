import random
s = ''
for i in range(0, 9500):
    a = random.randint(0, 2)
    if a == 0:
        s += 'W'
    if a == 1:
        s += 'G'
    if a == 2:
        s += 'R'
print(s)
