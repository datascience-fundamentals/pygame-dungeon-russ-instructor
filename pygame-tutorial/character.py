import pygame
import constants as cons


class Character:
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, cons.RED, self.rect)
