from turtle import *
from datetime import datetime

s_hand = Turtle()
m_hand = Turtle()
h_hand = Turtle()
writer = Turtle()


def jump(distance_, angle_=0):
    penup()
    right(angle_)
    forward(distance_)
    left(angle_)
    pendown()


def hand(length_, angle_):
    fd(length_ * 1.15)
    rt(90)
    fd(angle_ / 2.0)
    lt(120)
    fd(angle_)
    lt(120)
    fd(angle_)
    lt(120)
    fd(angle_ / 2.0)


def make_hand_shape(name, length_, angle_):
    reset()
    jump(-length_ * 0.15)
    begin_poly()
    hand(length_, angle_)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)


def clock_face(radius):
    reset()
    pensize(6)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius - 25)
        else:
            dot(3)
            jump(-radius)
        rt(6)


def setup():
    global s_hand, m_hand, h_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand", 130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clock_face(160)

    s_hand.shape("second_hand")
    s_hand.color("gray20", "orange")

    m_hand.shape("minute_hand")
    m_hand.color("blue1", "brown")

    h_hand.shape("hour_hand")
    h_hand.color("blue3", "green")

    for hand_ in s_hand, m_hand, h_hand:
        hand_.resizemode("user")
        hand_.shapesize(1, 1, 3)
        hand_.speed(0)
    ht()

    writer.ht()
    writer.pu()
    writer.bk(85)


def weekday(t):
    weekday_ = ["Понедельник", "Вторник", "Среда",
                "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return weekday_[t.weekday()]


def date_set(z):
    month = ["Янв.", "Фев.", "Март", "Апр.", "Май", "Июнь",
             "Июль", "Авг.", "Сен.", "Окт.", "Ноябрь.", "Дек."]
    j = z.year
    m = month[z.month - 1]
    t = z.day
    return f'{t} {m} {j}'


def tick():
    time = datetime.today()
    second = time.second + time.microsecond * 0.000001
    minute = time.minute + second / 60.0
    hour = time.hour + minute / 60.0
    try:
        tracer(False)
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(weekday(time),
                     align="center", font=("neucha", 15, "bold"))
        writer.back(150)
        writer.write(date_set(time),
                     align="center", font=("neucha", 15, "bold"))
        writer.forward(85)
        tracer(True)
        s_hand.setheading(6 * second)
        m_hand.setheading(6 * minute)
        h_hand.setheading(30 * hour)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass


def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "Наслаждаемся работающими часиками"


if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)

    exitonclick()
