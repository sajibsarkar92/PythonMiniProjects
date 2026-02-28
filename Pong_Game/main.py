from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.listen()
screen.tracer(0)




scoreboard = Scoreboard()
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

speed = 0.1
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.start_move()

    #detect collsion

    if(abs(ball.ycor())>280):
        ball.bounce()

    #detect collision with r_paddle

    if r_paddle.distance(ball) <50 and ball.xcor()>325:
        print("collison")
        ball.paddle_bounce()
        ball.setx(325)
        speed *= .95


    if l_paddle.distance(ball) <50 and ball.xcor()<-325:
        print("collison")
        ball.paddle_bounce()
        ball.setx(-325)
        speed *= .95



    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()
        speed = .1



    if ball.xcor() <-370:
        ball.reset_position()
        scoreboard.r_point()
        speed = .1



screen.exitonclick()