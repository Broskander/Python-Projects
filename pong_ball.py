from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moveX = 10
        self.moveY = 10

    def move(self):
        x = self.xcor() + self.moveX
        y = self.ycor() + self.moveY
        self.goto(x, y)

    def bounceVertical(self):
        self.moveY *= -1

    def bounceHorizontal(self):
        self.moveX *= -1
