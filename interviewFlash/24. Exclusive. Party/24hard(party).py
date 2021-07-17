f = open('24hard(party).txt', 'r', encoding="utf-8")  # обязательно указываем кодировку для кириллицы
s = f.readline()
buf = []  # некое подобие стека
i = 0
while i <= len(s)-1:  # Реализуем почти стандартный алгоритм проверки на ПСП(правильность скобочной последовательности)
    if s[i:i + 5] == 'Артем':   # срез строки{ символы [начало:конец] }, можно if s[i] == 'А' and s[i+1] == 'р' and s[i+2] == 'т' and s[i+3] == 'е' and s[i+4] == 'м':
        buf.append('Артем')
        i += 5
    if s[i:i + 6] == 'Пьяный':
        buf.append('Пьяный')
        i += 6
    if s[i:i + 4] == 'Саня':
        buf.append('Саня')
        i += 4
    if s[i:i + 4] == 'Стас':
        buf.append('Стас')
        i += 4
    if s[i:i + 4] == 'Флэш':
        if 'Артем' in buf:
            buf.remove('Артем')
        else:  # на случай если обнаружим лишнее
            buf.append('Флэш')
        i += 4
    if s[i:i + 6] == 'Мастер':
        if 'Пьяный' in buf:
            buf.remove('Пьяный')
        else:
            buf.append('Мастер')
        i += 6
    if s[i:i + 5] == 'Касио':
        if 'Саня' in buf:
            buf.remove('Саня')
        else:
            buf.append('Касио')
        i += 5
    if s[i:i + 10] == 'Валентиныч':
        if 'Стас' in buf:
            buf.remove('Стас')
        else:
            buf.append('Валентиныч')
        i += 10

for elem in buf:
    print(elem)
