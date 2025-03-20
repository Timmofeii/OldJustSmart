from random import randrange
import time
import turtle
from random import randrange

def draw_border():
    border = turtle.Turtle()
    border.hideturtle()
    border.penup()
    border.goto(-311, 311)
    border.pendown()
    border.goto(311, 311)
    border.goto(311, -311)
    border.goto(-311, -311)
    border.goto(-311, 311)

def down():
    snake[0].setheading(270)

def create_snake():
    snake = []
    for i in range(3):
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.penup()
        # якщо сегмент >0 робимо його сірим
        if i > 0:
            snake_segment.color('gray')
        snake.append(snake_segment)
    return snake

def up():
    snake[0].setheading(90)

def lef():
    snake[0].setheading(180)

def right():
    snake[0].setheading(0)

def create_food():
    food = turtle.Turtle()
    food.shape("circle")
    food.color("black")
    food.penup()
    food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
    return food

def eat_food():
    if snake[0].distance(food) < 10:
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('gray')
        snake_segment.penup()
        snake.append(snake_segment)

def move_snake():
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)
    snake[0].forward(20)

def check_body_corner():
    x_cor = snake[0].xcor()
    y_cor = snake[0].ycor()
    cord = 290
    if x_cor > cord or x_cor < -cord or y_cor > cord or y_cor < -cord:
        return True
    return False

def game_over():
    screen.bgcolor('red')

def check_tail():
    for segment in snake[1:]:
        # Проверяем расстояние между головой змеи и сегментами хвоста
        if snake[0].distance(segment) < 10:
            return True  # столкновение

    return False  # нет столкновения

def draw_start_game():
    snake_gif = turtle.Turtle()
    snake_gif = bgpig("faceGame.gif")
    snake_gif.done()



BREAK_FLAG = False
wait_time = 0.2
def create_screen():
    # Создаем окно
    screen = turtle.Screen()
    screen.title('Змійка')
    screen.bgcolor('green')
    screen.setup(650, 650)
    return screen
screen = create_screen()

# Отключаем отрисовку
turtle.tracer(0, 0)

food = create_food()
snake = create_snake()
draw_border()

# Включаем небольшую задержку перед началом игры
time.sleep(2)

# Включаем отрисовку
turtle.tracer(1, 0)
while True:

    if BREAK_FLAG:
        game_over()
        break

    eat_food()
    screen.listen()
    screen.onkeypress(up, 'Up')
    screen.onkeypress(down, 'Down')
    screen.onkeypress(lef, 'Left')
    screen.onkeypress(right, 'Right')

    move_snake()
    if check_tail() or check_body_corner():
        BREAK_FLAG = True
    screen.update()
    time.sleep(wait_time)
screen.done()
