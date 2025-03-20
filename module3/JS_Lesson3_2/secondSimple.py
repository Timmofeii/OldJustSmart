import turtle
import random
# Створення вікна
win = turtle.Screen()
win.title("Рух м'яча")
win.bgcolor("white")
win.setup(width=600, height=400)
# Створення м'яча
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
# Швидкість та напрямок м'яча
ball.dx = 2
ball.dy = -2
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
# Перевірка на зіткнення з верхньою та нижньою межами
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1
        colors = ["red", "blue", "green", "yellow", "purple", "orange","pink", "brown", "gray", "black", "white", "cyan", "magenta", "lime", "navy", "gold"]
        choose_color = random.choice(colors)
        ball.color(choose_color) # Зміна кольору м'яча на червоний при зіткненні з верхньою та нижньою межами
# Перевірка на зіткнення з лівою та правою межами
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown","gray", "black", "white",
        "cyan", "magenta", "lime", "navy", "gold"]
        choose_color = random.choice(colors)
        win.bgcolor(choose_color) # Зміна кольору фону на світло-синій при зіткненні з лівою та правою межами
        win.update()