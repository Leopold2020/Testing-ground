from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

def create_turtles():
    """
    Returnerar en lista med en sköldpadda per färg.

    Returns:
        list: Listan med sköldpaddor
    """
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i in colors:
        temp_turtle = Turtle(shape="turtle")
        temp_turtle.color(i)
        turtles.append(temp_turtle)
    
    return turtles

def init_turtles(turtles: list()):
    """
        Initiera sköldpaddornas positioner på skärmen.
        Börja på y = 75 och avta 25 för varje sköldpadda i y-led.

    Args:
        turtles (list): Listan med sköldpaddorna.
    """
    number = 75
    for t in turtles:
        t.penup()
        t.sety(number)
        t.setx(-200)
        number -= 25
        t.pendown()



def race(turtles):
    """
       Funktion som får racet att ske. Varje gång funktionen
       anropas ska sköldpaddorna röra sig framåt.
    """
    for t in turtles:
        t.forward(randint(1, 10))
        if t.xcor() >= 200:
            break


if __name__ == "__main__":
    
    # Låt användaren betta på en sköldpadda att vinna.
    user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")
    if user_bet:
        turtles = create_turtles()
        init_turtles(turtles)
        is_race_on = True
    
    # do race
    while is_race_on:
        race(turtles)
        for racer in turtles:
            if racer.xcor() >= 200:
                print(f"{racer.color()[0]} win")
                is_race_on = False
                winner = racer

if winner.color()[0] == user_bet:
    print("You win the bet")

else:
    print("You lost the bet")

    
    # skriv vem som vann
    # avgör om anv. vann sitt bet
    
    
    screen.exitonclick()
