from shutil import posix

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)
color = (0, 0, 0)
running = True


def simple_moving():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            print("Move the character forwards")
        elif event.key == pygame.K_s:
            print("Move the character backwards")
        elif event.key == pygame.K_a:
            print("Move the character left")
        elif event.key == pygame.K_d:
            print("Move the character right")


def simple_using_mouse():
    if event.type == pygame.MOUSEMOTION:
        if event.rel[0] > 0:
            print("Mouse moving to the right")
        elif event.rel[1] > 0:
            print("Mouse moving down")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
            print("Right mouse button pressed")
    elif event.type == pygame.MOUSEBUTTONUP:
        print("Mouse button has bin released")


def move_right(x):
    return x + 10


def move_left(x):
    return x - 10


def move_up(y):
    return y - 10


def move_down(y):
    return y + 10


image = pygame.image.load("C:\\Users\\Дениса ПК\\Desktop\\Sprites\\Gold-0.png")


def practica():
    global pos_x, pos_y
    screen.fill((0,0,0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            pos_y= move_up(pos_y)

        elif event.key == pygame.K_s:
            pos_y=move_down(pos_y)
        elif event.key == pygame.K_a:
            pos_x=move_left(pos_x)
        elif event.key == pygame.K_d:
            pos_x=move_right(pos_x)


pos_x = 0
pos_y = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # simple_moving()
        # simple_using_mouse()
        practica()

    screen.blit(image, pos_x, pos_y)
    pygame.display.flip()
    clock.tick(13)
    pygame.display.update()
