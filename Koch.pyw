import turtle

# screen settings
ratio_w, ratio_h = 0.99, 0.99
width, height = 1920, 1080
screen = turtle.Screen()
screen.setup(ratio_w, ratio_h, 0, 0)

screen.bgcolor('black')
screen.delay(0)

# turtle settings
leo = turtle.Turtle()
leo.pensize(1)
leo.speed(0)
leo.ht()
leo.setpos(-width // 6, height // 6)
leo.color('gold')

# l-system settings
gens = 6
axiom = 'F++F++F'
chr_1, rule_1 = 'F', 'F-F++F-F'
step = 600
angle = 60


def apply_rules(axiom_):
    return ''.join([rule_1 if _ == chr_1 else _ for _ in axiom_])


def get_result(gens_, axiom_):
    for _ in range(gens_):
        axiom_ = apply_rules(axiom_)
    return axiom_


for gen in range(gens):
    turtle.delay(0)
    turtle.ht()
    turtle.pencolor('white')
    turtle.pu()
    turtle.goto(-width // 10, 0)
    
    turtle.pd()
    turtle.write(f'generation: {gen}', align="left", font=("FreeMono", 33, "bold"))

    leo.setheading(0)

    leo.goto(-width // 6, height // 6)
    leo.clear()

    length = step / pow(3, gen)
    for _ in axiom:
        if _ == chr_1:
            leo.forward(length)
        elif _ == '+':
            leo.right(angle)
        elif _ == '-':
            leo.left(angle)

    axiom = apply_rules(axiom)

screen.exitonclick()
