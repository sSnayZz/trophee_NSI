import pygame 
from sys import exit

#initiation du module Pygame
pygame.init()
pygame.mixer.init()


sfx_wind = pygame.mixer.Sound('fx_wind.mp3')
sfx_rain = pygame.mixer.Sound('fx_rain.mp3')
music_starting_menu = pygame.mixer.Sound('track_start.mp3')

#definition de la taille du jeux
Size = (1920/2,1080/2)
screen = pygame.display.set_mode(Size)

#titre afficher en haut de la page
pygame.display.set_caption('The Temple Of The Idol')

#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()

MBG = pygame.image.load('Background_Main_Menu.jpg').convert()
MBG = pygame.transform.scale(MBG,Size)

BGB = pygame.image.load('Background_Battle.jpg').convert()
BGB = pygame.transform.scale(BGB,Size)

BBG = pygame.image.load('Background_Black.png').convert()
BBG = pygame.transform.scale(BBG,Size)


icon = pygame.image.load('game_icon.ico')
pygame.display.set_icon(icon)

font = pygame.font.Font(None, 36)

button_color=(255,255,255)  
button_color_pressed=(200,200,200) 
button_text_color=(0,0,0)
button_width,button_height=200,50
center_x,center_y = (Size[0] - button_width) // 2,(Size[1] - button_height) // 2
button_y_play,button_y_option,button_y_leave=center_y//2,center_y,center_y+center_y//2


button_BG = pygame.image.load('button_background.png').convert()
button_BG = pygame.transform.scale(button_BG,(button_width,button_height))
#
#
#
#
#
#
#
#
# Fonction pour créer un bouton
def draw_button(x, y, width, height, color, pressed_color, text, text_color,is_pressed):
    current_color = pressed_color if is_pressed else color
    pygame.draw.rect(screen, current_color, (x, y, width, height))
    screen.blit(button_BG,(x,y))
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width/2, y + height/2))
    screen.blit(button_text, text_rect)
#
#
#
#
#
#
#
#
def play_image(chemin,type_fichier,stage,exceed):
    stage+=1
    if stage>=exceed+1:
        stage=1
    return [chemin+str(stage)+type_fichier,stage]
#
#
#
#
#
#
#
#
def wait(time):
    time_wait=0
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(BBG,(0,0))
        
        if time_wait!=time*30:
            time_wait+=1
        else:
            running=False
        
        pygame.display.update()
        clock.tick(30)
#
#
#
#
#
#
#
#
def starting_menu():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if count==1:
            wait(0)
            sfx_rain.play(-1)
            sfx_wind.play(-1)
            sfx_wind.set_volume(0)
            sfx_rain.set_volume(0)
            music_starting_menu.play(-1)
            music_starting_menu.set_volume(0.5)

        sfx_rain.set_volume(count/100)
        sfx_wind.set_volume(count/100)
        MBG.set_alpha(alpha)
        screen.blit(MBG,(0,0))

        alpha = int(255 * (count/100)**2)
        count+=1
        if alpha>=255 and count>=11:
            running = False
        
        count,alpha = 1,0
       
        pygame.display.update()
        clock.tick(30)
#
#
#
#
#
#
#

#Initiation du jeu
def main_menu():

    #starting_menu()
    stage=0
    button_Play_pressed, button_Options_pressed, button_Leave_pressed, running = False,False,False,True
    while running:
        

        img=play_image('test_anim/img_','.png',stage,3)
        stage=img[1]
        play_img  = pygame.image.load(img[0]).convert_alpha()
        play_img = pygame.transform.scale(play_img,Size)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if center_x <= event.pos[0] <= center_x+button_width and button_y_play <= event.pos[1] <= button_y_play+button_height:
                    button_Play_pressed = True
                    play_menu(main_menu)


                if center_x <= event.pos[0] <= center_x+button_width and button_y_option <= event.pos[1] <= button_y_option+button_height:
                    button_Options_pressed = True
                    option_menu(main_menu)
                if center_x <= event.pos[0] <= center_x+button_width and button_y_leave <= event.pos[1] <= button_y_leave+button_height:
                    button_Leave_pressed = True
                    pygame.mixer.music.stop()
                    pygame.quit()
                    exit()

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button_Play_pressed,button_Options_pressed,button_Leave_pressed = False,False,False
        
        screen.blit(MBG,(0,0))
        screen.blit(play_img,(0,0))
        #play
        draw_button(center_x, button_y_play, button_width, button_height, button_color,button_color_pressed, "Jouer", button_text_color, button_Play_pressed)
        #option
        draw_button(center_x, button_y_option, button_width, button_height, button_color,button_color_pressed, "Options", button_text_color, button_Options_pressed)
        #leave
        draw_button(center_x, button_y_leave, button_width, button_height, button_color,button_color_pressed, "Quitter", button_text_color, button_Leave_pressed)
        pygame.display.update()
        clock.tick(120)
#
#
#
#
#
#
#
#
def option_menu(come_from):
    running=True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    come_from
                    running=False
        screen.blit(BBG,(0,0))
        pygame.display.update()
        clock.tick(120)
#           
#
#
#
#
#
#
#
def play_menu(come_from):
    running=True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    come_from
                    running=False
        screen.blit(BBG,(0,0))
        pygame.display.update()
        clock.tick(120)
#           
#
#
#
#
#
#
#
main_menu()
