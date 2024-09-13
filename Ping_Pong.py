# Ping pong game project

import turtle
import winsound
from winsound import SND_ASYNC

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(800,600)
wn.title("Ping Pong")
wn.tracer(0)

#Score
score_a=0
score_b=0

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A:{score_a}   Player B:{score_b}", align="center", font=("Courier",24,"normal"))


# Paddle A
paddle_a=turtle.Turtle()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shape("square")



# Paddle B
paddle_b=turtle.Turtle()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shape("square")

# Ball
ball=turtle.Turtle()
ball.goto(0,0)
ball.color("white")
ball.speed(0)
ball.penup()
ball.shape("square")
ball.dx=0.05
ball.dy=-0.05

# Functions to move paddle a and b, up and down
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>270:
        ball.sety(270)
        ball.dy *= -1
        score_b+=1
        pen.clear()
        winsound.PlaySound("ping-pong-game",SND_ASYNC)
        pen.write(f"Player A:{score_a}   Player B:{score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.ycor()<-270:
        ball.sety(-270)
        ball.dy *= -1
        score_a+=1
        pen.clear()
        winsound.PlaySound("ping-pong-game", SND_ASYNC)
        pen.write(f"Player A:{score_a}   Player B:{score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor()>370:
        ball.goto(0,0)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        winsound.PlaySound("ping-pong-game", winsound.SND_ASYNC)
        pen.write(f"Player A:{score_a}   Player B:{score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-370:
        ball.goto(0,0)
        ball.dx*=-1
        score_a += 1
        pen.clear()
        winsound.PlaySound("ping-pong-game", SND_ASYNC)
        pen.write(f"Player A:{score_a}   Player B:{score_b}", align="center", font=("Courier", 24, "normal"))

    if 340>ball.xcor()>330 and paddle_b.ycor()-40<ball.ycor()<paddle_b.ycor()+40:
        ball.setx(340)

    if -340<ball.xcor()<-330 and paddle_b.ycor()-40<ball.ycor()<paddle_b.ycor()+40:
        ball.setx(-340)

