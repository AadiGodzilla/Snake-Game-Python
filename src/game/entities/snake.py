import pygame
from pygame.rect import Rect
from enum import Enum 
from ..config import Settings
from ..events import is_key_pressed
from typing import List
from ..collision import collision
from ..resource import Texture, load_texture
from copy import deepcopy

class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2
    RIGHT = 3

class Segment:
    def __init__(self, direction: Direction, rect: Rect):
        self.direction: Direction = direction
        self.rect: Rect = rect

class Snake:
    def __init__(self, screen: pygame.Surface, init_x: int, init_y: int):
        self.__init_x = init_x
        self.__init_y = init_y
        self.__body_size = 4
        self.__direction = Direction.RIGHT
        self.__screen = screen
        self.head = Segment(
            self.__direction, 
            Rect(
                init_x * Settings.TILE_SIZE,
                init_y * Settings.TILE_SIZE,
                Settings.TILE_SIZE, 
                Settings.TILE_SIZE
            )
        )
        self.sprites: List[Texture] = [
            load_texture("head_up", "assets/head_up.png"),
            load_texture("head_down", "assets/head_down.png"),
            load_texture("head_left", "assets/head_left.png"),
            load_texture("head_right", "assets/head_right.png"),
            load_texture("top_left", "assets/body_topleft.png"),
            load_texture("top_right", "assets/body_topright.png"),
            load_texture("bottom_left", "assets/body_bottomleft.png"),
            load_texture("bottom_right", "assets/body_bottomright.png"),
            load_texture("horizontal", "assets/body_horizontal.png"),
            load_texture("vertical", "assets/body_vertical.png"),
            load_texture("tail_up", "assets/tail_up.png"),
            load_texture("tail_down", "assets/tail_down.png"),
            load_texture("tail_left", "assets/tail_left.png"),
            load_texture("tail_right", "assets/tail_right.png"),
        ]
        self.body: List[Segment] = []

        for i in range(self.__body_size):
            seg = Segment(self.__direction.__copy__(), Rect(
                self.head.rect.x - (i * Settings.TILE_SIZE), 
                self.head.rect.y, 
                self.head.rect.width, 
                self.head.rect.height
            ))
            self.body.append(seg)


    def update(self):
        if (is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w)) and self.head.direction != Direction.DOWN:
            self.head.direction = Direction.UP
        elif (is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s)) and self.head.direction != Direction.UP:
            self.head.direction = Direction.DOWN
        elif (is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a)) and self.head.direction != Direction.RIGHT:
            self.head.direction = Direction.LEFT
        elif (is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d)) and self.head.direction != Direction.LEFT:
            self.head.direction = Direction.RIGHT

        match self.head.direction:
            case Direction.UP:
                self.head.rect.y -= Settings.TILE_SIZE
            case Direction.DOWN:
                self.head.rect.y += Settings.TILE_SIZE
            case Direction.LEFT:
                self.head.rect.x -= Settings.TILE_SIZE
            case Direction.RIGHT:
                self.head.rect.x += Settings.TILE_SIZE

        self.body.insert(0, deepcopy(self.head)) 
        if len(self.body) != self.__body_size:
            self.body.pop()
        

    def head_boundary_collision(self) -> bool:
        if (self.head.rect.x >= Settings.SCREEN_WIDTH or 
        self.head.rect.y >= Settings.SCREEN_HEIGHT or 
        self.head.rect.x < 0 or self.head.rect.y < 0):
            self.reset()
            return True
        else:
            return False


    def snake_body_collision(self) -> bool:
        for index, seg in enumerate(self.body):
            if index == 0:
                continue

            if collision(Rect(seg.rect), Rect(self.head.rect)):
                self.reset()
                return True
            
        return False


    def grow(self):
        self.__body_size += 1


    def reset(self):
        self.__init__(self.__screen, self.__init_x, self.__init_y)

    def render(self):
        for index, seg in enumerate(self.body):
            if index == 0 or seg == self.body[-1]:
                continue

            prev = self.body[index - 1]

            if ((prev.direction == Direction.UP and seg.direction == Direction.RIGHT) or 
                (prev.direction == Direction.LEFT and seg.direction == Direction.DOWN)):
                self.sprites[4].render(self.__screen, Rect(seg.rect))
            elif ((prev.direction == Direction.UP and seg.direction == Direction.LEFT) or 
                (prev.direction == Direction.RIGHT and seg.direction == Direction.DOWN)):
                self.sprites[5].render(self.__screen, Rect(seg.rect))
            elif ((prev.direction == Direction.LEFT and seg.direction == Direction.UP) or 
                (prev.direction == Direction.DOWN and seg.direction == Direction.RIGHT)):
                self.sprites[6].render(self.__screen, Rect(seg.rect))
            elif ((prev.direction == Direction.DOWN and seg.direction == Direction.LEFT) or 
                (prev.direction == Direction.RIGHT and seg.direction == Direction.UP)):
                self.sprites[7].render(self.__screen, Rect(seg.rect))
            elif seg.direction == Direction.LEFT or seg.direction == Direction.RIGHT:
                self.sprites[8].render(self.__screen, Rect(seg.rect))
            elif seg.direction == Direction.UP or seg.direction == Direction.DOWN:
                self.sprites[9].render(self.__screen, Rect(seg.rect))
                

        match self.head.direction:
            case Direction.UP:
                self.sprites[0].render(self.__screen, Rect(self.head.rect))
            case Direction.DOWN:
                self.sprites[1].render(self.__screen, Rect(self.head.rect))
            case Direction.LEFT:
                self.sprites[2].render(self.__screen, Rect(self.head.rect))
            case Direction.RIGHT:
                self.sprites[3].render(self.__screen, Rect(self.head.rect))

        match self.body[-2].direction:
            case Direction.DOWN:
                self.sprites[10].render(self.__screen, Rect(self.body[-1].rect))
            case Direction.UP:
                self.sprites[11].render(self.__screen, Rect(self.body[-1].rect))
            case Direction.RIGHT:
                self.sprites[12].render(self.__screen, Rect(self.body[-1].rect))
            case Direction.LEFT:
                self.sprites[13].render(self.__screen, Rect(self.body[-1].rect))
