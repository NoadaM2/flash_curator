import random
for i in range(0, 950):
    s = ''
    for j in range(0, 500):
        a = random.randint(0, 100)
        if a > 70:
            if a > 90:
                s += 'X'
            s += 'FLASH'
            if a < 80:
                s += 'X'
        else:
            b = random.randint(65, 90)
            s += chr(b)
    print(s)
