from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# We define these as None initially
snake = None
food = None
scoreboard = None
game_on = False


def start_game():
    global snake, food, scoreboard, game_on, speed

    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)

    # 2. Re-initialize objects
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    speed = 0.1
    game_on = True

    # 3. Re-bind keys (clearscreen removes them)
    setup_listeners()

    run_game()


def setup_listeners():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    # Bind space to restart only when the game is NOT running
    screen.onkey(start_game, "space")


def run_game():
    global game_on, speed
    while game_on:
        screen.update()
        time.sleep(speed)
        snake.move()

        if food.distance(snake.head) < 17:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
            if scoreboard.score % 10 == 0:
                speed *= 0.95

        # Collision with Wall
        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            game_over()

        # Collision with Tail
        for segment in snake.segments[1:]:
            if segment.distance(snake.head) < 10:
                game_over()


def game_over():
    global game_on
    game_on = False
    scoreboard.game_over()
    # Tell the user they can restart
    scoreboard.goto(0, -50)
    scoreboard.write(
        "Press SPACE to Restart", align="center", font=("Courier", 14, "normal")
    )


# Initial Start
start_game()
screen.exitonclick()
