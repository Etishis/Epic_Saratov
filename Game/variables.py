import pygame

pygame.init()

icon = pygame.image.load('images/icon.png')

bg_sound = pygame.mixer.Sound('sounds/ost.mp3')

font = pygame.font.Font('D:/Emin/My programmes/Game/font/VT323/VT323-Regular.ttf', 36)
guide_text = font.render("We want to escape Saratov! - 1    We just walking. - 2    General Gaws - 3",
                         False, pygame.Color('white'))

start_button = pygame.image.load('D:/Emin/My programmes/Game/images/need/start.png')

key = pygame.image.load('images/door_and_key/key.png')
door = pygame.image.load('images/door_and_key/door.png')

square = pygame.Surface((75, 150))
square.fill('Black')

bomj_valera = pygame.image.load('images/Bomj_Valera/Bomj_Valera.png')
valera_x = 100
valera_y = 100

walk = [
    pygame.image.load('images/Player/Vasya_Petkin.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step1.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step2.png')
]

gop_gopov = [
    pygame.image.load('images/Gop_Gopov/stand.png'),
    pygame.image.load('images/Gop_Gopov/angry.png'),
    pygame.image.load('images/Gop_Gopov/fail.png'),
]
gop_index = 0

list_of_maps = [
    pygame.image.load('images/bgs/menu.png'),
    pygame.image.load('images/bgs/bedroom.png'),
    pygame.image.load('images/bgs/room.png'),
    pygame.image.load('images/bgs/castle.png'),
    pygame.image.load('images/bgs/basement.png'),
    pygame.image.load('images/bgs/wall.png'),
    pygame.image.load('images/bgs/street.png'),
    pygame.image.load('images/bgs/street.png')
]


player_count = 0
player_speed = 100
player_x = -354
player_y = 370
