#!/usr/bin/env python3
"""      turtle-example-suite:

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses:
(1) a tree-generator, where the drawing is
quasi the side effect, whereas the generator
always yields None.
(2) Turtle-cloning: At each branching point
the current pen is cloned. So in the end
there are 1024 turtles.
"""
from time import perf_counter as clock
from turtle import Turtle, exitonclick


def tree(plist, length, alpha, factor):
    """ plist is list of pens
    'length' is length of branch
    'alpha' is half of the angle between 2 branches
    'factor' is factor by which branch is shortened
    from level to level."""
    if length > 3:
        lst = []
        for p in plist:
            p.forward(length)
            q = p.clone()
            p.left(alpha)
            q.right(alpha)
            lst.append(p)
            lst.append(q)
        for _ in tree(lst, length * factor, alpha, factor):
            yield None


def make_tree():
    p = Turtle()

    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(30, 0)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    t = tree([p], 200, 65, 0.6375)
    for _ in t:
        pass


def main():
    a = clock()
    make_tree()
    b = clock()
    return f"done: {(b - a):.2f} sec."


if __name__ == "__main__":

    msg = main()
    print(msg)
    exitonclick()
