import turtle

wn = turtle.Screen()
wn.title("pong copy game by @nandasuna")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer() #this makes the window manually update to make the game run faster)

#score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #no drawinh when moving
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)

ball.dx = 4 #move in x
ball.dy = 4

#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" player A: 0    player B: 0 ", align="center", font=('arial black', 24, "normal"))

# functions

def paddle_a_up():
    y = paddle_a.ycor() #the .ycor() is form the turtle module and tells the y cordenates
    if y < 240:
        y += 20
        paddle_a.sety(y) #moving the y up

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    if y < 240:
        y += 20
        paddle_b.sety(y) #moving the y up

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)



#keyboard binding
wn.listen() #tells the window to listen to keyboard input
wn.onkeypress(paddle_a_up, "w") #when u press "w" call paddle_a_up funcion
wn.onkeypress(paddle_a_down, "s") #when u press "s" call paddle_a_up funcion
wn.onkeypress(paddle_b_up, "Up") #when u press "w" call paddle_a_up funcion
wn.onkeypress(paddle_b_down, "Down") #when u press "s" call paddle_a_up funcion



# main game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border cheking
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390 :
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(" player A:{}     player B:{} ".format(score_a, score_b), align="center", font=('arial black', 24, "normal"))


    if ball.xcor() > 390 :
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(" player A:{}     player B:{} ".format(score_a, score_b), align="center", font=('arial black', 24, "normal"))


# comparing paddle and ball
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
  
    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1



