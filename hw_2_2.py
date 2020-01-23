a, b = int(input('Введите два значения - a, b; a = ')), int(input('b = '))
def sum_of_natural_numbers (a, b):
    if a <= b:
        d = (a + b)*(b-a+1)/2

    else:
        d = (a + b)*(a-b+1)/2

    print('Сумма всех значений в заданном промежутке составляет', d)


sum_of_natural_numbers(a,b)





