import pygame
from pygame.locals import *
import random

def create_stars(density, screen_x, screen_y):
    stars = {}
    for i in range(density):
        coordinates = (random.randint(0, screen_x), random.randint(0, screen_y))
        stars["star_" + str(i)] = coordinates
    return stars

def render_stars(stars, surface, star_image):
    for star, position in stars.items():
        surface.blit(pygame.image.load(star_image), position)