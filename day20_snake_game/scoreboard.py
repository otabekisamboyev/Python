from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score_board()
