def cls():
    print("\n" * 100)


def check_password(func):
    def wrapper():
        passwd=str(input("Введите пароль: "))
        if passwd=='pass1':
            cls()
            print("Вход выполнен!")
            func()
        else:
            print("В доступе отказано!")

    return wrapper

@check_password
def fibo():
    a, b = 1, 1
    n = int(input("Номер элемента ряда Фибоначчи: "))
    i = 0
    while i < n - 2:
        fib_sum = a + b
        a, b = b, fib_sum
        i = i + 1
    print("Значение этого элемента:", b)


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a ** 2
        a, b = b, a + b


def arithmetic_operation(operation):  # так и не понял как работает lambda
    if operation == '+':  # но в документации по ошибке сказано было что нужно использовать её
        return lambda x, y: x + y
    elif operation == '-':
        return lambda x, y: x - y
    elif operation == '*':
        return lambda x, y: x * y
    elif operation == '/':
        return lambda x, y: x / y
    else:
        return lambda x, y: print('Такой операции нет!')


def sorting():
    s = str(input("Введите слова"))
    a = s.split(' ')
    print(sorted(sorted(a), key=str.upper))


def sorting_abs():
    s=[]
    n=int(input("Сколько чисел будет?"))
    print("Вводите числа по 1")
    for i in range(n):
        x=int(input())
        s.append(x)
    print(sorted(sorted(s),key=abs,reverse=True))


x = -1

while x != 0:
    y = -1
    print("1:Генераторы\n2:Функция как объект \n3:Функ. для итераторов и коллекций \n4:Декоратор \n0:Выход")

    x = int(input("Выберете раздел задач: "))
    if x == 1:  # Генераторы
        cls()
        while y != 0:
            print("1:fibonacci()\n2:\n3: \n4: \n0:Назад")

            y = int(input("Введите номер задания "))

            if y == 1:
                for n in fibonacci(7):
                    print(n)

            else:

                print("Такого задания нет")

    elif x == 2:  # Функция как объект
        cls()
        while y != 0:
            print("1:arithmetic_operation()\n2:\n3: \n4: \n0:Назад")

            y = int(input("Введите номер задания "))

            if y == 1:
                operation = arithmetic_operation('+')
                print(operation(1, 4))



            else:

                print("Такого задания нет")



    elif x == 3:  # Функ. для итераторов и коллекций
        while y != 0:
            print("1:sorted()\n2:sorting_abs()\n3: \n4: \n0:Назад")

            y = int(input("Введите номер задания "))

            if y == 1:
                sorting()

            if y == 2:
                sorting_abs()




    elif x == 4:
        cls()
        while y != 0:
            print("1:check_password\n2:\n3: \n4: \n0:Назад")

            y = int(input("Введите номер задания "))

            if y == 1:

                fibo()



            else:

                print("Такого задания нет")



    elif x == 0:
        print("Пока")
    else:

        print("Такого задания нет")
