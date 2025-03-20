 from turtle import *


class Ball(Turtle):
    def __init__(self, move_speed):
        Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = move_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.move_speed = 0.1

    def y_bounce(self):
        self.y_move = self.y_move * (-1)

    def x_bounce(self):
        self.x_move = self.x_move * (-1)

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
        self.move_speed = 0.1
