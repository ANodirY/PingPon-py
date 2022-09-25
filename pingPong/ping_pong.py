import turtle
import winsound

wn = turtle.Screen()
wn.title('PingPong by A.Nodir')
wn.bgcolor('olive drab')
wn.setup(width=700, height=400)
wn.tracer(0)



score_a = 0
score_b = 0

#line
line = turtle.Turtle()
line.shape('square')
line.color("white")
line.shapesize(stretch_wid=12, stretch_len=0.2)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('crimson')
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-300, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('indigo')
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(300, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('gold')
ball.penup()
ball.goto(0, 0)
ball.dx = 1.45
ball.dy = 1.45

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('#000')
pen.penup()
pen.goto(0, 160)
pen.hideturtle()
pen.write('Player RED:0  Player BLUE:0, q = exit', align='center', font=('Gungsuh', 16, 'normal'))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 28
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 27
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 28
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 27
    paddle_b.sety(y)

def quit():
    turtle.Screen().bye()

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
wn.onkeypress(quit, 'q')

while True:
    wn.update()
           
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() > 330:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player RED:{}  Player BLUE:{}, q = exit'.format(score_a, score_b), align='center', font=('Gungsuh', 16, 'normal'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if ball.xcor() < -330:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player RED:{}  Player BLUE:{}, q = exit'.format(score_a, score_b), align='center', font=('Gungsuh', 16, 'normal'))
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if (ball.xcor() > 280 and ball.xcor() <290) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(280)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
  
    if (ball.xcor() < -280 and ball.xcor() > -290) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-280)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
