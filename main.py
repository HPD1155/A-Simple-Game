import pygame
import Entity
from pygame.locals import *
import effects
import time

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set caption
pygame.display.set_caption("Space Explorer")

# Create a clock object for managing FPS
clock = pygame.time.Clock()

## Set up Entities
# Main Player
player = Entity.PlayerCharacter(100, 100, "./assets/basic_player.png", 10, 100)
# Background Stars
stars = effects.create_stars(100, SCREEN_WIDTH, SCREEN_HEIGHT)

## Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # basic player controls (We will update this later with smoother movement)
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player.rect.y -= player.speed
            elif event.key == K_s:
                player.rect.y += player.speed
            elif event.key == K_a:
                player.rect.x -= player.speed
            elif event.key == K_d:
                player.rect.x += player.speed
            # Check if player needed rerender
            elif event.key == K_DELETE:
                pygame.display.set_caption("Space Explorer (Rerendering Screen...)")
                time.sleep(0.5)
                SCREEN_WIDTH = 800
                SCREEN_HEIGHT = 600
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                screen.fill((0, 0, 15))
                player = Entity.PlayerCharacter(100, 100, "./assets/basic_player.png", 10, 100)
                stars = effects.create_stars(100, SCREEN_WIDTH, SCREEN_HEIGHT)
                pygame.display.set_caption("Space Explorer")

    # Clear the screen
    screen.fill((0, 0, 15))  # Fill with space-blue

    # Render Background behind player
    effects.render_stars(stars, screen, "./assets/star.png")
    # Render Player
    player.render(screen)


    # Update the display
    pygame.display.update()

    # Limit FPS
    clock.tick(100)  # Aim for 100 FPS

# Quit Pygame
pygame.quit()
