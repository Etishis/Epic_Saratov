import pygame
import variables as vb
import motion as mtn
import sounds
import custom_events
from time import sleep

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Epic Saratov')

pygame.display.set_icon(vb.icon)


ost = pygame.mixer.music.load('D:/Emin/My programmes/Game/sounds/ost.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


running = True
map_index = 0
channelOne = pygame.mixer.Channel(1)
vb.screen.blit(vb.list_of_maps[map_index], (0, 0))
while running:

    clock.tick(10)

    vb.screen.blit(vb.list_of_maps[map_index], (0, 0))

    if map_index == 5:
        vb.screen.blit(vb.bomj_valera, (100, 100))

    if map_index == 6:
        vb.screen.blit(vb.bomj_valera, (100, 100))

    vb.screen.blit(vb.walk[vb.player_count], (vb.player_x, vb.player_y))
    vb.screen.blit(vb.start_button, (875, 777))

    player_rect = vb.walk[0].get_rect(topleft=(vb.player_x, vb.player_y))
    start_button_rect = vb.start_button.get_rect(topleft=(1200, 870))

    if player_rect.colliderect(start_button_rect):
        vb.player_x = -354
        vb.player_y = 370

        map_index = custom_events.new_level(map_index)


        if map_index == 1:
            sounds.start_Vasya_voice.play()

        if map_index == 3:
            sounds.door_is_closed.play()

        if map_index == 5:
            channelOne.play(sounds.help_Vasya)
            channelOne.queue(sounds.Bomj_Valera_voice)

        if map_index == 6:
            vb.player_speed = 0

    mtn.motion()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

