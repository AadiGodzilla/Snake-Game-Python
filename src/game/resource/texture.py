import copy

import pygame

class Texture:
    def __init__(self, image_file: str):
        self.__image_file = image_file
        self.__image = pygame.image.load(image_file)
        
    def render(self, screen: pygame.surface.Surface, rect: pygame.rect.Rect):
        self.__image = pygame.transform.scale(self.__image, (rect.w, rect.h))
        screen.blit(self.__image, rect)

    def __copy__(self):
        return Texture(self.__image_file)

    def __deepcopy__(self, memo):
        return Texture(copy.deepcopy(self.__image_file, memo))