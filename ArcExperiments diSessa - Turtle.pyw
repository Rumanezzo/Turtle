from turtle import *
from random import shuffle

setup(0.99, 0.9, 0, 0)  # Установка Размеров Окна относительное - пользуемся везде где можно!
title("Эксперименты с Дугами и Цветами!")  # Заголовок
mode("logo")  # Черепашка на север
bgcolor("black")  # Цвет Фона
color("gray", "green")  # Цвет Линии и Заливки
shape("circle")  # Форма Черепашки
shapesize(0.5)
ht()
speed(0)  # Скорость Движения

w = window_width() // 2 - 16
h = window_height() // 2 - 16

colors = [
    "aquamarine",
    "bisque",
    "burlywood",
    "chartreuse",
    "magenta",
    "moccasin",
    "navy",
    "plum",
    "tan",
    "thistle",
    "turquoise",
    "tomato",
    "red",
    "green",
    "blue",
    "orange",
    "purple",
    "pink",
    "yellow",
    "brown",
    "violet",
    "salmon",
    "gold",
    "lavender",
    "gainsboro",
    "cornsilk",
    "ivory",
    "linen",
    "honeydew",
    "maroon",
    "azure",
    "sienna",
    "peru",
]

n_clr = len(colors)


# Начало секции определения функций

def sgn(n):
    return n // abs(n) if n != 0 else 0


def arc_r(r, deg):
    for x in range(deg):
        fd(r)
        rt(1)


def arc_l(r, deg):
    for x in range(deg):
        fd(r)
        lt(1)


def hammer(r=1, fill="maroon"):
    fillcolor(fill)
    begin_fill()

    for x in range(2):
        arc_l(r, 45)
        rt(90)
        arc_r(r, 45)
        rt(90)

    end_fill()


def veer():
    for _ in range(12):
        hammer(5, colors[_])
        rt(30)


def colorizer(w_line):
    width(w_line)
    rt(90)
    for _ in range(w_line // 2, window_height() + w_line, w_line):
        pu()
        goto(-window_width() // 2, window_height() // 2 - _)
        pd()
        shuffle(colors)
        for x in colors:
            color(x)
            fd(window_width() // n_clr + 1)


def petal(size=1):
    for x in range(2):
        arc_r(size, 60)
        rt(120)


def flower(size=1, k=2):
    for x in range(6 * k):
        petal(size)
        rt(60 / k)


def ray(r):
    for x in range(2):
        arc_l(r, 90)
        arc_r(r, 90)


def centre(x=0, y=0):
    pu()
    goto(x, y)
    setheading(0)
    pd()


def contour():
    for _ in range(200):
        global w, h
        w0, h0 = w, h
        if _ % 4 == 0 or _ % 4 == 3:
            w0, h0 = -w0, -h0
        elif _ % 4 == 1:
            h0 = -h0
        elif _ % 4 == 2:
            w0 = -w0
        goto(sgn(w0) * (abs((abs(w0) - _ * 10)) % w), sgn(h0) * abs((abs(h0) - _ * 10) % h))
        stamp()

    goto(0, 0)
    stamp()


def imagination(count):
    lng = (6, 4, 3, 2, 2)
    rot = (30, 60, 120, 150, 160)
    for _ in range(360 // count, 361, 360 // count):
        for i, j in zip(lng, rot):
            arc_r(i, j)
            rt(150)
            arc_l(i, j)
        centre()
        rt(_)
        title(f'Повернулись на {_} градусов')


# Секция Запуска Функций
imagination(5)

title(f'Работа окончена!')
exitonclick()
