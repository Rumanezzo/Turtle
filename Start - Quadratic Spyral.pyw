from turtle import *

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine", "bisque", "burlywood",
          "chartreuse", "magenta", "moccasin", "navy", "plum", "tan", "thistle", "turquoise", "tomato", "brown",
          "salmon", "gold", "lavender", "gainsboro", "cornsilk", "ivory", "linen", "honeydew", "maroon", "azure",
          "sienna", "peru"]
setup(0.9, 0.75)
title('Непричесанные спирали')
shape('turtle')
color('white')
bgcolor('black')
width(0)
speed(0)
ht()


def spiral():
    for i in range(len(colors)):
        color(colors[i % len(colors)])
        fd(30 + 10 * i)
        lt(90)
        width(i % 5)
    pu()
    home()
    pd()


def main(n):
    for i in range(n):
        spiral()
        rt(360 / n + 360 / n * i)


n_ = int(numinput('Сколько спиралей?', '3-20', 5, 3, 20))
main(n_)

exitonclick()
