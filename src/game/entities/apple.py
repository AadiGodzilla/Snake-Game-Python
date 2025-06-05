import pygame
import random
from ..config import Settings
from ..resource import load_texture, Texture

class Apple:
    def __init__(self, screen: pygame.Surface):
        self.__screen = screen
        self.rect = pygame.rect.Rect(0, 0, Settings.TILE_SIZE, Settings.TILE_SIZE)
        self.texture: Texture = load_texture("apple", "assets/apple.png")

        self.randomize_position()

    def randomize_position(self):
        rand_x = random.randint(0, Settings.TILE_COLS - 1) * Settings.TILE_SIZE
        rand_y = random.randint(0, Settings.TILE_ROWS - 1) * Settings.TILE_SIZE

        self.rect.x = rand_x
        self.rect.y = rand_y

    def render(self):
        self.texture.render(self.__screen, self.rect)