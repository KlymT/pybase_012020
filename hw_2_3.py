print('Начало ряда Чисел Фибоначчи - 1, 1')

def fib():
    n = int(input('\nВведиде количество следующих Чисел фибоначи, n = '))
    a = 1
    b = 1
    i = 1
    if n <= 0:
        print("Программа завершает работу")
    else:
        while i <= n:
            c = a + b
            a = b
            b = c
            print(c, end=", ")
            i +=1

while True:
    fib()
