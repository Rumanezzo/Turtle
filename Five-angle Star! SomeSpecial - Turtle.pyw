from TurtleSetup import *


def polygon(t, size, n=5):
    for x in range(n):
        t.fd(size)
        t.rt(360 // n)


def triangle(t, size):
    polygon(t, size, 3)


def star_exp(t=t0, s=s0, size=120, n=5):
    n0 = n
    tess, leo = Trt('blue', 'yellow'), Trt('orange', 'red')

    r = 360 % n

    if r:
        while 360 % n:
            n -= 1
    s.title(f'Вы ввели n = {n0}, а значит рисуем {n}-угольник')
    leo.rt(90)
    for _ in range(n):
        triangle(t, size)
        triangle(tess, size // 2)
        triangle(leo, size // 3)

        t.fd(size)
        tess.fd(size // 2)
        leo.fd(size // 3)
        t.lt(360 // n)
        tess.rt(360 // n)
        leo.rt(360 // n)

    t.rt(30)
    tess.lt(30)
    leo.rt(90)

    t.pu()
    tess.pu()
    leo.pu()

    t.speed(1)
    tess.speed(1)
    leo.speed(1)

    t.fd(100)
    tess.fd(100)
    leo.fd(100)


def super_star(t, s=s0, size=120, n=6, m=9):
    for x in range(n):
        star(t, s, size, m)
        t.rt(360 // n)


def star(t=t0, s=s0, size=120, n=5):
    n0 = n

    r = 360 % n

    if r:
        while 360 % n:
            n -= 1
    s.title(f'Вы ввели n = {n0}, а значит рисуем {n}-угольник')

    for _ in range(n):
        triangle(t, size)
        t.fd(size)
        t.lt(360 // n)


super_star(t0, s0, size=55, n=11, m=18)

s0.exitonclick()
