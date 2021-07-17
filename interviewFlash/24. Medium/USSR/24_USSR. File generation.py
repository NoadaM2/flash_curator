import random
s = ''
for i in range(0, 9500):
    a = random.randint(0, 100)
    if a > 70:
        s += 'SS'
    else:
        s += 'USSR'
print(s)
