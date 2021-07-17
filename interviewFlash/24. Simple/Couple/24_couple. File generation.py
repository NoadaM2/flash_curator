import random
s = ''
for i in range(0, 9500):
    a = random.randint(65, 90)
    if chr(a) != 'D':  # символы D проставляем вручную
        s += chr(a)
print(s)