import sys

import pygame
from pygame.constants import KEYDOWN, MOUSEMOTION, MOUSEBUTTONDOWN

pygame.init()
HEIGHT = 800
WIDTH = 1200
screen = pygame.display.set_mode((1200, 800))

running = True
font_path = "C:/Users/Дениса ПК/Desktop/Шрифты/Doto-VariableFont_ROND,wght.ttf"
font = pygame.font.Font(font_path, 50)
pos_x = WIDTH / 4
pos_y = 0
txt = "test"
color_text = (255, 255, 255)
text = font.render(txt, True, color_text)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                pos_x = WIDTH * 0.25
                txt = "Left"
            elif event.button == 3:
                pos_x = WIDTH * 0.75
                txt = "Right"
    screen.fill((0, 0, 0))
    screen.blit(text, (pos_x, pos_y))

    clock.tick(50)
    pygame.display.update()
