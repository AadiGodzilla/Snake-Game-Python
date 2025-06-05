import pygame
from .scene import Scene
from ..entities import Snake, Apple, Score
from ..collision import *
from ..config import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..window import Window

class GameScene(Scene):
    def __init__(self, window: 'Window'):
        super().__init__(window)
        self.__snake = Snake(self.window.screen, 10, 10)
        self.__apple = Apple(self.window.screen)
        self.__score = Score()

    def update(self):
        self.__snake.update()

        if self.__snake.snake_body_collision() or self.__snake.head_boundary_collision():
            self.window.game_over = True

        if self.window.game_over:
            self.__snake.reset()
            self.__score.reset()

        if collision(self.__snake.head.rect, self.__apple.rect):
            self.__apple.randomize_position()
            self.__snake.grow()
            self.__score.increment()

    def render(self):
        self.window.screen.fill("black")

        for i in range(Settings.TILE_ROWS):
            for j in range(Settings.TILE_COLS):
                if (i + j) % 2 == 0:
                    color = (146, 235, 52)
                else:
                    color = (110, 235, 52)
                pygame.draw.rect(self.window.screen, color, (
                    j * Settings.TILE_SIZE,
                    i * Settings.TILE_SIZE,
                    Settings.TILE_SIZE,
                    Settings.TILE_SIZE
                ))

        self.__snake.render()
        self.__apple.render()
        self.__score.render(self.window.screen)

        pygame.display.flip()