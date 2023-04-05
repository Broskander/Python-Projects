from turtle import Screen, Turtle
from pong_paddle import Player
from pong_ball import Ball
import time

# Window
game = Screen()
game.title("Pong Game")
game.bgcolor("black")
game.setup(width=800, height=600)
game.tracer(0)

# Assets
playerOne = Player((-350, 0))
playerTwo = Player((350, 0))
ball = Ball()

# # Movement
game.listen()
game.onkey(playerOne.up, "w")
game.onkey(playerOne.down, "s")
game.onkey(playerTwo.up, "Up")
game.onkey(playerTwo.down, "Down")

running = True
while running:
    time.sleep(0.1)
    game.update()
    ball.move()

    #When the ball hits the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceVertical()


    #When the ball hits the player(s)
    if (ball.distance(playerOne) < 50 and ball.xcor() < -320) or (ball.distance(playerTwo) < 50 and ball.xcor() > 320):
        ball.bounceHorizontal()


game.exitonclick()
