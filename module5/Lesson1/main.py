import pygame, random





pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
surface = pygame.Surface((200, 200))
surface.fill((255, 255, 255))

sprite = pygame.sprite.Sprite()
sprite.image = pygame.Surface((50, 50))

sprite.image.fill((255, 0, 0))

sprite.rect = sprite.image.get_rect()
sprite.rect.x = random.randint(0, WIDTH - sprite.rect.width)
sprite.rect.y = random.randint(0, HEIGHT - sprite.rect.height)


rect = pygame.Rect(50, 50, 100, 100)
font = pygame.font.Font(None,36)
text = font.render("Hello, Pygame!", True, (255, 255, 255))

font_path = "C:/Users/Дениса ПК/Desktop/Шрифты/Doto-VariableFont_ROND,wght.ttf"

font1 = pygame.font.Font(font_path, 35)


text_hw = font1.render("Home work", True, (255, 255, 255))
text_x = 0
text_y = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    sprite.rect.x += random.randint(-5, 5)
    sprite.rect.y += random.randint(-5, 5)

    if sprite.rect.left < 0 or sprite.rect.right > WIDTH:
        sprite.rect.x -= 2 * (sprite.rect.centerx - WIDTH / 2)
    if sprite.rect.top < 0 or sprite.rect.bottom > HEIGHT:
        sprite.rect.y -= 2 * (sprite.rect.centery - HEIGHT / 2)
    screen.fill((0,0,0))
    screen.blit(surface,(100,100))
    screen.blit(text_hw,(0,0))
    pygame.draw.rect(screen,(0,255,0),rect)
    screen.blit(text,(text_x,text_y))

    text_x += 1
    text_y += 1
    if text_x > WIDTH:
        text_x = 0
    if text_y > HEIGHT:
        text_y = 0
    clock.tick(60)
    pygame.display.update()
