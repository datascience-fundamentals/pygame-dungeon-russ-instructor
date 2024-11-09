import pygame
import constants as cons
import math


class Character:
    def __init__(self, x, y, image):
        self.flip = False
        self.image = image
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):

        self.flip = True if dx < 0 else False

        # control diagonal speed
        if dx != 0 and dy != 0:
            dx *= (math.sqrt(2)/2)
            dy *= (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, cons.RED, self.rect, 1)
