import pygame
import math
import constants as cons
from character import Character


class Weapon():
    def __init__(self, image: pygame.Surface):
        self.__original_image = image
        self.__angle = 0
        self.__image = pygame.transform.rotate(
            self.__original_image, self.__angle)
        self.__rect = self.__image.get_rect()

    def update(self, player: Character):
        self.__rect.center = player.rect.center
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.__rect.centerx
        # negative because pygame and coordinates increase down the screen
        y_dist = -(pos[1] - self.__rect.centery)
        self.__angle = math.degrees(math.atan2(y_dist, x_dist))

    def draw(self, surface: pygame.Surface):
        self.__image = pygame.transform.rotate(
            self.__original_image, self.__angle)
        coordinates = (self.__rect.centerx - int(self.__image.get_width()/2),
                       self.__rect.centery - int(self.__image.get_height()/2))
        surface.blit(self.__image, coordinates)
        pygame.draw.rect(surface, cons.GREEN, self.__rect, 1)
