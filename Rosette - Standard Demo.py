from turtle import Screen, Turtle, exitonclick
from time import perf_counter as clock, sleep


def mn_eck(p, ne, sz):
    turtle_list = [p]
    # create ne-1 additional turtles
    for i in range(1, ne):
        q = p.clone()
        q.rt(360.0 / ne)
        turtle_list.append(q)
        p = q
    for i in range(ne):
        c = abs(ne / 2.0 - i) / (ne * .7)

        for t in turtle_list:
            t.rt(360. / ne)
            t.pencolor(1 - c, 0, c)
            t.fd(sz)


def main():
    s = Screen()
    s.title('Rosette - Standard Demo')
    s.bgcolor("black")
    p = Turtle()
    p.speed(0)
    p.hideturtle()
    p.pencolor("red")
    p.pensize(3)

    s.tracer(36, 0)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et - at

    sleep(1)

    at = clock()
    while any(t.undobufferentries() for t in s.turtles()):
        for t in s.turtles():
            t.undo()
    et = clock()
    return f"runtime: {(z1 + et - at):.3f} sec"


if __name__ == '__main__':
    msg = main()
    print(msg)
    exitonclick()
