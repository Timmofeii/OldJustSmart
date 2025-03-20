# import pygame
# import random
# # Инициализация Pygame
# pygame.init()
#
# # Определение цветов
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# # Создание окна
# size = (600, 200)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Dino Game")
#
# # Загрузка изображений
# dino_img = pygame.image.load("dino.png")
# cactus_img = pygame.image.load("cactus.png")
# ground=pygame.draw.rect(screen, BLACK, pygame.Rect(0, 50, 200, 10))
#
# # Установка параметров игры
# clock = pygame.time.Clock()
#
# class Ground(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface([600, 1])
#         self.image.fill(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.x = 0
#         self.rect.y = 190
# # Создание классов
# class Dino(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = dino_img
#         self.rect = self.image.get_rect()
#         self.rect.x = 50
#         self.rect.y = 150
#         self.y_speed = 0
#         self.is_jumping = False
#
#     def update(self):
#         self.y_speed += 1
#         self.rect.y += self.y_speed
#         if self.rect.y > 150:
#             self.rect.y = 150
#             self.y_speed = 0
#             self.is_jumping = False
#
#     def jump(self):
#         if not self.is_jumping:
#             self.y_speed = -15
#             self.is_jumping = True
#
#
# class Cactus(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = cactus_img
#         self.rect = self.image.get_rect()
#         self.rect.x = 600
#         self.rect.y = 150
#         self.speed = -10
#
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x < -40:
#             self.kill()
#
#
# class Score(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.font = pygame.font.Font(None, 36)
#         self.text = "Score: 0"
#         self.image = self.font.render(self.text, True, BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.x = 450
#         self.rect.y = 10
#         self.score = 0
#
#     def update(self):
#         self.score += 1
#         self.text = "Score: " + str(self.score)
#         self.image = self.font.render(self.text, True, BLACK)
#
#
# # Создание групп спрайтов
# all_sprites = pygame.sprite.Group()
# cactus_sprites = pygame.sprite.Group()
#
# # Создание объектов
# dino = Dino()
# all_sprites.add(dino)
#
# score = Score()
# all_sprites.add(score)
#
# ground=Ground()
# all_sprites.add(ground)
#
#
# # Установка начального значения таймера для появления кактусов
# spawn_timer = 0
#
# # Основной игровой цикл
# done = False
# while not done:
#     # Обработка событий
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             dino.jump()
#
#     # Обновление игровых объектов
#     all_sprites.update()
#     score.update()
#
#     # Создание новых кактусов
#     current_time = pygame.time.get_ticks()
#     if current_time - spawn_timer > 1500:
#         new_cactus = Cactus()
#         all_sprites.add(new_cactus)
#         cactus_sprites.add(new_cactus)
#         spawn_timer = current_time
#
#     # Проверка столкновения
#     if pygame.sprite.spritecollide(dino, cactus_sprites, False):
#         done = True
#
#     # Отрисовка игровых объектов
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)
#
#     # Обновление экрана
#     pygame.display.flip()
#
#     # Задержка
#     clock.tick(60)
#
# # Завершение игры
# pygame.quit()
#
#
#

font_path = "C:/Users/Дениса ПК/Desktop/Шрифты/Doto-VariableFont_ROND,wght.ttf"

import pygame, time

BLACK = (0, 0, 0)

pygame.display.set_caption("Dino Game")
dino_png = pygame.image.load("dino.png")
cactus_png = pygame.image.load("cactus.png")


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([600, 1])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 190


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dino.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 150
        self.y_speed = 0
        self.is_jumping = False

    def update(self):
        self.y_speed += 1
        self.rect.y += self.y_speed
        if self.rect.y >= 150:
            self.rect.y = 150
            self.speed_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.y_speed = -15
            self.is_jumping = True


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cactus.png")
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 150
        self.speed = -10

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < -40:
            self.kill()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(font_path, 36)
        self.text = ("Score: ")
        self.image = self.font.render(self.text, True, BLACK)
        self.score = 0
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 10  # подимати як зробити зробти scale screen

    def update(self):
        self.score += 1
        self.text = ("Score" + str(self.score))
        self.image = self.font.render(self.text, True, BLACK)
        # подумати над тим щоб зробити залежність при збільшенні вікна





pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        self.score = Score()
        self.dino = Dino()
        self.cactus = Cactus()
        self.ground = Ground()
        self.barrier = pygame.sprite.Group(self.cactus)
        self.all_sprites = pygame.sprite.Group(self.dino, self.ground)
        self.start_timer = time.time()

    def start_game(self):
        spawn_timer = 0
        screen = pygame.display.set_mode((600, 200))
        screen.fill(WHITE)
        pygame.display.set_caption("Dino Game")
        ground_png = pygame.draw.rect(screen, BLACK, pygame.Rect(0, 50, 200, 10))
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.jump()
            current_time = pygame.time.get_ticks()
            # Спам кактусів з певною періодичністью 1500 мл с
            if current_time - spawn_timer > 1500:
                cactus = Cactus()
                self.barrier.add(cactus)
                spawn_timer = current_time

            # Оновлюємо группу спрайтів
            self.barrier.update()
            self.all_sprites.update()
            # Завершення гри при зіткненні з кактусом
            if pygame.sprite.spritecollide(self.dino, self.barrier, False):
                done = True

            screen.fill(WHITE)
            self.all_sprites.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


def main():
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()

    # Чи можна встановити відстань за пікселями? наприклад, 20 пікселів = 1 метр, і лічильник підрахує, скільки пікселів ми подолали, і відобразить кількість метрів.
# можливо, у кактуса може бути "очко хітбокс", де, якщо динозавр потрапляє в нього (не торкаючись самого кактуса), він отримує очко

