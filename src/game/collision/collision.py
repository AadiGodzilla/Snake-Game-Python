import pygame

def collision(rect_a: pygame.rect.Rect, rect_b: pygame.rect.Rect) -> bool:
    return rect_a.x == rect_b.x and rect_a.y == rect_b.y