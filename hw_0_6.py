a = input('Введите длину стороны A треугольника, см:')
b = input('Введите длину стороны B треугольника, см:')
c = input('Введите длину стороны C треугольника, см:')
d = (float(a)+float(b)+float(c))/2
e = float(d)*(float(d)-float(a))*(float(d)-float(b))*(float(d)-float(c))
f = pow(float(e), .5)
print('Площадь треугольника=', f, 'см2')