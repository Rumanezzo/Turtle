import random
# import time
import turtle

joe = turtle.Turtle()


def star_fill(n, length):
    joe.lt(random.randint(10, 350))
    joe.begin_fill()
    if n % 2 != 0:
        for _ in range(n):
            joe.fd(length)
            angle = n // 2 * 360 / n
            joe.lt(angle)
    joe.end_fill()


color = ('white', 'green', 'yellow', 'brown', 'red', 'grey', 'magenta', 'cyan', "blue",
         "orange", "purple", "pink", "violet")


window = turtle.Screen()
window.bgcolor('black')
window.setup(1280, 600)

joe.speed(0)
joe.ht()


def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    size_ = random.randint(8, 16)
    vertex_ = random.choice([5, 7, 9])
    joe.color(random.choice(color))
    star_fill(vertex_, size_)
    # window.title(f'Нарисуем звездное небо координаты звезд x = {x:4d}, y = {y:4d}')


for i in range(100):
    x_pos = random.randint(-window.window_width() // 2 + 30, window.window_width() // 2 - 30)
    y_pos = random.randint(-window.window_height() // 2 + 30, window.window_height() // 2 - 30)
    move(x_pos, y_pos)
    window.title(f'Нарисуем звездное небо. {i + 1}-я звездочка с координатами x = {x_pos:4d}, y = {y_pos:4d}')

window.onclick(move)
window.listen()
window.mainloop()
