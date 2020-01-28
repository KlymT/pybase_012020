def sum_of_natural_numbers(a, b):
    if a <= b:
        d = (a + b)*(b-a+1)/2

    else:
        d = (a + b)*(a-b+1)/2

    print('Сумма всех значений в заданном промежутке составляет', d)

while True:
    a, b = int(input('Введите два натуральных целых числа - a, b;\na = ')), int(input('b = '))

    if a < 0 or b < 0:
        print('Натуральные числа не могут принимать отрицательные значения')
        continue
    sum_of_natural_numbers(a, b)
    print('Желаете повторить?\nD = Да\nN = Нет')
    c = input()
    if c == 'D':
        continue
    if c == 'N':
        break







