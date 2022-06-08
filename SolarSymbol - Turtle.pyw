from turtle import *

title('Внезапная Находка в виде Солярного Символа!')  # Заголовок
mode('logo')  # Черепашка на север
bgcolor('black')  # Цвет Фона
shape('turtle')  # Форма Черепашки
setup(0.99, 0.9, 0, 0)
speed(0)  # Скорость Движения
color('white', 'red')


# Начало Программы

def six1(size):
    for x in range(6):
        width(6 // 2 ** x + 1)
        fd(size)
        lt(60)
        fd(size // 2)
        bk(size // 2)
        rt(120)


def poly(n, size):
    for x in range(n, 0, -1):
        width(x)
        fd(size)
        rt(360 // n)


def sun(count, n):
    for x in range(3 * count):
        poly(n, 100)
        lt(120 // count)


# poly(5, 180)
sun(15, 12)

# Конец Программы
exitonclick()
