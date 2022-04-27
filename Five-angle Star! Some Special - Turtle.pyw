from TurtleSetup import *


setup(width=1.0, height=0.85)

# Начало Программы
def polygon(size, n):
    for x in range(n):
        fd(size)
        rt(360 // n)


def triangle(size):
    polygon(size, 3)


def star(size=120, n=5):
    for x in range(n):
        triangle(size)
        fd(size)
        lt(360 // n)


def pos():
    pu()
    rt(90)
    fd(75)
    lt(125)
    pd()


def cmp1(size=120, n=6, m=9):
    for x in range(n):
        star(size, m)
        rt(360 // n)


cmp1(66, 6, 9)
# Конец Программы
exitonclick()
