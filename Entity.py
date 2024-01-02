import pygame
import main

types = ["player", "enemy", "asteroid", "material", "cosmetics"]

class Entity(pygame.sprite.Sprite):
    """
    Base class for all entities in the game.
    """
    def __init__(self, image, start_x, start_y, speed, obj_type, name):
        """
        Initialize an entity with the given parameters.

        Parameters:
        image (str): Path to the image file for the entity's sprite.
        start_x (int): The starting x-coordinate of the entity.
        start_y (int): The starting y-coordinate of the entity.
        speed (int): The speed at which the entity moves.
        obj_type (str): The type of the entity, must be one of the predefined types.
        name (str): The name of the entity.

        Raises:
        ValueError: If the obj_type is not in the predefined types list.
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.s_x = start_x
        self.s_y = start_y
        self.speed = speed
        if obj_type in types:
            self.type = obj_type
        else:
            raise ValueError(f"Invalid type: {obj_type}")
        self.name = name
    def show(self):
        """
        Displays the image of the object on the screen at the specified coordinates.

        Parameters:
            None

        Returns:
            None
        """
        main.SCREEN.blit(self.image, (self.s_x, self.s_y))
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        