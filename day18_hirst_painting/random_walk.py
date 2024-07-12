import turtle as t
import random

screen = t.Screen()
t.colormode(255)
screen.bgcolor(89, 49, 123)

line = t.Turtle()
line.pensize(12)
line.speed(10)
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_turn(turns):
    angle = random.choice(turns)
    line.color(random_color())
    line.right(angle)


for _ in range(100):
    line.forward(20)
    random_turn(direction)

"""Teacher's solution
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r/255, g/255, b/255)
    return random_color
for _ in range(200):
    line.color(random_color())
    line.forward(30)
    line.right(random.choice(direction))
"""

screen.exitonclick()
