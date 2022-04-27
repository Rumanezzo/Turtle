from turtle import *

bgcolor('black')
speed(0)
setup(0.9, 0.8)
colors = ['red', 'yellow', 'blue', 'green']
ht()

name = textinput('Введите своё имя', 'Как тебя зовут?') or "Василиса Премудрая"
for x in range(264):
    color(colors[x % 4])
    up()
    fd(x * 4)
    down()
    write(name, font=('FreeMono', int((x + 4) / 4), 'bold'))
    lt(92)
exitonclick()
