import time

import paddle, ball, turtle, scoreboard


def bind_key(screen, padle, key_up, key_down):
    screen.onkey(padle.go_up, key_up)
    screen.onkey(padle.go_down, key_down)


def movePadle(screen, r_padle, l_padle):
    screen.listen()
    bind_key(screen, r_padle, "Up", "Down")
    bind_key(screen, l_padle, "w", "s")


def creat_screen(name, bgcolor, width, height):
    screen = turtle.Screen()
    screen.title(name)
    screen.bgcolor(bgcolor)
    screen.setup(width=width, height=height)
    screen.tracer(0)
    return screen



# window,ball,player1,player2
def game():
    window = creat_screen("PingPong", "Black", 800, 600)
    r_padle = paddle.Paddle(350, 0)
    l_padle = paddle.Paddle(-350, 0)
    my_ball = ball.Ball(0.1)
    scor = scoreboard.Scoreboard()

    while True:
        movePadle(window, r_padle, l_padle)
        my_ball.move()
        time.sleep(0.05)

        window.update()
        if my_ball.ycor() > 280 or my_ball.ycor() < -280:
            my_ball.y_bounce()
        if my_ball.distance(r_padle) < 50 and my_ball.xcor() > 320 or my_ball.distance(
                l_padle) < 50 and my_ball.xcor() < 320:
            my_ball.x_bounce()
        if my_ball.xcor() > 380:
            my_ball.reset_position()
            scor.l_point()
        if my_ball.xcor()  <-380:


            my_ball.reset_position()
            scor.r_point()


game()
