from Vector2 import Vector2
import pygame

class Circle():
    def __init__(self, position : Vector2, radius : float = 20, color : tuple[int, int, int] = (255, 255, 255)):
        self.pos = position
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos.deconstruct(), self.radius, 0)
