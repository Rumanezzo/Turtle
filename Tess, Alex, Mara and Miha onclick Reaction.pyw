import turtle


def make_window(clr='grey', title="Tess, Alex, Mara and Miha"):
    w = turtle.Screen()
    w.bgcolor(clr)
    w.title(title)
    return w


def make_turtle(clr='red', sz=5, shp='turtle'):
    t = turtle.Turtle()
    t.color(clr)
    t.pensize(sz)
    t.shape(shp)
    return t


def handler_tess(x, y):
    wn.title('Tess задета по координатам ({0}, {1})'.format(x, y))
    tess.lt(42)
    tess.fd(80)


def handler_alex(x, y):
    wn.title('Alex задет по координатам ({0}, {1})'.format(x, y))
    alex.rt(84)
    alex.fd(110)


def handler_mara(x, y):
    wn.title('Mara задета по координатам ({0}, {1})'.format(x, y))
    mara.lt(42)
    mara.fd(80)


def handler_miha(x, y):
    wn.title('Miha задет по координатам ({0}, {1})'.format(x, y))
    miha.rt(84)
    miha.fd(110)


turtle.setup(1024, 600)
wn = make_window(title='Ловим Мышиные Клики!')

tess = make_turtle(clr='blue')
alex = make_turtle(clr='yellow')
mara = make_turtle(clr='red')
miha = make_turtle(clr='green')

alex.pu()
tess.pu()
mara.pu()
miha.pu()

alex.fd(200)
tess.fd(-200)

mara.rt(90)
mara.fd(200)

miha.rt(-90)
miha.fd(200)

alex.pd()
tess.pd()
mara.pd()
miha.pd()

tess.onclick(handler_tess)
alex.onclick(handler_alex)
mara.onclick(handler_mara)
miha.onclick(handler_miha)

wn.mainloop()
