import pygame
from .texture import Texture
from typing import Dict
from copy import deepcopy

__cache: Dict[str, Texture] = {}

def load_texture(id: str, image: str = "") -> Texture:
    for keys in __cache.keys():
        if keys == id:
            return deepcopy(__cache[id])
        
    texture = Texture(image)
    __cache[id] = texture

    return deepcopy(texture)