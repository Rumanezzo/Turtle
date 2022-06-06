import turtle


def make_window(clr='grey', title='Идёт Загрузка...'):
    w = turtle.Screen()
    w.bgcolor(clr)
    w.title(title)
    return w


def make_turtle(clr='red', sz=5, shp='turtle', pos_x=0, pos_y=0):
    t = turtle.Turtle()
    t.color(clr)
    t.pensize(sz)
    t.shape(shp)

    t.pu()
    t.ht()
    t.goto(pos_x, pos_y)
    t.st()
    return t


def spiro(name, clock=0):
    name.penup()
    size = 20
    for i in range(30):
        name.stamp()
        size += 3
        name.shapesize(1, 1, i + 1)
        name.fd(size)
        name.rt(24 * clock)


turtle.setup(0.99, 0.9, 0, 0)  # Установка Размеров Окна относительное - пользуемся везде где можно!
wn = make_window()
c = ('blue', 'yellow', 'red', 'green', 'cyan', 'magenta', 'black', 'white')
x = (0, 0, 150, 150, -150, -150, 300, -300)
y = (0, 0, 150, -150, 150, -150, 0, 0)
s = (1, -1, 2, -2, 2, -2, 2, -2)

for clr0, i0, j, k in zip(c, x, y, s):
    t0 = make_turtle(clr0, pos_x=i0, pos_y=j)
    wn.title(f'Создаем несколько черепашек и пусть они крутят спирали! -> {clr0} turtle is going!!!')
    spiro(t0, k)
wn.title('Для завершения нажмите клавишу q, или просто кликнете по экрану левой клавишей мышки!')

wn.onkey(wn.bye, 'q')
wn.listen()

wn.exitonclick()
