import math, os
from operator import index

import pygame
from pygame.locals import *

path_image = "C:\\Users\\Дениса ПК\\Desktop\\Sprites\\Gold-0.png"
path = "C:\\Users\\Дениса ПК\\Desktop\\Sprites\\"

""" Завантажує серію зображень і повертає їх у вигляді списку. 
Parameters: 
path (str): Шлях до каталогу з зображеннями.
name_file (str): Шаблон імені файлу. 
count_img (int): Кількість зображень. 
format (str): Формат файлу зображення. 
Returns: list: Список завантажених зображень. """


def create_images(path, name_file, count_img, format):
    images = list()
    for i in range(count_img):
        file_path = f"{path}{name_file}{i}.{format}"
        if os.path.exists(file_path):
            images.append(pygame.image.load(f"{path}{name_file}{i}.{format}"))
        else:
            print(f"Файл не знайдено: {file_path}")
    return images


"""
Отримує лист зобрежень та повертає список з них у вказаному розмірі
Parameters:
images(list.pygame.images) : список картинок для зміни розміру 
size (list(int)) Список потрібного розміру картинки
Returns: list: Список зображень нового розміру.
"""


def resize_images(images, size):
    new_images = list()
    for img in images:
        new_images.append(pygame.transform.scale(img, size))
    return new_images


def home_work():
    images = list()
    for i in range(7):
        images.append(pygame.image.load(f"{path}Gold-{i}.png"))
    return images


def get_polygon_points(center, size, count_point):
    points = []
    angl = 365 / count_point
    for i in range(count_point):
        angle = math.radians(i * angl)
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append([x, y])
    return points


pygame.init()
screen = pygame.display.set_mode((600, 600))

surface = pygame.Surface((500,500))

circle_position = (300, 300)
circle_radius = 50
circle_color = (255, 0, 0)

points = get_polygon_points((150, 150), 50, 6)
image = pygame.image.load(path_image)

resized_image = pygame.transform.scale(image, (200, 200))

rotate_img = pygame.transform.rotate(image, 90)
image.set_colorkey((255, 255, 255))
get_color = image.get_at((10, 10))
print(get_color)
running = True
images = create_images(path, 'Gold-', 7, 'png')
images = resize_images(images, (50, 50))
clock = pygame.time.Clock()
i = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255, 255, 255))

    # pygame.draw.circle(surface, circle_color, circle_position, circle_radius, 2)
    # pygame.draw.rect(surface, (0, 0, 255), [100, 100, 400, 100], 2)
    # pygame.draw.line(surface, (200,200,200), [0,0], [100,100], 2)
    # pygame.draw.polygon(surface, (255, 74, 199), points, 2)
    if i >= len(images):
        i = 0
    screen.blit(images[i], (0, 0))
    i += 1
    clock.tick(14)
    pygame.display.update()
