

#while True:
    #s = str(input('Введите текст\n'))
    #n = s.split(' ')

    #if not n.isalpha():
        #print('Вводить можно только текст')
        #continue
    #else:
        #break


from string import whitespace, punctuation
#print('whitespace = {}'.format(repr(whitespace)))
#print('punctuation = {}'.format(repr(punctuation)))

s = str(input('Введите текст\n'))
s = s.lower()
n = s.split()
b = 0

def countmax():
    global b
    for i in n:
        a = len(i)
        if a > b:
            b = a

countmax()
d = dict()
for i in n:
    d[i] = n.count(i)
    #v = b - int(len(i))
    #print('|', i, ' '*v, '|', n.count(i), '|')
for name, num in d.items():
    v = b - int(len(name))
    print('|{}'.format(name), ' '*v, '|{}|'.format(num))

