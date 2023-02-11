import os
import sys
import pygame
import requests


# 37.588392,55.734036 0.005,0.005

def draw_(search_params):
    search_api_server = f"https://static-maps.yandex.ru/1.x/?"
    response = requests.get(search_api_server, params=search_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(requests.get(search_api_server, params=search_params))
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load("map.png"), (0, 0))


if __name__ == '__main__':
    pygame.init()
    n = input('Введите координаты и масштаб: ').split()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.

    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    a = n[1].split(',')[0]
    search_params = {
        "ll": n[0],
        "spn": ','.join([a, a]),
        "l": "sat"
    }
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    a = float(a) - 0.05 if search_params["spn"] - 0.05 > 0 else 0.001
                    search_params["spn"] = search_params["spn"] - 0.05 if \
                        search_params["spn"] - 0.05 > 0 else 0.001
                if event.key == pygame.K_PAGEDOWN:
                    search_params["spn"] = search_params["spn"] + 0.05 if\
                        search_params["spn"] + 0.05 <= 50 else 50
        draw_(search_params)
        pygame.display.flip()
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove("map.png")
