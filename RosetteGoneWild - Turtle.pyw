from turtle import *

colors = ['yellow', 'blue', 'red', 'green']
shape('turtle')
ht()
bgcolor('black')
width(0)
speed(0)

circles = int(numinput('Количество окружностей', 'Сколько окружностей в вашей розетке? [2..100]', 3))

for x in range(circles):
    for i in range(4):
        color(colors[i])
        circle(175 - 50 * i)

    lt(360 / circles)
    width(x)

exitonclick()
