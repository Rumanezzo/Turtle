import turtle


def make_window(clr='grey', title="Tess, Alex, Mari and Mike"):
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
    wn.title(f'Tess задета по координатам ({x}, {y})')
    tess.lt(42)
    tess.fd(80)


def handler_alex(x, y):
    wn.title(f'Alex задет по координатам ({x}, {y})')
    alex.rt(84)
    alex.fd(110)


def handler_mari(x, y):
    wn.title(f'Mari задета по координатам ({x}, {y})')
    mari.lt(42)
    mari.fd(80)


def handler_mike(x, y):
    wn.title(f'Mike задет по координатам ({x}, {y})')
    mike.rt(84)
    mike.fd(110)


turtle.setup(0.99, 0.9, 0, 0)
wn = make_window(title='Ловим Мышиные Клики!')

tess = make_turtle(clr='blue')
alex = make_turtle(clr='yellow')
mari = make_turtle(clr='red')
mike = make_turtle(clr='green')

alex.pu()
tess.pu()
mari.pu()
mike.pu()

alex.fd(200)
tess.lt(180)
tess.fd(200)

mari.rt(90)
mari.fd(200)

mike.rt(-90)
mike.fd(200)

alex.pd()
tess.pd()
mari.pd()
mike.pd()

tess.onclick(handler_tess)
alex.onclick(handler_alex)
mari.onclick(handler_mari)
mike.onclick(handler_mike)

wn.mainloop()
