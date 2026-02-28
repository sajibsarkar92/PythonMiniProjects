from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE





    def create_car(self):
        chance = random.randint(1,6)
        if chance ==4:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(random.randint(280, 310), random.randint(-280, 280))
            self.all_cars.append((car))


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            self.finish(car)


    def finish(self,car):
        if car.xcor()<-280:
            car.clear()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
