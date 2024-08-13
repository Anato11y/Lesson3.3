import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/f76ac4.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальные координаты для скорости движения мишени
target_speed_x = random.choice([-0.3, 0.4])
target_speed_y = random.choice([-0.3, 0.4])

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик очков
score = 0
font = pygame.font.SysFont(None, 55)  # Инициализация шрифта для отображения счета

# Функция отображения счета на экране
def display_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

running = True
while running:
    screen.fill(color)
    # Обновление положения мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение со стенами и изменение направления
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  # Увеличение счета

    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    display_score(score)

    pygame.display.update()

pygame.quit
