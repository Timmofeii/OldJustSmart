import random
import string
import turtle
import time

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

print(random.choice(ukrainian_alphabet))


def draw_figure(user_color, edge, corner, length):
    turtle.begin_fill()
    turtle.color(user_color)
    for i in range(edge):
        turtle.left(corner)
        turtle.forward(length)
    turtle.end_fill()
    time.sleep(1)
    turtle.clear()


def draw_triagle(user_color):
    draw_figure(user_color, 3, 120, 100)


def draw_squer(user_color):
    draw_figure(user_color, 4, 90, 50)


def draw_hexagon(user_color):
    draw_figure(user_color, 6, 50, 50)


def draw_pentahedron(user_color):
    draw_figure(user_color, 5, 60, 50)


def draw_circle(user_color, size, coordinate_x, coordinate_y):
    turtle.up()
    turtle.goto(coordinate_x, coordinate_y)
    turtle.down()
    turtle.begin_fill()
    turtle.color(user_color)
    turtle.circle(size)
    turtle.end_fill()


def draw_smile():
    # draw face
    turtle.width(5)
    turtle.up()
    turtle.goto(0, -50)
    turtle.down()
    turtle.color('Yellow')
    turtle.circle(180)
    draw_circle("blue", 30, 80, 175)
    draw_circle("blue", 30, -80, 175)
    # draw smile
    turtle.up()
    turtle.color('Red')
    turtle.goto(130, 80)
    turtle.down()
    turtle.left(60)
    turtle.circle(150, -120)
    time.sleep(1)
    turtle.exitonclick()
    turtle.clear()


def draw_kasper():
    kasper = turtle.Turtle()
    kasper.color('red', 'yellow')
    kasper.begin_fill()
    while True:
        kasper.forward(200)
        kasper.left(170)
        if abs(kasper.pos()) < 1:
            break
    kasper.end_fill()
    turtle.done()


def draw_abstraction_circle(count_circle):
    size = 100
    position_x = 0
    position_y = 0
    for i in range(count_circle):
        turtle.circle(180)
        turtle.up()
        turtle.left(45)
        position_x += 10
        position_y += 10
        turtle.goto(position_x, position_y)
        size -= 10
        turtle.down()


# draw_squer("Yellow")
# draw_triagle("Red")
# draw_hexagon("Blue")
# draw_pentahedron("Green")
# draw_smile()
# draw_kasper()


def __you_the_fa():
    variants = ["scissors", "rug", "paper"]
    computer_choice = random_value(variants)
    human_choice = input("eNTER your choice")  # input("Enter your choice:\nscissors, rug, paper ")
    ia_win = f"Computer win {computer_choice} human's {human_choice}"
    if computer_choice == variants[0] and human_choice == variants[2]:
        return ia_win
    elif computer_choice == variants[1] and human_choice == variants[0]:
        return ia_win
    elif computer_choice == variants[2] and human_choice == variants[1]:
        return ia_win
    elif computer_choice == human_choice:
        return f"no winners {human_choice} {computer_choice}"
    else:
        return f"Human win {human_choice} computer's {computer_choice}"


def random_value(list):
    return random.choice(list)


def light_reg():
    turtle.delay(0)

    # Створення об'єкта turtle
    t = turtle.Turtle()
    t.hideturtle()

    # Початкові налаштування
    red = False
    green = True

    while True:
        t.clear()

        if green:
            t.penup()
            t.goto(0, 0)
            t.fillcolor("green")
            t.begin_fill()
            t.circle(40)
            t.end_fill()
            t.pendown()
            time.sleep(1)  # затримка 1 сек
            red = True
            green = False
            continue

        if red:
            t.penup()
            t.goto(0, -100)
            t.fillcolor("red")
            t.begin_fill()
            t.circle(40)
            t.end_fill()
            t.pendown()
            time.sleep(1)  # затримка 1 сек
            red = False
            green = True
            continue


def __codes_words(word, key_word):  # нужно переписать код шифровки, есть код асси,
    # берем слово, увеличиваем длину нового слова в два раза заполняя буквами, дальше проходим циклом по key_word беря индекс с word и вставляя символы в новое слово по  key_word
    #  string.asccii_letters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ""
    len_new_word = len(word) * 2
    if (len_new_word < 10):
        len_new_word = 10

        code_list = [random.choice(alphabet) for _ in range(len_new_word)]
        for i in range(10):
            code += random.choice(alb)
        for i in range(len(key_word)):
            code_list[int(key_word[i])] = word[i]
    code = ''.join(code_list)
    return code


def de_code_word(word, code):
    answer = ""

    for i in range(len(code)):
        answer += word[int(code[i])]

    return answer


def same_char(first_word, second_word):
    count_same_char = 0
    for i in range(min(len(first_word), len(second_word))):
        if first_word[i] == second_word[i]:
            count_same_char += 1
    return count_same_char


ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
word = "Море"
code = "2843"
result = ""
len_code_word = 0
for i in range(len(code)):
    # пропігаємо по циклу та порівнюємо len_code_word з текучім значенням i, якщо len_code_word менше i тоді даємо нове значення len_code_word = i
    if len_code_word < int(code[i]):  # here
        len_code_word = int(code[i])
print(len_code_word)
for i in range(len_code_word):
    result += random.choice(ukrainian_alphabet)

for i in range(len(word)):
    index = int(code[i]) - 1
    result = result[:index] + word[i] + result[index + 1:]
print(result)

a = [3, 5, 6, 1, 2]
print(a.reverse())
print(a)


def de_code_word(word, code):
    result = ""
    for index in code:
        result = result + word[int(index)]  # дістаємо літеру з word по індексу
    return result


def code_word(word, code):
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    result = ""
    len_code_word = 0
    for i in range(len(code)):
        # пропігаємо по циклу та порівнюємо len_code_word з текучім значенням i, якщо len_code_word менше i тоді даємо нове значення len_code_word = i
        if len_code_word < int(code[i]):  # here
            len_code_word = int(code[i])
    if len_code_word < 9:
        len_code_word += 1
    for i in range(len_code_word):
        result += random.choice(ukrainian_alphabet)

    for i in range(len(word)):
        index = int(code[i])
        result = result[:index] + word[i] + result[index + 1:]
    result = result.lower()
    print(result)
    return result


word = "Бумеранго"
code = "2843"
word = "Море"
word = code_word(word, code)
print(de_code_word(word, code))
