from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.speed(0)
        self.color("black")
        self.penup()
        self.hideturtle()

        self.goto(-200, 250)
        self.write(arg=f"Level {self.level}:", move=False, align=ALIGN, font=FONT)

    def increase_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(arg=f"Level {self.level}:", move=False, align=ALIGN, font=FONT)

    def add_level(self):
        self.level += 1
        self.increase_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'Game Over!', move=False, align=ALIGN, font=FONT)