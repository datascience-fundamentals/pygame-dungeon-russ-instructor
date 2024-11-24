import pygame
import constants as cons
from character import Character


class Weapon():
    def __init__(self, image):
        self.__original_image = image
        self.__angle = 0
        self.__image = pygame.transform.rotate(
            self.__original_image, self.__angle)
        self.__rect = self.__image.get_rect()

    def update(self, player: Character):
        self.__rect.center = player.rect.center

    def draw(self, surface: pygame.Surface):
        surface.blit(self.__image, self.__rect)
        pygame.draw.rect(surface, cons.GREEN, self.__rect, 1)
