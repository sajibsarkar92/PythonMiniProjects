from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        # self.shape("rectangle")
        self.penup()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.goto(-270, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(
            f"Score: {self.score}",
            move=False,
            align="center",
            font=("Arial", 10, "bold"),
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Arial", 18, "bold"))
