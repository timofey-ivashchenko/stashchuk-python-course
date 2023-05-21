import sys

import pygame

pygame.init()
pygame.display.set_caption('Pygame Shooter')

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x = (SCREEN_WIDTH - FIGHTER_WIDTH) / 2
FIGHTER_Y = SCREEN_HEIGHT - FIGHTER_HEIGHT
moving_left, moving_right = False, False
STEP = 1

while True:
    for event in pygame.event.get():
        print(event)
        # Exit the application on the QUIT event.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
        elif event.type == pygame.KEYUP:
            moving_left = False
            moving_right = False

    # Move the ship to the left by clicking on the left arrow.
    if moving_left:
        fighter_x -= STEP
        if fighter_x < 0:
            fighter_x = 0

    # Move the ship to the right when clicking on the right arrow.
    if moving_right:
        fighter_x += STEP
        if fighter_x + FIGHTER_WIDTH > SCREEN_WIDTH:
            fighter_x = SCREEN_WIDTH - FIGHTER_WIDTH

    SCREEN.fill((32, 52, 71))
    SCREEN.blit(FIGHTER_IMAGE, (fighter_x, FIGHTER_Y))
    pygame.display.update()
