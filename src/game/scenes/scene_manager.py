from typing import TYPE_CHECKING

from .gameover_scene import GameOverScene
from .scene import Scene
from .game_scene import GameScene
from .pause_scene import PauseScene 
from enum import Enum

if TYPE_CHECKING:
    from ..window import Window

class SceneID(Enum):
    GAME = 0
    PAUSE = 1
    GAME_OVER = 2

class SceneManager:

    def __init__(self, window: 'Window'):
        self.scenes: dict[SceneID, Scene] = {
            SceneID.GAME : GameScene(window),
            SceneID.PAUSE : PauseScene(window),
            SceneID.GAME_OVER : GameOverScene(window)
        }
        self.scene_id: SceneID = SceneID.GAME

    def change(self, scene_id: SceneID):
        self.scene_id = scene_id

    def run(self):
        self.scenes[self.scene_id].update()
        self.scenes[self.scene_id].render()