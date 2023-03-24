import turtle as t
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self, cars: list) -> None:
        self.cars = cars
        self.speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        """
            En metod som har en 1/6 sannolikhet att skapa en bil.
            Om bilen skapas så gör den det här som läggs i sin egna billista.
            
            Bilar kan vara slumpmässig färg.
            De bör vara en fyrkant.
            De bör ha en shapesize på wid 1 och len 3, kanske 2, du bestämmer.
            De börjar på koordinaten (300, -240 <= y <= 260).
            Bilarna borde titta vänster.
            
        """
        if randint(1, 6) == 6:
            new_car = t.Turtle()
            new_car.shape("square")
            new_car.shapesize(1,3)
            new_car.color(COLORS)
            new_car.xcor(300)
            new_car.ycor(randint(-240, 260))
            new_car.left(180)
            self.cars.append(new_car)
            
    
    def move_cars(self):
        """
            Förflyttar alla bilar i billistan med den hastighet bilarna ska ha
            för nuvarande nivå.
        """
        for i in self.cars:
            i.forward(self.speed)
    
    def increase_speed(self):
        """
            Ökar hastigheten på samtliga bilar.
            Anropas när en nivå är avklarad.
        """
        self.speed += MOVE_INCREMENT