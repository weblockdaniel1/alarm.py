import pygame
import time

# Initialize the game
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up game variables
snake_block = 10
snake_speed = 15

# Set up the snake
x, y = width / 2, height / 2
x_change, y_change = 0, 0

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    # Update the snake's position
    x += x_change
    y += y_change

    # Draw the snake and the screen
    display.fill(black)
    pygame.draw.rect(display, white, [x, y, snake_block, snake_block])
    pygame.display.update()

    # Set the frame rate
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
