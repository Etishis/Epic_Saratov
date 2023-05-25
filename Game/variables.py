import pygame

pygame.init()

screen = pygame.display.set_mode((1171, 877))

icon = pygame.image.load('images/icon.png').convert_alpha()

bg_sound = pygame.mixer.Sound('sounds/ost.mp3')

font = pygame.font.Font('D:/Emin/My programmes/Game/font/VT323/VT323-Regular.ttf', 36)

start_button = pygame.image.load('D:/Emin/My programmes/Game/images/need/start.png')

square = pygame.Surface((75, 150))
square.fill('Black')

bomj_valera = pygame.image.load('images/Bomj_Valera/Bomj_Valera.png')

walk = [
    pygame.image.load('images/Player/Vasya_Petkin.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step1.png'),
    pygame.image.load('images/Player/Vasya_Petkin_step2.png')
]


list_of_maps = [
    pygame.image.load('images/bgs/menu.png'),
    pygame.image.load('images/bgs/bedroom.png'),
    pygame.image.load('images/bgs/room.png'),
    pygame.image.load('images/bgs/castle.png'),
    pygame.image.load('images/bgs/basement.png'),
    pygame.image.load('images/bgs/wall.png'),
    pygame.image.load('images/bgs/street.png')
]

player_count = 0
player_speed = 50
player_x = -354
player_y = 370
