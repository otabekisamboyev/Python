from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(f"You've chose {user_bet} color...")
colors = ["purple", "yellow", "black", "red", "blue"]
y_position = [-100, -50, 0, 50, 100]
turtles_list = []

for turtle_index in range(0, 5):
    donatello = Turtle(shape="turtle")
    turtles_list.append(donatello)
    donatello.color(colors[turtle_index])
    donatello.penup()
    donatello.goto(x=-200, y=y_position[turtle_index])


if user_bet and user_bet in colors:
    is_race_on = True
else:
    print(f"There is not {user_bet} color turtle!")

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")
        random_distances = random.randint(0, 10)
        turtle.forward(random_distances)

screen.exitonclick()
