import turtle as t
import random

screen = t.Screen()
t.colormode(255)
circle = t.Turtle()

circle.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        circle.color(random_color())
        circle.circle(100)
        current_heading = circle.heading()
        circle.setheading(current_heading + 5)


draw_spirograph(5)
screen.exitonclick()
