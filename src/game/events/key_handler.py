import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..window import Window

__keyboard: pygame.key.ScancodeWrapper | None = None

def poll_events(window: 'Window'):
    global __keyboard

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.pause = not window.pause
            if window.game_over:
                window.game_over = False

        __keyboard = pygame.key.get_pressed()


def is_key_pressed(key: int) -> bool:
    global __keyboard
    return __keyboard[key]