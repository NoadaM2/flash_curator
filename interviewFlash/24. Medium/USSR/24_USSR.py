f = open('24_USSR.txt')
s = f.readline()
s = s.replace('USSR','A')
print(s.count('A')-s.count('SS'))
