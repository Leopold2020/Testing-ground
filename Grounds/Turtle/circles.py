import turtle as t
from random import randint

ragnar = t.Turtle()
ragnar.shape("turtle")

def random_color():
    t.colormode(255)
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def circle(value1):
    # for _ in range(value2):
    #     ragnar.color(random_color())
    #     ragnar.circle(value1)
    #     ragnar.left(5)
    value = 50
    for _ in range(value1):
        for __ in range(72):
            ragnar.circle(value)
            ragnar.left(5)
            ragnar.color(random_color())
        value += 30

if __name__ == "__main__":

    choice = int(input("How many layers\n>> "))

    ragnar.speed("fastest")

    circle(choice)


input()