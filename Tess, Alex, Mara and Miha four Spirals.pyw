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


def spiro(name, clock=0):
    name.penup()
    size = 20
    if clock == 0:
        def f():
            name.rt(24)
    else:
        def f():
            name.lt(24)
    for i in range(30):
        name.stamp()
        size += 3
        name.shapesize(1, 1, i + 1)
        name.fd(size)
        f()


def ex(): wn.bye()


turtle.setup(0.9, 0.8)  # Установка Размеров Окна - Пользуемся везде где можно!
wn = make_window()
tess = make_turtle('blue')
alex = make_turtle('yellow')
mara = make_turtle('red')
miha = make_turtle('green')

spiro(tess, 0)
spiro(alex, 1)
mara.rt(45)
spiro(mara, 0)
miha.lt(45)
spiro(miha, 1)
miha.ht()
miha.goto(-500, 280)
miha.color('black')
miha.write('Нажмите Клавишу [q] или кликните Мышкой!', font=('FreeMono', 14, 'bold'))
wn.onkey(ex, 'q')
wn.listen()
wn.exitonclick()
# wn.mainloop()
