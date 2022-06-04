import turtle
from random import randint

# screen settings
width, height = 1790, 890
screen = turtle.Screen()
screen.setup(width, height, 0, 0)

screen.bgpic('moon.gif')
screen.delay(0)

# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.penup()
leo.setpos(width // 6, -height // 4 - 25)
leo.pendown()
leo.color('green')
# l-system settings
gens = 13
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 85

stack = []
colors = [0.35, 0.2, 0.0]
thickness = 20


def angle():
    return randint(0, 45)


def apply_rules(axiom_):
    return ''.join([rule_1 if _ == chr_1 else _ for _ in axiom_])


def get_result(gens_, axiom_):
    for gen in range(gens_):
        axiom_ = apply_rules(axiom_)
    return axiom_


axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
for _ in axiom:
    leo.color(*colors)
    if _ == 'F' or _ == 'X':
        leo.forward(step)
    elif _ == '@':
        step -= 6
        colors[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif _ == '+':
        leo.right(angle())
    elif _ == '-':
        leo.left(angle())
    elif _ == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, colors[1]))
    elif _ == ']':
        angle_, pos_, thickness, step, colors[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()
