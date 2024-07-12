from turtle import Turtle, Screen
import random


shapes = Turtle()
colors_data = ["IndianRed3", "chartreuse4", "OliveDrab4", "RosyBrown2", "DodgerBlue", "MidnightBlue", "MediumVioletRed",
               "CadetBlue2", "bisque1", "bisque2", "bisque3", "bisque4", "DarkOrchid2", "DeepPink3", "DarkSalmon"]

"""Draw from triangle until decagon"""
shape = 3
num_sides = 3
while shape <= 10:
    color = random.choice(colors_data)
    shapes.color(color)
    angle = 360 / num_sides
    for n in range(num_sides):
        shapes.forward(50)
        shapes.right(angle)
    num_sides += 1
    shape += 1


"""Teacher's solution for drawing shapes


def draw_shape(num_sides):
    angle = 360 / num_sides
    shapes.color(random.choice(colors_data))
    for _ in range(num_sides):
        shapes.forward(50)
        shapes.right(angle)


for shape_sides_n in range(3, 11):
    draw_shape(shape_sides_n)
"""

screen = Screen()
screen.exitonclick()
