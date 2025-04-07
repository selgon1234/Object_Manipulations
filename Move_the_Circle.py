import pygame
import sys

# Initialize Pygame
pygame.init()

# Game window setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 48)

# Game loop
def game_loop():
    x = 400
    y = 300
    speed = 1
    circle_radius = 20

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
        
        # Game background
        screen.fill(WHITE)

        # Draw the circle
        pygame.draw.circle(screen, (0, 0, 255), (x, y), circle_radius)

        # Update the display
        pygame.display.update()

# Menu function
def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key to start the game
                    return  # Start the game and exit the menu

        # Menu background
        screen.fill(WHITE)

        # Display title and instructions
        title_text = font.render("Welcome to the Game!", True, BLACK)
        screen.blit(title_text, (200, 100))

        start_text = font.render("Press 'Enter' to Start", True, BLACK)
        screen.blit(start_text, (250, 200))

        # Update the display
        pygame.display.update()

# Main function
def main():
    show_menu()  # Show menu before starting the game
    game_loop()  # Start the game after menu

# Run the main function
main()
