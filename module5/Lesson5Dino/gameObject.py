import pygame
from abc import ABC, abstractmethod


# pygame.init()

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass


class Updatable(ABC):
    @abstractmethod
    def update(self):
        pass


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]


#
# self.image = pygame.Surface([600, 1])
# self.image.fill(BLACK) add by create

class Ground(GameObject):
    def __init__(self, img, position):
        super().__init__(img, position)


path_dino = "dino.png"


class Dino(GameObject, Updatable):

    def __init__(self, image, position):
        super(Dino, self).__init__(image, position)
        self.y_speed = 0
        self.is_jumping = False
        self.temp_running = 1

    def update(self):
        self.y_speed += self.temp_running
        self.rect.y += self.y_speed
        if self.rect.y > 150:  # тут надо поправить  это координа границы пола,
            # нужно переписать брав обьект пол и брав его координату
            self.rect.y = 150
            self.y_speed = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.y_speed = -15
            self.is_jumping = True


class Barrier(GameObject, Updatable):
    def __init__(self, image, position):
        super(Barrier, self).__init__(image, position)
        self.speed = -10

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < -40:
            self.kill()


class Score(GameObject, Updatable):
    textUI = "Score: "

    def __init__(self, text, position, colorText, textUI, font):
        super().__init__(text, position)
        self.color = colorText
        self.score = 0
        self.textUI = textUI
        self.font = font
        self.position = position

    def get_position(self):
        return self.position

    def update(self):
        self.score += 1
        current_txt = self.textUI + str(self.score)
        self.image = self.font.render(current_txt, True, self.color)
