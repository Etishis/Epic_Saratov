import pygame
import variables as vb
import motion as mtn
import sounds
import custom_events

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1171, 877))

pygame.display.set_caption('Epic Saratov')

pygame.display.set_icon(vb.icon)


running = True
map_index = 0
channelOne = pygame.mixer.Channel(1)
screen.blit(vb.list_of_maps[map_index], (0, 0))
while running:

    clock.tick(10)

    screen.blit(vb.list_of_maps[map_index], (0, 0))

    if map_index == 5:
        screen.blit(vb.bomj_valera, (vb.valera_x, vb.valera_y))

    if map_index == 6:
        screen.blit(vb.bomj_valera, (vb.valera_x, vb.valera_y))
        screen.blit(vb.gop_gopov[vb.gop_index], (370, 30))
        screen.blit(vb.guide_text, (0, 0))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and map_index == 6:
            map_index = 7
            if map_index == 7:
                vb.gop_index = 1
                screen.blit(vb.gop_gopov[vb.gop_index], (370, 30))
                sounds.Krishka.play()

    screen.blit(vb.walk[vb.player_count], (vb.player_x, vb.player_y))
    screen.blit(vb.start_button, (875, 777))

    if map_index == 4:
        screen.blit(vb.key, (500, 800))
        screen.blit(vb.door, (850, 460))

    player_rect = vb.walk[0].get_rect(topleft=(vb.player_x, vb.player_y))
    start_button_rect = vb.start_button.get_rect(topleft=(1200, 870))
    key_rect = vb.key.get_rect(topleft=(990, 850))

    if map_index == 4:
        if player_rect.colliderect(key_rect):
            vb.key.fill((0, 0, 0, 0))
            vb.door.fill((0, 0, 0, 0))

    if player_rect.colliderect(start_button_rect):
        vb.player_x = -354
        vb.player_y = 370

        map_index = custom_events.new_level(map_index)

        if map_index == 1:
            sounds.start_Vasya_voice.play()

        if map_index == 4:
            sounds.door_is_closed.play()

        if map_index == 5:
            channelOne.play(sounds.help_Vasya)
            channelOne.queue(sounds.Bomj_Valera_voice)

        if map_index == 6:
            vb.player_speed = 0
            vb.player_x = -100
            vb.valera_x = -354
            vb.valera_y = 370
            vb.start_button.fill((0, 0, 0, 0))
            sounds.Draduti.play()

    mtn.motion()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
