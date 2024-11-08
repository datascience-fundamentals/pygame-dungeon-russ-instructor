import pygame
import constants as cons
import math


class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):
        # control diagonal speed
        if dx != 0 and dy != 0:
            dx *= (math.sqrt(2)/2)
            dy *= (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, cons.RED, self.rect)
