import pygame
import Entity
import time
import random

# Initialize Pygame
pygame.init()

# Setup screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
COLOR = (0, 0, 15)
SCREEN.fill(COLOR)
pygame.display.update()

# Main game loop
if __name__ == "__main__":
    # Space stars
    class Star(Entity.Entity):
        def __init__(self, image, start_x, start_y, speed=0):
            super().__init__(image, start_x, start_y, speed, "cosmetics", "star")

    # Setup base stars
    def create_stars(image_path, quantity, map_width, map_height):
        stars = {}
        for j in range(quantity):
            x = random.randint(0, map_width)
            y = random.randint(0, map_height)
            star = Star(image_path, x, y)
            stars[star.name + str(j)] = (x, y)
        return stars
    
    # Variable to hold stars dictionary with star names and coordinates
    cos_stars = create_stars("./assets/star.png", 50, SCREEN_WIDTH, SCREEN_HEIGHT)
    print(cos_stars)

    # Rerender stars after screen refresh
    def update_stars(keys):
        for name, key in keys.items():
            star = Star("./assets/star.png", key[0], key[1])
            SCREEN.blit(star.image, (key[0], key[1]))

    # Window title
    pygame.display.set_caption("Space Explorer")

    # Ticker
    clock = pygame.time.Clock()

    # Creating new player entity and showing it
    player = Entity.Entity("./assets/basic_player.png", 100, 100, 10, "player", "player")
    player.show()

    # Game loop
    RUNNING = True
    while RUNNING:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        
        # Rerender necissary objects after screen refresh
        SCREEN.fill((COLOR))
        update_stars(cos_stars)
        player.show()
        pygame.display.flip()

        # Maintains game at certain fps
        clock.tick(60)  # 60 fps game

    # If game loop ended then quit the game
    pygame.quit()
