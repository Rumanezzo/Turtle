from turtle import *

bgcolor('black')  # Цвет Фона
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(5)  # Скорость Движения
# ht()                 # Спрятать Черепашку
pen(pencolor='white')  # Настройки Пера

ratio = numinput('Плотность Звёзд', 'Введите Коэффициент [1..5]', 2)
r = int(ratio)

if r < 4:
    speed(4 * r)
else:
    speed(0)


def five_star():
    for i in range(5):
        rt(144)
        fd(200)


for x in range(10 * r):
    five_star()
    rt(36 // r)

# Конец Программы
exitonclick()
