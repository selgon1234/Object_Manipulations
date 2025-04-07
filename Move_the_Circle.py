import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Circle!")

# Define circle parameters
circle_color = (60, 219, 57)  # Red color
circle_radius = 50  # Radius of the circle
x, y = 400, 300  # Initial position of the circle
speed = 1  # Speed of the circle movement

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys currently being pressed
    keys = pygame.key.get_pressed()

    # Move the circle based on keypress
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill the screen with a white color (background)
    screen.fill((255, 255, 255))

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()