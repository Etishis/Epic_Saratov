import pygame
import variables as vb
import motion as mtn
import sounds
import custom_events
import states as stl
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1171, 877))

pygame.display.set_caption('Epic Saratov')

pygame.display.set_icon(vb.icon)


running = True
map_index = 0
action_index = 0
channelOne = pygame.mixer.Channel(1)
screen.blit(vb.list_of_maps[map_index], (0, 0))
player_walk_count = 0
SECOND_TIMER = pygame.USEREVENT + 1
timer = 0
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
            if action_index == 0:
                vb.gop_index = 1
                screen.blit(vb.gop_gopov[vb.gop_index], (370, 30))
                vb.min_state_var = stl.MinState.PLAY
                vb.bomj_valera.fill((0, 0, 0, 0))
                channelOne.play(sounds.We_want)
                channelOne.queue(sounds.Krishka)
                vb.guide_text.fill((0, 0, 0, 0))
                action_index += 1
                pygame.time.set_timer(SECOND_TIMER, 1000)

        if keys[pygame.K_2] and map_index == 6:
            if action_index == 0:
                vb.end_state_var = stl.EndingsStates.BORING_END
                sounds.We_are_just_walking.play()
                vb.guide_text.fill((0, 0, 0, 0))
                action_index += 1
                pygame.time.set_timer(SECOND_TIMER, 1000)

        if keys[pygame.K_3] and map_index == 6:
            if action_index == 0:
                vb.end_state_var = stl.EndingsStates.FUN_END
                sounds.General_Gaws_voice.play()
                vb.general_gaws_state_var = stl.GeneralGawsState.NOTABLE
                action_index += 1
                pygame.time.set_timer(SECOND_TIMER, 1000)

    if action_index == 1 and vb.min_count > 0 and map_index == 6:
        pass

    if vb.general_gaws_state_var == stl.GeneralGawsState.NOTABLE:
        screen.blit(vb.general_gaws, (550, 3))
        vb.guide_text.fill((0, 0, 0, 0))

    elif vb.general_gaws_state_var == stl.GeneralGawsState.HIDDEN:
        pass

    if not vb.player_walk.value:
        screen.blit(vb.walk[0], (vb.player_x, vb.player_y))
    else:
        screen.blit(vb.walk[player_walk_count], (vb.player_x, vb.player_y))
        player_walk_count += 1
        if player_walk_count >= len(vb.walk):
            player_walk_count = 0

    if vb.min_state_var == stl.MinState.STOP:
        pass

    elif vb.min_state_var == stl.MinState.PLAY:
        screen.blit(vb.min_count_img, (0, 0))
        screen.blit(vb.min_count_text, (120, 5))
        screen.blit(vb.attack_text, (200, 0))

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
        if event.type == SECOND_TIMER:
            timer += 1
            if timer == 5:
                vb.min_count -= 1
                timer = 0
                vb.min_count_text = vb.font.render(str(vb.min_count), False, pygame.Color('black'))
            if vb.end_state_var.value and timer == 3:
                vb.walk[0].fill((0, 0, 0, 0))
                vb.walk[1].fill((0, 0, 0, 0))
                vb.walk[2].fill((0, 0, 0, 0))
                vb.gop_gopov[0].fill((0, 0, 0, 0))
                vb.gop_gopov[1].fill((0, 0, 0, 0))
                vb.gop_gopov[2].fill((0, 0, 0, 0))
                vb.bomj_valera.fill((0, 0, 0, 0))
                vb.general_gaws.fill((0, 0, 0, 0))
                vb.min_count_img.fill((0, 0, 0, 0))
                vb.min_count_text.fill((0, 0, 0, 0))
                map_index = vb.end_state_var.value
                vb.min_state_var = stl.MinState.STOP

            if vb.min_count == 0:
                if not vb.end_state_var.value and vb.min_count == 0:
                    vb.end_state_var = stl.EndingsStates.FAIL_END

            if vb.min_count == -1:
                running = False
                pygame.quit()

        if event.type == pygame.KEYDOWN:
            if vb.min_count > 0 and map_index == 6:
                if event.key == pygame.K_a and vb.end_state_var != stl.EndingsStates.CANON_END:
                    vb.end_state_var = stl.EndingsStates.CANON_END
                    vb.gop_index = 2
                    sounds.Ebkarniy_Babay.play()
                    vb.min_state_var = stl.MinState.STOP
