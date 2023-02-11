import os
import sys
import pygame
import requests

# 37.588392,55.734036 0.005,0.005
n = input('Введите координаты и масштаб: ').split()
for i in n:
    map_request = f"https://static-maps.yandex.ru/1.x/?l=sat&ll={n[0]}&spn={n[1]}&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load("map.png"), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.flip()
pygame.quit()
# Удаляем за собой файл с изображением.
os.remove("map.png")