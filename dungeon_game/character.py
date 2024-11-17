import pygame
import constants as cons
import math


class Character:
    def __init__(self, x, y, mob_animations, char_type):
        self.__char_type = char_type
        self.__flip = False
        self.__animation_list = mob_animations[self.__char_type]
        self.__frame_index = 0
        # 0: idle, 1: run
        self.__action = 0
        # how time has passed since the last time since game started
        self.__update_time = pygame.time.get_ticks()
        self.__running = False
        self.__image = self.__animation_list[self.__action][self.__frame_index]
        self.__rect = pygame.Rect(0, 0, 40, 40)
        self.__rect.center = (x, y)

    def move(self, dx, dy):
        self.__running = False

        if dx != 0 or dy != 0:
            self.__running = True

        # self.flip = True if dx < 0 else False
        if dx < 0:
            self.__flip = True
        elif dx > 0:
            self.__flip = False

        # control diagonal speed
        if dx != 0 and dy != 0:
            dx *= (math.sqrt(2)/2)
            dy *= (math.sqrt(2)/2)

        self.__rect.x += dx
        self.__rect.y += dy

    def update(self):
        # check what action the player is performing
        if self.__running == True:
            self.update_action(1)  # 1:run
        else:
            self.update_action(0)  # 0:idle

        animation_cooldown = cons.ANIMATION_COOLDOWN
        # handle animation
        # update image
        self.__image = self.__animation_list[self.__action][self.__frame_index]
        # check if enought time  has passed since the last update
        if pygame.time.get_ticks() - self.__update_time > animation_cooldown:
            self.__frame_index += 1
            self.__update_time = pygame.time.get_ticks()
            # check if the animation has finished
            if self.__frame_index == len(self.__animation_list[self.__action]):
                self.__frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.__action:
            self.__action = new_action
            # update the animation settings
            self.__frame_index = 0
            self.__update_time = pygame.time.get_ticks()

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.__image, self.__flip, False)
        surface.blit(flipped_image, self.__rect)
        pygame.draw.rect(surface, cons.RED, self.__rect, 1)
