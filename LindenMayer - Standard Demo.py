from turtle import *


def replace(seq, replacement_rules, n):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + replacement_rules.get(element, element)
        seq = newseq
    return seq


def draw(commands, rules):
    for b in commands:
        try:
            rules[b]()
        except TypeError:
            try:
                draw(rules[b], rules)
            except StopIteration:
                pass


def main():
    # Example 1: Snake

    def r():
        right(45)

    def lo():
        left(45)

    def f():
        forward(7.5)

    snake_rules = {"-": r, "+": lo, "f": f, "b": "f+f+f--f--f+f+f"}
    snake_replacement_rules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacement_rules, 3)

    reset()
    speed(3)
    tracer(1, 0)
    ht()
    up()
    backward(195)
    down()
    draw(drawing, snake_rules)

    from time import sleep
    sleep(3)

    # Example 2: Anklets of Krishna

    def a():
        color("red")
        circle(10, 90)

    def b():
        from math import sqrt
        color("black")
        li = 5 / sqrt(2)
        forward(li)
        circle(li, 270)
        forward(li)

    def f1():
        color("green")
        forward(10)

    krishna_rules = {"a": a, "b": b, "f": f1}
    krishna_replacement_rules = {"a": "a" + "fb" + "fa", "b": "a" + "fb" * 3 + "fa"}
    krishna_start = "fb" * 4

    reset()
    speed(0)
    tracer(3, 0)
    ht()
    left(45)
    drawing = replace(krishna_start, krishna_replacement_rules, 3)
    draw(drawing, krishna_rules)
    tracer(1)
    return "Done!"


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
