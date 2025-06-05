import pygame
from .scene import Scene
from ..config import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..window import Window

class GameOverScene(Scene):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self.__font = pygame.font.SysFont("arial.ttf", 75)
        self.__text = self.__font.render("GAME OVER", True, (255, 255, 255))
        self.__rect = self.__text.get_rect()
        self.__rect.center = (Settings.SCREEN_WIDTH / 2, Settings.SCREEN_HEIGHT / 2)

    def update(self):
        pass

    def render(self):
        self.window.screen.fill((0, 0, 0))

        self.window.screen.blit(self.__text, self.__rect)

        pygame.display.flip()