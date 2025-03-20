from threading import Barrier

import gameObject, pygame
from gameObject import *


class Game():
    def __init__(self, screen, screen_color, player, barrier_img, barrier_pos, ui_score, ground):
        self.screen = screen
        self.screen_color = screen_color
        self.player = player
        self.barrier = Barrier(barrier_img, barrier_pos)
        self.ui_score = ui_score
        self.uiGroup = pygame.sprite.Group(ui_score)
        self.gameObjects = pygame.sprite.Group(ground, player)
        self.barriers = pygame.sprite.Group()
        self.barrier_img = barrier_img
        self.barrier_pos = barrier_pos

    def play(self):
        # Установка начального значения таймера для появления кактусов
        spawn_timer = 0
        runner = True
        clock = pygame.time.Clock()

        while runner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runner = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.jump()
            # Обновление игровых объектов
            self.gameObjects.update()

            # Создание новых преград
            current_time = pygame.time.get_ticks()
            if current_time - spawn_timer > 1500:
                new_barrier = Barrier(self.barrier_img, self.barrier_pos)
                self.gameObjects.add(new_barrier)
                self.barriers.add(new_barrier)
                spawn_timer = current_time
            # Проверка столкновения
            if pygame.sprite.spritecollide(self.player, self.barriers, False):
                runner = False

            for sprite in self.barriers:
                if sprite.rect.x < 0:
                    self.ui_score.update()
                    self.barriers.remove(sprite)

            # Отрисовка игровых объектов
            self.screen.fill(self.screen_color)
            self.gameObjects.draw(self.screen)
            self.uiGroup.draw(self.screen)
            # Обновление экрана
            pygame.display.flip()
            # Задержка
            clock.tick(60)
        pygame.quit()
