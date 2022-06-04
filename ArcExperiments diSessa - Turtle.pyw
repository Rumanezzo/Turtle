from turtle import *

title("Эксперименты с Дугами и Цветами!")  # Заголовок
mode("logo")  # Черепашка на север
bgcolor("black")  # Цвет Фона
color("gray", "green")  # Цвет Линии и Заливки
shape("turtle")  # Форма Черепашки
width(5)  # Ширина Линии
speed(0)  # Скорость Движения

colors = (
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
)

# Начало секции определения функций


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


def color_demo():
    width(100)
    pu()
    lt(90)
    fd(633)
    rt(180)
    pd()
    for x in range(len(colors)):
        color(colors[x])
        fd(38)


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


def sun(size):
    for x in range(9):
        ray(size)
        rt(160)


def centre(x=0, y=0):
    pu()
    setpos(x, y)
    pd()


def horns():
    arc_l(1, 90)
    arc_r(1, 90)
    centre()

    arc_r(1, 90)
    arc_l(1, 90)
    centre()


def contour():
    w = window_width() // 2 - 16
    h = window_height() // 2 - 16
    setpos(w, h)
    stamp()
    setpos(-w, h)
    stamp()
    setpos(w, -h)
    stamp()
    setpos(-w, -h)
    stamp()
    setpos(0, 0)


def shape_probe():
    shape("square")
    shapesize(16, 8)
    shearfactor(-0.25)
    shapetransform()


def new_poly(side, angle):
    for x in range(5):
        fd(side)
        rt(angle)
        fd(side)
        rt(2 * angle)


# Конец секции определения функций
contour()
exitonclick()
