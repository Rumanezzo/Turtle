from turtle import *

setup(0.99, 0.9, 0, 0)
bgcolor('black')  # Цвет Фона
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(0)  # Скорость Движения
color('white', 'black')

# Начало Программы

length = numinput('Длина Шага', 'Введите [3..10]', 5)
angle = numinput('Угол Поворота', 'Введите [10..175]', 60)
increment = numinput('Прирост Линии', 'Введите [1..5]', 3)
times = numinput('Сколько Линий', 'Введите [5..200]', 40)


def spiral(length_, angle_, increment_, times_):
    fd(length_)
    rt(angle_)
    if times_ == 0:
        return
    spiral(length_ + increment_, angle_, increment, times_ - 1)


spiral(length, angle, increment, times)

# Конец Программы
exitonclick()
