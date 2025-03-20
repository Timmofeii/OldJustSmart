
import pygame
import random
from game import Game
from gameObject import *
class DinoGame:
    def play(self):
        pygame.init()
        size = (600, 200)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Dino_Game")

        dino_img = pygame.image.load("dino.png")
        dino_pos = (50, 150)
        cactus_img = pygame.image.load("cactus.png")
        cactus_pos = (600, 150)
        font = pygame.font.Font(None, 36)
        textUI = "Score: "
        text_img = font.render(textUI, True, BLACK)
        text_pos = (450, 10)
        ground_img = pygame.Surface([600, 1])
        ground_pos = (0, 190)
        dino = Dino(dino_img, dino_pos)

        score = Score(text_img, text_pos, BLACK, textUI, font)
        ground = Ground(ground_img, ground_pos)

        game = Game(screen, WHITE, dino, cactus_img, cactus_pos, score, ground)
        game.play()