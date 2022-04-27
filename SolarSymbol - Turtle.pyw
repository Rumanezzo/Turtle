from turtle import *

title('Внезапная Находка в виде Солярного Символа!')  # Заголовок
mode('logo')  # Черепашка на север
bgcolor('black')  # Цвет Фона
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(5)  # Скорость Движения
pen(pencolor='white')  # Настройки Пера


# Начало Программы

def six1(size):
    for x in range(6):
        width(6 // 2 ** x + 1)
        fd(size)
        lt(60)
        fd(size // 2)
        bk(size // 2)
        rt(120)


def six(size):
    for x in range(6):
        width(6 // 2 ** x + 1)
        fd(size)
        rt(60)


def sun(count):
    for x in range(3 * count):
        six(100)
        lt(120 // count)


six(100)
sun(12)

# Конец Программы
exitonclick()
