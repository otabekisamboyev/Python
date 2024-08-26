from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.l_score = 0
        self.r_score = 0
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGN, font=FONT)

    def add_score_left(self):
        self.l_score += 1
        self.increase_score()

    def add_score_right(self):
        self.r_score += 1
        self.increase_score()
