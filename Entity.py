import pygame

# Player Character
class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed, health):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.health = health
    def render(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

