import random
for i in range(0, 95):
    s = ''
    for j in range(0, 100):
        b = random.randint(5, 30)
        s += str(b)
        a = random.randint(0, 2)
        if a == 0:
            s += '+'
        if a == 1:
            s += '-'
        if a == 2:
            s += '*'

    print(s[:-1])