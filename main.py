# Import necessary libraries
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random
import sys

# Initialize the Pygame library
pygame.init()

# Set screen dimensions
screen_width = 900
screen_height = 600

# Create the game window and set its title
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game by arnav")
pygame.display.update()

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Define color constants
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
purple = (128, 0, 128)

# Create a font for displaying text
font = pygame.font.SysFont(None, 55)

# Function to display text on the screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

# Function to draw the snake on the screen
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# Main game loop
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 65
    snake_y = 65
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width // 1.5)
    food_y = random.randint(20, screen_height // 1.5)
    score = 0
    init_velocity = 7
    snake_size = 20
    food_size = 15
    fps = 55
    sensitivity = 15
    snake_list = []
    snake_length = 1

    while not exit_game:

        if exit_game:
            sys.exit(0)

        if game_over:
            game_window.fill(white)
            text_screen("Game Over. Press Enter to start again!", red, 100, screen_height/2 - 25)
            text_screen(f"Your score was {str(score * 10)}", red, 100, screen_height/2 - 100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
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

            if (abs(snake_x - food_x) < sensitivity and abs(snake_y - food_y) < sensitivity):
                score += 1
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length += 3

            game_window.fill(white)
            text_screen(f"Score: " + str(score * 10), purple, 10, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            plot_snake(game_window, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    pygame.init()
    game_loop()
    pygame.quit()
    sys.exit(0)
