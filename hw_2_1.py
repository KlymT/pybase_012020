a, b, c = float(input('Введите параметры квадратного уравнения - a, b c; a = ')), float(input('b = ')), float(input('c = '))

D = b ** 2 - 4 * a * c
print('D=', D)

if a == b == 0:
    print('Уравнение не имеет решения')

elif a == 0:
    X = -c/b
    print('Уравнение имеет один корень X = ', X)

elif D < 0:
    X1 = (-b + complex(D) ** 0.5) / (2 * a)
    X2 = (-b - complex(D) ** 0.5) / (2 * a)
    print('X1=', X1, ';' 'X2=', X2)

else:
    X1 = (-b + D**0.5)/(2*a)
    X2 = (-b - D**0.5)/(2*a)
    print('X1=', X1,';' 'X2=', X2)

