import random
for i in range(0, 95):
    s = ''
    for j in range(0, 500):
        a = random.randint(0, 5)
        if a == 0:
            s += 'BEAR'
        if a == 1:
            s += 'BEER'
        if a == 2:
            s += 'DEER'
        if a > 2:
            b = random.randint(65, 90)
            s += chr(b)
    print(s)
