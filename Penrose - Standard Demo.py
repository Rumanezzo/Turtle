from turtle import *
from math import cos, pi
from time import perf_counter as clock, sleep

f = (5 ** 0.5 - 1) / 2.0  # (sqrt(5) - 1) / 2 -- golden ratio
d = 2 * cos(3 * pi / 10)
tile_dict = {}
setup(0.99, 0.9, 0, 0)


def kite(length):
    fl = f * length
    lt(36)
    fd(length)
    rt(108)
    fd(fl)
    rt(36)
    fd(fl)
    rt(108)
    fd(length)
    rt(144)


def dart(length):
    fl = f * length
    lt(36)
    fd(length)
    rt(144)
    fd(fl)
    lt(36)
    fd(fl)
    rt(144)
    fd(length)
    rt(144)


def inflate_kite(length, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px, 3), round(py, 3)
        tile_dict[(h, x, y)] = True
        return
    fl = f * length
    lt(36)
    inflate_dart(fl, n - 1)
    fd(length)
    rt(144)
    inflate_kite(fl, n - 1)
    lt(18)
    fd(length * d)
    rt(162)
    inflate_kite(fl, n - 1)
    lt(36)
    fd(length)
    rt(180)
    inflate_dart(fl, n - 1)
    lt(36)


def inflate_dart(length, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px, 3), round(py, 3)
        tile_dict[(h, x, y)] = False
        return
    fl = f * length
    inflate_kite(fl, n - 1)
    lt(36)
    fd(length)
    rt(180)
    inflate_dart(fl, n - 1)
    lt(54)
    fd(length * d)
    rt(126)
    inflate_dart(fl, n - 1)
    fd(length)
    rt(144)


def draw(length, n, th=2):
    clear()
    length = length * f ** n
    shapesize(length / 100.0, length / 100.0, th)
    for k in tile_dict:
        h, x, y = k
        setpos(x, y)
        setheading(h)
        if tile_dict[k]:
            shape("kite")
            color("black", (0, 0.75, 0))
        else:
            shape("dart")
            color("black", (0.75, 0, 0))
        stamp()


def sun(length, n):
    for i in range(5):
        inflate_kite(length, n)
        lt(72)


def star(length, n):
    for i in range(5):
        inflate_dart(length, n)
        lt(72)


def make_shapes():
    tracer(0)
    begin_poly()
    kite(100)
    end_poly()
    register_shape("kite", get_poly())
    begin_poly()
    dart(100)
    end_poly()
    register_shape("dart", get_poly())
    tracer(1)


def start():
    reset()
    ht()
    pu()
    make_shapes()
    resizemode("user")


def test(length=200, n=4, fun=sun, start_pos=(0, 0), th=2):
    global tile_dict
    goto(start_pos)
    setheading(0)
    tile_dict = {}
    tracer(0)
    fun(length, n)
    draw(length, n, th)
    tracer(1)
    nk = len([x for x in tile_dict if tile_dict[x]])
    nd = len([x for x in tile_dict if not tile_dict[x]])
    print("%d kites and %d darts = %d pieces." % (nk, nd, nk + nd))


def demo(fun=sun):
    start()
    for i in range(8):
        a = clock()
        test(300, i, fun)
        b = clock()
        t = b - a
        if t < 2:
            sleep(2 - t)


def main():
    title('Мозаики Penrose "with kites and arrows"')
    mode("logo")
    bgcolor(0.3, 0.3, 0)
    demo(sun)
    sleep(2)
    demo(star)
    pencolor("black")
    goto(0, -200)
    pencolor(0.65, 0.85, 0.9)
    write("Чуть-чуть терпения...",
          align="center", font=('FreeMono', 36, 'bold'))
    test(600, 8, start_pos=(70, 117))
    return "Done"


if __name__ == "__main__":
    msg = main()
    title('Щелкните по экрану для завершения...')
    exitonclick()
