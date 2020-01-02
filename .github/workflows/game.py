import turtle

# Screen
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("Black")
win.setup(height=600, width=840)
win.tracer(0)

# Paddles
# paddle_a
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-385, 0)
paddle_a.shapesize(stretch_wid=7, stretch_len=1)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(385, 0)
paddle_b.shapesize(stretch_wid=7, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("Red")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1
# Score
score_a = 0
score_b = 0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write((f"Player A {score_a}     Player B {score_b}" ), align = "center", font = ("Courier", 24, "normal"))
#Me
author = turtle.Turtle()
author.speed(0)
author.penup()
author.hideturtle()
author.goto(250, -250)
author.color("white")
author.write("Pong By Samir Gyawali", align="left", font=("Arial", 8, "normal"))

### Moving Paddles
## paddle_a
# paddle_a_up
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 10
    paddle_a.sety(y)


# Paddle_a_down
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 10
    paddle_a.sety(y)


## Paddle_b
# paddle_b_up
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 10
    paddle_b.sety(y)


# paddle_b_down
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 10
    paddle_b.sety(y)

## Key Strokes

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop

while True:
    win.update()
    # Ball Move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Edge Handel
    if ball.ycor() > 273:
        ball.sety(273)
        ball.dy = ball.dy * -1
    if ball.xcor() > paddle_b.xcor() + 20:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        pen.clear()
        pen.write((f"Player A : {score_a}    Player B : {score_b}"), align="center", font=("Courier", 24, "normal"))
        author.write("Pong By Samir Gyawali", align="left", font=("Arial", 8, "normal"))

    if ball.ycor() < -273:
        ball.sety(-273)
        ball.dy = ball.dy * -1
    if ball.xcor() <  paddle_a.xcor() - 20:
        ball.goto(0, 0)
        ball.dx = ball.dx * - 1
        score_b = score_b + 1
        pen.clear()
        pen.write((f"Player A : {score_a}    Player B : {score_b}"), align="center", font=("Courier", 24, "normal"))
        author.write("Pong By Samir Gyawali", align="left", font=("Arial", 8, "normal"))
    # COLLISION DETECTION
    if (ball.xcor() > paddle_b.xcor()) and ((ball.ycor() < paddle_b.ycor() + 80) and (ball.ycor() > paddle_b.ycor() - 90)):
        ball.dx = ball.dx * - 1
    if (ball.xcor() < paddle_a.xcor()) and ((ball.ycor() < paddle_a.ycor() + 80) and (ball.ycor() > paddle_a.ycor() -80)):
        ball.dx = ball.dx * -1

