from turtle import Turtle, colormode, tracer, exitonclick
from random import randrange
from time import perf_counter as clock


def sym_random(n):
    return randrange(-n, n + 1)


def randomize(branch_list, angle_dist, size_dist):
    return [(angle + sym_random(angle_dist),
             size_factor * 1.01 ** sym_random(size_dist))
            for angle, size_factor in branch_list]


def random_fd(t, distance, parts, angle_dist):
    for i in range(parts):
        t.left(sym_random(angle_dist))
        t.forward((1.0 * distance) / parts)


def tree(tlist, size, level, width_factor, branch_lists, angle_dist=10, size_dist=5):
    size_factor = 0
    if level > 0:
        lst = []
        brs = []
        for t, branch_list in list(zip(tlist, branch_lists)):
            t.pensize(size * width_factor)
            t.pencolor(255 - (180 - 11 * level + sym_random(15)),
                       180 - 11 * level + sym_random(15),
                       0)
            t.pendown()
            random_fd(t, size, level, angle_dist)
            yield 1
            for angle, size_factor in branch_list:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branch_list, angle_dist, size_dist))
                t.right(angle)
        for _ in tree(lst, size * size_factor, level - 1, width_factor, brs,
                      angle_dist, size_dist):
            yield None


def start(t, x, y):
    colormode(255)
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x, y)
    t.pendown()


def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20, -208)
    t = tree([pen], 80, level, 0.1, [[(45, 0.69), (0, 0.65), (-45, 0.71)]])
    return t


def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree([pen], 120, level, 0.1, [[(45, 0.69), (-45, 0.71)]])
    return t


def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree([pen], 100, level, 0.1, [[(45, 0.7), (0, 0.72), (-45, 0.65)]])
    return t


def main():
    p = Turtle()
    p.ht()
    tracer(75, 0)
    u = doit1(6, Turtle(undobuffersize=1))
    s = doit2(7, Turtle(undobuffersize=1))
    t = doit3(5, Turtle(undobuffersize=1))
    a = clock()
    while True:
        done = 0
        for b in u, s, t:
            try:
                b.__next__()
            except StopIteration:
                done += 1
        if done == 3:
            break

    tracer(1, 10)
    b = clock()
    return "runtime: %.2f sec." % (b - a)


if __name__ == '__main__':
    main()
    exitonclick()
