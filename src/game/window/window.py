import pygame
from ..config import Settings 
from ..events import poll_events
from ..scenes import SceneManager, SceneID

class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Settings.TITLE)
        pygame.display.set_icon(pygame.image.load("assets/icon.ico"))

        self.screen: pygame.Surface = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        self.__clock = pygame.time.Clock()
        self.running = True
        self.pause = False
        self.game_over = False

        self.__sceneManager = SceneManager(self)

    def run(self):
        while self.running:
            poll_events(self)

            if self.pause:
                self.__sceneManager.change(SceneID.PAUSE)
            elif self.game_over:
                self.__sceneManager.change(SceneID.GAME_OVER)
            else:
                self.__sceneManager.change(SceneID.GAME)

            self.__sceneManager.run()

            self.__clock.tick(12)
        pygame.quit()