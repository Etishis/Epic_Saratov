import pygame
import variables as vb
import states as stl

pygame.init()


def motion():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and vb.player_x > -354:
        vb.player_x -= vb.player_speed
        vb.player_walk = stl.WalkState.WALK

    elif keys[pygame.K_RIGHT] and vb.player_x < 657:
        vb.player_x += vb.player_speed
        vb.player_walk = stl.WalkState.WALK

    else:
        vb.player_walk = stl.WalkState.RELAX

