import turtle
#score logic
scorea=0
scoreb=0
win=turtle.Screen()
win.setup(800,600)
win.bgcolor('blue')
win.title("pong game")
win.tracer(0)

left=turtle.Turtle()

left.speed(0)
left.shape('square')
left.color('white')
left.shapesize(stretch_wid=5,stretch_len=1)
left.penup()
left.goto(-388,0)


right= turtle.Turtle()
right.speed(0)
right.shape('square')
right.color('white')
right.shapesize(stretch_wid=5,stretch_len=2)
right.penup()
right.goto(388,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx=0.11
ball.dy=0.11

pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player_A:0 player_b:0",align='center',font=('ariel',24,'normal'))


#moving paddles
def left_paddle_up():
    left.sety(left.ycor() +20)

def left_paddle_down():
    left.sety(left.ycor() - 20)

def right_paddle_up():
    right.sety(right.ycor() + 20)

def right_paddle_up():
    right.sety(right.ycor() + 20)

def right_paddle_down():
    right.sety(right.ycor() - 20)

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
#top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
#bottom wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
    #right wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *=-1
        scorea+=1
        pen.clear()
        pen.write("playerA:{} player_b:{}".format(scorea,scoreb),align='center',font=('ariel',24,'normal'))
    #left wall
    if ball.xcor()<-390:
        ball.setx(-370)
        ball.dx *=-1
        scoreb+=1
        pen.clear()
        pen.write("playerA:{} player_b:{}".format(scorea,scoreb),align='center',font=('ariel',24,'normal'))
    if ball.xcor() > 380 and ball.ycor() <right.ycor()+50 and ball.ycor()>right.ycor()-50:
        ball.setx(360)
        ball.dx*= -1
    if ball.xcor() <-380 and ball.ycor()<left.ycor()-50 and ball.ycor() > left.ycor()+50:
        ball.setx(-360)
        ball.dy*= -1
