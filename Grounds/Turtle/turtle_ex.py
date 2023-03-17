
import turtle as t
from random import randint, choice

ragnar = t.Turtle()
ragnar.shape("turtle")
ragnar.color("red")

#   first test
# ragnar.forward(40)
# ragnar.left(45)
# ragnar.forward(50)
# ragnar.right(90)
# ragnar.forward(30)

#   dotted line
# ragnar.shape("arrow")
# for _ in range(10):
#     ragnar.pendown()
#     ragnar.forward(25)
#     ragnar.penup()
#     ragnar.forward(15)

#   Random walk
STATIC_COLOURS = ["deep pink", "cadet blue", "crimson", "cyan"]
ANGLES = [0, 90, 180, 270]
def random_walk():
    ragnar.color(choice(STATIC_COLOURS))

    paces = randint(15, 60)
    ragnar.setheading(choice(ANGLES))
    ragnar.forward(paces)

def random_color():
    t.colormode(255)
    return (randint(0, 255), randint(0, 255), randint(0, 255))
    

if __name__ == "__main__":

    ragnar.speed(40)
    ragnar.pensize(10)

    for _ in range(100):
        random_walk()

input()