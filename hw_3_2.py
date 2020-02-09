'''
Пользователь вводит с клавиатуры строки, состоящие из слов.
Пустая строка означает прекратить ввод текста.
Программа выводит на экран слова из текста, отсортированные по алфавиту.
'''

a = str(input('Введите текст\n'))
b = str(',')
c = str()


def fib():
    global a
    global b
    global c
    while not b == str(''):
        c = a + b
        a = c
        b = str(input('Введите текст\n'))


fib()

s = c.lower()
s = s.replace(',', ' ', -1)
s = s.replace('.', ' ', -1)
s = s.replace(':', ' ', -1)
s = s.replace('\n', ' ', -1)
s = s.replace('  ', ' ', -1)
n = s.split(' ')
n = sorted(n)
f = 0


def countmax():
    global f
    for i in n:
        a = len(i)
        if a > f:
            f = a


countmax()
d = dict()
for i in n:
     d[i] = n.count(i)

for name, num in d.items():
    v = f - int(len(name))
    print('|{}'.format(name), ' '*v, '|{}|'.format(num))