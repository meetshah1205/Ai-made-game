import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title and colors
pygame.display.set_caption("Zyntax: Jungle Survival")
background_color = (34, 139, 34)  # Jungle green

# Player properties
player_color = (255, 0, 0)  # Red 
player_width = 40
player_height = 60
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 3 

# Clock for frame rate control
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move left
        player_x -= player_speed
    if keys[pygame.K_d]:  # Move right
        player_x += player_speed
    if keys[pygame.K_w]:  # Move up
        player_y -= player_speed
    if keys[pygame.K_s]:  # Move down
        player_y += player_speed

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

    # Limit frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
