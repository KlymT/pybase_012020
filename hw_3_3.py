'''
Пользователь вводит с клавиатуры строки, состоящие из слов.
Пустая строка означает прекратить ввод текста.
Программа выводит на экран слова из текста, отсортированные по алфавиту.
Изменить программу из Задачи №2 так, чтобы слова не повторялись.
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

d = dict()
for i in n:
     d[i] = n.count(i)

for i in d:
    print(i)
