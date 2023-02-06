import pygame

from Samples.mapapi_PG import show_map
import sys
import os


pygame.init()
font = pygame.font.Font(None, 20)
try:
    coords = input('Введите координаты: ').split()
    coords = list(map(float, coords))
    size = int(input('Введите масштаб: '))

    assert 17 >= size >= 0
except ValueError:
    print('Неверные значения! Повторите попытку')
    sys.exit()
except AssertionError:
    print('Неверный уровень масштаба (0-17)')
    sys.exit()

a = show_map(f'll={",".join(map(str, coords))}&spn=1,1', 'map', f'z={size}')
print(coords)
text_surface = font.render(f'Координаты: {", ".join(list(map(str, coords)))}, масштаб: 1 к {size}',
                           True, pygame.Color('black'))
running = True

screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Большая задача по MAPS.APi')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(a, (0, 0))
    screen.blit(text_surface, (2, 430))
    pygame.display.flip()
os.remove('map.png')
pygame.quit()
