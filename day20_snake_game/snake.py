from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.direction = 0  # 0=right, 1=up, 2=left, 3=down

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.speed(0)
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_list.append(snake)

    def extend(self):
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_num - 1].xcor()
            new_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
