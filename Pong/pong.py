#Pong
#By STW_Galaxy#8295 on Discord

import turtle
import random
import time

#Draw the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.bgpic("gamebg.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
ScoreA = 0
ScoreB = 0

#Paddle A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("white")
padA.shapesize(stretch_wid=5, stretch_len=1)
padA.penup()
padA.goto(-375, 0)

#Paddle B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("white")
padB.shapesize(stretch_wid=5, stretch_len=1)
padB.penup()
padB.goto(375, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(-0.7, -0.7)
ball.penup()
ball.dx = 0.25
ball.dy = 0.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0              Player 2: 0", align="center", font=("Courier", 24, "normal"))

#Function
def padA_up():
    y = padA.ycor()
    y += 20
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    y -= 20
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 20
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    y -= 20
    padB.sety(y)

#Keyboard Bindings
wn.listen()
wn.onkeypress(padA_up, "w")
wn.onkeypress(padA_down, "s")
wn.onkeypress(padB_up, "Up")
wn.onkeypress(padB_down, "Down")

#Main game loop
while True:
    wn.update()

    #Ball - Top / bottom Collision
    if padA.ycor() >= 240:
        padA.sety(240)

    if padA.ycor() <= -220:
        padA.sety(-220)

    if padB.ycor() >= 240:
        padB.sety(240)

    if padB.ycor() <= -230:
        padB.sety(-230)

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        pen.clear()
        ScoreA += 30
        pen.write("Player 1: {}              Player 2: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        pen.clear()
        ScoreB += 30
        pen.write("Player 1: {}              Player 2: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    #Paddle - Ball Collision
    if ball.xcor() > 360 and (ball.ycor() < padB.ycor() + 50 and ball.ycor() > padB.ycor() - 50):
        ball.setx(340)
        ball.dx += 0.04
        ball.dy += 0.04
        ball.dx *= -1
        pen.clear()
        ScoreB += 10
        pen.write("Player 1: {}              Player 2: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -360 and (ball.ycor() < padA.ycor() + 50 and ball.ycor() > padA.ycor() - 50):
        ball.setx(-340)
        ball.dx += 0.04
        ball.dy += 0.04
        ball.dx *= -1
        pen.clear()
        ScoreA += 10
        pen.write("Player 1: {}              Player 2: {}".format(ScoreA, ScoreB), align="center", font=("Courier", 24, "normal"))