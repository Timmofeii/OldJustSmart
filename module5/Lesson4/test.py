import pygame, sys, os
class Sprite(pygame.sprite.Sprite):
    def __init__(self, path_image, sprite_x, sprite_y):
        super().__init__()
        self.image = pygame.image.load(path_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y


def practice_lesson4_4():
    screen = pygame.display.set_mode((600, 400))
    WHITE = (255, 255, 255)
    pygame.display.set_caption("My window")
    path_folder_images = "sprites"
    path_img = "C:\\Users\\Дениса ПК\\Desktop\\Sprites\\Gold-0.png"
    sprite = Sprite(path_img, 100, 100)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(sprite)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sprite_group.update()
        screen.fill(WHITE)
        sprite_group.draw(screen)
        pygame.display.flip()


practice_lesson4_4()


