a, b, c = float(input('Введите параметры квадратного уравнения - a, b c; a = ')), float(input('b = ')), float(input('c = '))
if a == 0:
    print("Параметр 'а' не может быть равен '0' введите значения параметров повторно")
else:
    D = b ** 2 - 4 * a * c
    print('D=', D)

if D < 0:
    X1 = (-b + complex(D) ** 0.5) / (2 * a)
    X2 = (-b - complex(D) ** 0.5) / (2 * a)
else:
    X1 = (-b + D**0.5)/(2*a)
    X2 = (-b - D**0.5)/(2*a)

print('X1=', X1, 'X2=', X2)

