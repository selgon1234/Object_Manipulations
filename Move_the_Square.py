import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Square")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up square
square_size = 50
x, y = width // 2, height // 2
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)  # Delay to control frame rate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))
    pygame.display.update()

# Quit
pygame.quit()
sys.exit()
