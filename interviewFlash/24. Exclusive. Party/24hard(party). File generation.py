import random

names = ['Артем', 'Пьяный', 'Саня', 'Стас']
surnames = ['Флэш', 'Мастер', 'Касио', 'Валентиныч']

buf = []  # будем следить за правильностью заполнения строки
s = ''
for i in range(0, 9000):  # сколько примерно нужно слов
    if i < 200:  # накидываем немного имён для начала (желательно 20% от общего количества)
        a = random.randint(0, 3)
        s += names[a]
        buf.append(surnames[a])
    else:
        choice = random.randint(0, 1)  # бросаем монетку "имя или фамилия"
        if choice == 0:
            a = random.randint(0, 3)
            s += names[a]
            buf.append(surnames[a])
        else:
            a = random.randint(0, 3)
            while surnames[a] not in buf:  # проверка на существование имени в стеке для конкретной фамилии
                a = random.randint(0, 3)
            s += surnames[a]
            buf.remove(surnames[a])
while len(buf) > 0:  # закрываем оставшиеся имена
    a = random.randint(0, 3)
    while surnames[a] not in buf:
        a = random.randint(0, 3)
    s += surnames[a]
    buf.remove(surnames[a])
print(s)
# далее не забываем ручками вставить "линших" людей
