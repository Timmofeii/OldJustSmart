import pygame, random

pygame.init()
WIDTH = 600
HEIGHT = 400
size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(size)
surface = pygame.Surface((200, 200))
# 1. Створи спрайт

# pygame.sprite.Sprite()

# 2. У змінну sprite помісти створенний спрайт

# 3. Створи змінну sprite.image і зміни розмір поверхні 50 на 50 пікселей

# 4. Зафарбуй спрайт. Колір має дорівнювати (255,0,0)
pygame.sprite.Sprite()

pygame.display.set_caption("Pong")
running = True
surface.fill((255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.blit(surface, (0, 0))
            running = False
            pygame.quit()
            pygame.display.update()

