import pygame
import variables as vb

pygame.init()


def motion():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and vb.player_x > -354:
        vb.player_x -= vb.player_speed
        if vb.player_count == 2:
            vb.player_count = 0
        else:
            vb.player_count += 1

    elif keys[pygame.K_d] and vb.player_x < 657:
        vb.player_x += vb.player_speed
        if vb.player_count == 2:
            vb.player_count = 0
        else:
            vb.player_count += 1

    elif keys[pygame.K_w] and vb.player_y > 100:
        vb.player_y -= vb.player_speed
        if vb.player_count == 2:
            vb.player_count = 0
        else:
            vb.player_count += 1

    elif keys[pygame.K_s] and vb.player_y < 370:
        vb.player_y += vb.player_speed
        if vb.player_count == 2:
            vb.player_count = 0
        else:
            vb.player_count += 1

