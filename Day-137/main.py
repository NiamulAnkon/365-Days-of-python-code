import pygame
from pygame.locals import *
import time
import random

pygame.init()

red = (255, 0, 0)
blue = (0, 0, 255)
gray = (192, 192, 192)
green = (0, 255, 0)

win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("consolas", 20)
score_font = pygame.font.SysFont("calibri", 25)

def usr_score(score):
    number = score_font.render("Score: " + str(score), True, blue)
    window.blit(number, [0, 0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake, snake])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width // 2
    y1 = win_height // 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    food_x = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    food_y = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    def message(msg, length):
        msg = font_style.render(msg, True, red)
        window.blit(msg, [win_width // 6, win_height // 3])
        usr_score(length - 1)
        pygame.display.update()

    while not game_over:
        while game_close:
            window.fill(gray)
            message("You have lost, press Q to quit or C to play again", snake_length)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        x1 += x1_change
        y1 += y1_change

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        window.fill(gray)
        pygame.draw.rect(window, red, [food_x, food_y, snake, snake])
        snake_size = [x1, y1]
        snake_length_list.append(snake_size)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        for segment in snake_length_list:
            pygame.draw.rect(window, green, [segment[0], segment[1], snake, snake])

        usr_score(snake_length - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            food_y = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
