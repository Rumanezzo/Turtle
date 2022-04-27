from turtle import *

s = Screen()
t = Turtle()
s.setup(0.9, 0.8)
s.title('Эксперименты с Орнаментами!')  # Заголовок
s.mode('logo')  # Черепашка на север
s.bgcolor('black')  # Цвет Фона


t.shape('turtle')  # Форма Черепашки
t.width(5)  # Ширина Линии
t.speed(0)  # Скорость Движения

t.pen(pencolor='white')  # Настройки Пера


# Начало Программы

def thing(turtle: Turtle, scale):
    for i in range(2):
        turtle.fd(4 * scale)
        turtle.rt(90)
    for i in range(2):
        turtle.fd(2 * scale)
        turtle.rt(90)
    turtle.fd(4 * scale)
    turtle.rt(90)
    for i in range(2):
        turtle.fd(scale)
        turtle.rt(90)
    turtle.fd(scale)


def thing1():
    for i in range(4):
        thing(t, 20)


def thing5():
    for i in range(5):
        thing(t, 18)
        t.rt(30)


def thing6():
    for i in range(6):
        thing(t, 30)
        t.rt(30)


def things():
    for i in range(6):
        thing1()
        t.rt(360 // 6)


things()

# Конец Программы
exitonclick()
