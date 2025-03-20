import turtle


def create_ball():
    # """Створює м'яч та повертає його."""
    ball = turtle.Turtle()
    ball.shape('ball.gif')
    ball.penup()
    ball.speed(5)
    return ball


def move_ball(ball, dx, dy):
    ballx = ball.xcor()
    bally = ball.ycor()
    ball.showturtle()
    while True:
        ball.goto(ballx + dx, bally + dy)
        ballx = ball.xcor()
        bally = ball.ycor()
        if ballx < -175 or ballx > 175:
            dx = dx * -1
        if bally < -175 or ballx > 175:
            dy = dy * -1


def draw_box():
    box = turtle.Turtle()
    box.hideturtle()
    box.pensize(20)
    box.penup()
    box.goto(-200, 200)
    box.pendown()
    box.color("white")
    for side in range(4):
        box.fd(400)
        box.right(90)


def main():
    window = turtle.Screen()
    window.bgcolor('green')
    window.setup(500, 500)
    window.title("Visible boll")
    window.register_shape("ball.gif")
    ball = create_ball()
    draw_box()
    move_ball(ball, dx=5, dy=-5)
    turtle.mainloop()


if __name__ == "__main__":
    main()
