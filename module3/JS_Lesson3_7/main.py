import turtle
from ball import Ball
from tennis_racket import Tenis_Raket





def game():
    screen = turtle.Screen()
    screen.title("PingPong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    ball = Ball(0.1)
    r_padle = Tenis_Raket(350, 0)
    l_padle = Tenis_Raket(-350, 0)

    screen.listen()
    screen.onkey(r_padle.go_up, "Up")
    screen.onkey(r_padle.go_down, "Down")
    screen.onkey(l_padle.go_up, "w")
    screen.onkey(l_padle.go_down, "s")

    while True:
        ball.move()
        screen.update()



# game()

