# Disable hello from the pygame community 
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' 

# import pygame module
import pygame
import random

# initializing pygame
pygame.init()

# set screen width and height
screen_width = 900
screen_height = 600

# setting game window
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game by arnav")
pygame.display.update()

# game specific variables
exit_game = False
game_over = False
snake_x = 65
snake_y = 65
velocity_x = 0
velocity_y = 0
food_x = random.randint(20, screen_width/1.5)
food_y = random.randint(20, screen_height/1.5)
score = 0
init_velocity = 7
snake_size = 20
food_size = 15
fps = 55
sensitivity = 15

# pygame clock
clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
purple = (128, 0, 128)

# font
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

# Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    
    snake_x += velocity_x
    snake_y += velocity_y

    if (abs(snake_x - food_x)<sensitivity and abs(snake_y - food_y)<sensitivity):
        score += 1
        food_x = random.randint(20, screen_width/2)
        food_y = random.randint(20, screen_height/2)

    game_window.fill(white)
    # print(f"Score: {score*10}")
    text_screen(f"Score: "+ str(score*10), purple, 10, 5)
    pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
    