import pygame
import states as stl


pygame.init()

icon = pygame.image.load('images/icon.png')

bg_sound = pygame.mixer.Sound('sounds/ost.mp3')

font = pygame.font.Font('D:/Emin/My programmes/Game/font/VT323/VT323-Regular.ttf', 36)


guide_text = font.render("We want to escape Saratov! - 1    We just walking. - 2    General Gaws - 3",
                         False, pygame.Color('white'))

attack_text = font.render('"A"- attack', False, pygame.Color('white'))

start_button = pygame.image.load('D:/Emin/My programmes/Game/images/need/start.png')

key = pygame.image.load('images/door_and_key/key.png')
door = pygame.image.load('images/door_and_key/door.png')

square = pygame.Surface((75, 150))
square.fill('Black')

bomj_valera = pygame.image.load('images/Bomj_Valera/Bomj_Valera.png')
valera_x = 100
valera_y = 100

general_gaws = pygame.image.load('images/General_Gaws/General_Gaws.png')

general_gaws_state_var = stl.GeneralGawsState.HIDDEN

walk = [
    pygame.image.load('images/Player/Vasya_Petkin.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step1.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step2.png')
]


player_walk = stl.WalkState.RELAX

gop_gopov = [
    pygame.image.load('images/Gop_Gopov/stand.png'),
    pygame.image.load('images/Gop_Gopov/angry.png'),
    pygame.image.load('images/Gop_Gopov/fail.png'),
]
gop_index = 0

list_of_maps = [
    pygame.image.load('images/bgs/menu.png'),       # 0
    pygame.image.load('images/bgs/bedroom.png'),        # 1
    pygame.image.load('images/bgs/room.png'),       # 2
    pygame.image.load('images/bgs/castle.png'),     # 3
    pygame.image.load('images/bgs/basement.png'),       # 4
    pygame.image.load('images/bgs/wall.png'),       # 5
    pygame.image.load('images/bgs/street.png'),     # 6
    pygame.image.load('images/Endings/fail_end.png'),       # 7
    pygame.image.load('images/Endings/canon_end.png'),        # 8
    pygame.image.load('images/Endings/bor_end.png'),     # 9
    pygame.image.load('images/Endings/fun_end.png'),  # 10

]
end_state_var = stl.EndingsStates.NOT_END


min_count = 3
min_count_img = pygame.image.load('images/need/minutes.png')
min_count_text = font.render(str(min_count), False, pygame.Color('black'))
min_state_var = stl.MinState.STOP

is_win = False
is_bored = False

player_count = 3
player_speed = 100
player_x = -354
player_y = 370
