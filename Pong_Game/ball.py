from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move =10
        self.y_move = 10


    def start_move(self):

        self.setx(self.xcor()+self.x_move)
        self.sety(self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):

        self.x_move  *= -1
    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()

