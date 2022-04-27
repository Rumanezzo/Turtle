# Внимание! Этот файл поместить в PythonPath\Lib или в папку с программой - приоритетнее
# После чего в проектах можно использовать import TurtleSetup с заданными настройками
from turtle import *


def main():
    exitonclick()


# Screen()  # Создание Экрана s
# title('Графика Черепашки!')  # Заголовок
setup(0.95, 0.75)  # Размер Активного Окна в процентах от экрана в центре
mode('logo')  # Черепашка на север
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine", "bisque", "burlywood",
          "chartreuse", "magenta", "moccasin", "navy", "plum", "tan", "thistle", "turquoise", "tomato", "brown",
          "salmon", "gold", "lavender", "gainsboro", "cornsilk", "ivory", "linen", "honeydew", "maroon", "azure",
          "sienna", "peru", "lightGrey"]


bgcolor(colors[-1])  # Цвет Фона
# Turtle() # Создание Черепашки
color('white', 'red')  # Цвет Линии и Заливки
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(5)  # Скорость Движения

# Начало секции определения функций


# Конец секции определения функций
# Начало Секции Вызовов

if __name__ == '__main__':
    main()

# Конец Секции Вызовов
