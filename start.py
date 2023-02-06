from Samples.mapapi_PG import show_map
import sys
import os
import pygame

pygame.init()
font = pygame.font.Font(None, 20)
try:
    coords = input('Введите координаты: ').split()
    coords = list(map(float, coords))
    size = int(input('Введите увеличение: '))
    assert 17 >= size >= 1

except ValueError:
    print('Неверные значения! Повторите попытку')
    sys.exit()
except AssertionError:
    print('Неверный уровень масштаба (0-17)')
    sys.exit()

running = True

screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Большая задача по MAPS.APi')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_PAGEUP:
            size += 1
        elif event.type == pygame.KEYUP and event.key == pygame.K_PAGEDOWN:
            size -= 1
    if 17 < size or size < 1:
        size = size % 18 + 1
    text_surface = font.render(f'Координаты: {", ".join(list(map(str, coords)))}, масштабирование: 1 к {size}',
                               True, pygame.Color('black'))
    a = show_map(f'll={",".join(map(str, coords))}&z={int(size)}')
    os.remove('map.png')
    screen.blit(a, (0, 0))
    screen.blit(text_surface, (2, 430))
    pygame.display.flip()
pygame.quit()
