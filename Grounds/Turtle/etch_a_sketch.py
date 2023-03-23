from turtle import Turtle, Screen

drawer = Turtle()
screen = Screen()

def draw_forward():
    drawer.forward(10)
def draw_backwords():
    drawer.backward(10)
def rotate_left():
    drawer.left(10)
def rotate_right():
    drawer.right(10)

if __name__ == "__main__":
    screen.listen()
    screen.onkey(key="w", fun=draw_forward)
    screen.onkey(key="s", fun=draw_backwords)
    screen.onkey(key="a", fun=rotate_left)
    screen.onkey(key="d", fun=rotate_right)

    screen.exitonclick()