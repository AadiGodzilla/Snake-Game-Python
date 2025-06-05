import pygame

from ..resource import load_texture

class Score:
    def __init__(self):
        self.__score_count = 0
        self.__font = pygame.font.SysFont("arial.ttf", 32)

        self.__text = self.__font.render(f"{self.__score_count}", True, (255, 255, 255))
        self.__rect = self.__text.get_rect()
        self.__rect.topleft = (45, 20)

        self.__texture = load_texture("apple")
        self.__texture_rect = self.__text.get_rect()
        self.__texture_rect.topleft = (0, 10)
        self.__texture_rect.width = 40
        self.__texture_rect.height = 40

    def increment(self):
        self.__score_count += 1
        
    def reset(self):
        self.__score_count = 0

    def render(self, screen: pygame.surface.Surface):
        self.__text = self.__font.render(f"{self.__score_count}", True, (255, 255, 255))

        self.__texture.render(screen, self.__texture_rect)
        screen.blit(self.__text, self.__rect)