import sys
from codecs import xmlcharrefreplace_errors

import pygame

pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_img, x, y):
        super().__init__()
        self.image = sprite_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():

    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Sprite Example")
    image1 = pygame.image.load("C:\\Users\\Дениса ПК\\Desktop\\Sprites\\Gold-0.png").convert_alpha()
    # image1= pygame.transform.scale(image1,(100,100))
    image2 = pygame.image.load("C:\\Users\\Дениса ПК\\Desktop\\Sprites\\Gold-4.png").convert_alpha()
    sprite1 = Sprite(image1, 100, 100)
    sprite2 = Sprite(image2, 500, 600)
    sprites = pygame.sprite.Group()
    sprites.add(sprite1)
    sprites.add(sprite2)
    running = True

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        screen.fill((0,0,0))
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
        pygame.display.update()

if __name__=="__main__":
    main()