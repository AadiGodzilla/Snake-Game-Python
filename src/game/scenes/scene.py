from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..window import Window

class Scene(ABC):
    def __init__(self, window: 'Window'):
        self.window = window
        pass 

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass