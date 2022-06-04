import turtle


def make_window(clr_='grey', title=''):
    w = turtle.Screen()
    w.bgcolor(clr_)
    w.title(title)
    return w


def make_turtle(clr_='red', sz=5, shp='turtle', pos_x=0, pos_y=0):
    t_ = turtle.Turtle()
    t_.color(clr_)
    t_.pensize(sz)
    t_.shape(shp)

    t_.pu()
    t_.ht()
    t_.goto(pos_x, pos_y)
    t_.st()
    return t_


def spiro(name, clock=0):
    name.penup()
    size = 20
    for i_ in range(30):
        name.stamp()
        size += 3
        name.shapesize(1, 1, i_ + 1)
        name.fd(size)
        name.rt(24 * clock)


turtle.setup(0.9, 0.9)  # Установка Размеров Окна относительное - пользуемся везде где можно!
wn = make_window()
c = ('blue', 'yellow', 'red', 'green', 'cyan', 'magenta', 'black', 'white')
x = (0, 0, 150, 150, -150, -150, 300, -300)
y = (0, 0, 150, -150, 150, -150, 0, 0)
s = (1, -1, 2, -2, 2, -2, 2, -2)

for clr, i, j, k in zip(c, x, y, s):
    t = make_turtle(clr, pos_x=i, pos_y=j)
    wn.title(f'Создаем несколько черепашек и пусть они крутят спирали! -> {clr} turtle is going!!!')
    spiro(t, k)
wn.title('Для завершения нажмите клавишу q, или просто кликнете по экрану левой клавишей мышки!')

wn.onkey(wn.bye, 'q')
wn.listen()

wn.exitonclick()
