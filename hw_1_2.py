a, b = int(input('Input a  ')), int(input('and b  '))

if b == 0:
    print("'b' mustn't be equal to 0")

else:
    c = a/b
    d = a*b
    e = a**b
    f = a+b
    g = a-b
    h = a//b
    i = a%b

    print('a/b =', c,',',
    'a*b =', d, ',',
    'a**b =', e, ',',
    'a+b =', f, ',',
    'a-b =', g, ',',
    'a//b =', h, ',',
    'a%b =', i, '.')

