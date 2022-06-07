from turtle import Turtle, Screen


class Trt(Turtle):
    def __init__(self, color1='white', color2='green'):
        super().__init__()
        self.color(color1, color2)
        self.shape('turtle')
        self.width(3)
        self.speed(5)


s0 = Screen()
s0.title('Черепашья Графика - предустановленные характеристики')
s0.setup(0.99, 0.9, 0, 0)  # Установка Размеров Окна на весь экран - пользуемся везде где можно!
s0.mode('logo')  # Черепашка на север
s0.bgcolor('gray')

t0 = Trt()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine", "bisque",
          "burlywood", "chartreuse", "magenta", "moccasin", "navy", "plum", "tan", "thistle", "turquoise", "tomato",
          "brown", "salmon", "gold", "lavender", "gainsboro", "cornsilk", "ivory", "linen", "honeydew", "maroon",
          "azure", "sienna", "peru", "lightGrey", "grey"]


if __name__ == '__main__':
    s0.exitonclick()
