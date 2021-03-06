from turtle import *

title('Интерактивная Черепашка!')  # Заголовок
mode('logo')  # Черепашка на север
bgcolor('black')  # Цвет Фона
color('green', 'blue')  # Цвет Линии и Заливки
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(0)  # Скорость Движения

colors = ["aquamarine", "bisque", "burlywood", "chartreuse", "magenta", "moccasin", "navy", "plum", "tan", "thistle",
          "turquoise", "tomato", "red", "green", "blue", "orange", "purple", "pink", "yellow", "brown", "violet",
          "salmon", "gold", "lavender", "gainsboro", "cornsilk", "ivory", "linen", "honeydew", "maroon", "azure",
          "sienna", "peru"]


def up():
    fd(50)


def down():
    bk(50)


def left():
    lt(30)


def right():
    rt(30)


onkey(up, "Up")
onkey(left, 'Left')
onkey(right, 'Right')
onkey(down, 'Down')

listen()
exitonclick()
