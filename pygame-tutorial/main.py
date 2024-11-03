import pygame
import constants as cons
from character import Character

pygame.init()

# setting the screen size
screen = pygame.display.set_mode((cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT))
# changing the game title
pygame.display.set_caption("Dungeon Crawler")

# define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# create player
player = Character(100, 100)

# main game loop
run = True
while run == True:
    # calculate player movement
    dx = 0
    dy = 0

    if moving_right == True:
        dx = 5
    if moving_left == True:
        dx = -5
    if moving_up == True:
        dy = -5
    if moving_down == True:
        dy = 5

    print(f"{str(dx)} , {str(dy)}")

    # draw player on screen
    player.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

    pygame.display.update()

pygame.quit()
