import turtle

# Window
game = turtle.Screen()
game.title("Pong Game")
game.bgcolor("white")
game.setup(width = 800, height = 600)
game.tracer(0)

# Assets
playerOne = turtle.Turtle()
playerOne.speed(0)
playerOne.shape("square")
playerOne.shapesize(stretch_wid = 5, stretch_len = 1)
playerOne.color("black")
playerOne.penup()
playerOne.goto(-350, 0)

playerTwo = turtle.Turtle()
playerTwo.speed(0)
playerTwo.shape("square")
playerTwo.shapesize(stretch_wid = 5, stretch_len = 1)
playerTwo.color("black")
playerTwo.penup()
playerTwo.goto(350, 0)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Movement
def playerOneUp():
    y_coord = playerOne.ycor()
    y_coord += 50
    playerOne.sety(y_coord)

def playerOneDown():
    y_coord = playerOne.ycor()
    y_coord -= 50
    playerOne.sety(y_coord)

def playerTwoUp():
    y_coord = playerTwo.ycor()
    y_coord += 50
    playerTwo.sety(y_coord)

def playerTwoDown():
    y_coord = playerTwo.ycor()
    y_coord -= 50
    playerTwo.sety(y_coord)

# Binding
game.listen()
game.onkeypress(playerOneUp, "w")
game.onkeypress(playerOneDown, "s")
game.onkeypress(playerTwoUp, "Up")
game.onkeypress(playerTwoDown, "Down")

# Scoring
scorePlayerOne = 0
scorePlayerTwo = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Times New Roman", 24, "italic"))

# Ending Screen
endScreen = turtle.Turtle()
endScreen.speed(0)
endScreen.color("black")
endScreen.penup()
endScreen.hideturtle()
endScreen.goto(0, 0)

# Game body
while True:
    game.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scorePlayerOne += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(scorePlayerOne, scorePlayerTwo), align="center", font=("Times New Roman", 24, "italic"))

        if (scorePlayerOne == 7):
            playerOne.hideturtle()
            playerTwo.hideturtle()
            ball.hideturtle()
            endScreen.write("The winner is player one", align="center", font=("Times New Roman", 24, "italic"))
            turtle.exitonclick()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scorePlayerTwo += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(scorePlayerOne, scorePlayerTwo), align="center", font=("Times New Roman", 24, "italic"))

        if (scorePlayerTwo == 7):
            playerOne.hideturtle()
            playerTwo.hideturtle()
            ball.hideturtle()
            endScreen.write("The winner is player two", align="center", font=("Times New Roman", 24, "italic"))
            turtle.exitonclick()

    if (340 < ball.xcor() < 350) and (playerTwo.ycor() + 40 > ball.ycor() > playerTwo.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (playerOne.ycor() + 40 > ball.ycor() > playerOne.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
