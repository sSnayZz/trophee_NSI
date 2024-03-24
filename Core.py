import pygame 
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle
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

MBGF = pygame.image.load('Background_Main_Menu_Flou.jpg').convert()
MBGF = pygame.transform.scale(MBGF,Size)

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


button_BG = pygame.image.load('Background_Button.jpg').convert()
button_BG = pygame.transform.scale(button_BG,(button_width,button_height))



#x y tx ty
toggle_music = Toggle(screen, 750, 110, 30, 20)
output_music = TextBox(screen, 800, 100, 40, 40, fontSize=20)
slider_music = Slider(screen, 100, 110, 600, 20, min=0, max=10, step=1)

toggle_sfx = Toggle(screen, 750, 210, 30, 20)
output_sfx = TextBox(screen,800, 200, 40, 40, fontSize=20)
slider_sfx = Slider(screen,  100, 210, 600, 20, min=0, max=10, step=1)

output_music.disable()  # Act as label instead of textbox
output_sfx.disable()  # Act as label instead of textbox


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
    ajout=''
    if stage>=exceed+1:
        stage=0

    stage+=1
    if stage<=9:
        ajout='000'
    elif stage<=99:
        ajout='00'
    elif stage<=999:
        ajout='0'
    
    
    return [chemin+str(ajout)+str(stage)+type_fichier,stage]
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
def alpha_intro(intro_count):
    if intro_count!=None and intro_count>=0 :
        return intro_count-1
    else:
        return 0
#
#
#
#
#
#
#

sfx_rain.play(-1)
sfx_wind.play(-1)
sfx_wind.set_volume(0)
sfx_rain.set_volume(0)
music_starting_menu.play(-1)
music_starting_menu.set_volume(0.5)
#Initiation du jeu
def main_menu():

    
    stage,intro_count=0,255
    button_Play_pressed, button_Options_pressed, button_Leave_pressed, running = False,False,False,True
    while running:
        

        img=play_image('Animation_Sand/','.png',stage,360)
        stage=img[1]
        play_img  = pygame.image.load(img[0]).convert_alpha()
        play_img.set_alpha(100)
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
        
        screen.blit(BBG,(0,0))
        BBG.set_alpha(alpha_intro(intro_count))
        intro_count=alpha_intro(intro_count)
        
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
    
    stage=0
    run,state_music,state_sfx=True,True,True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    come_from
                    running=False

        img=play_image('Animation_Sand/','.png',stage,360)
        stage=img[1]
        play_img  = pygame.image.load(img[0]).convert_alpha()
        play_img.set_alpha(100)
        play_img = pygame.transform.scale(play_img,Size)
        
        output_music.setText(slider_music.getValue())
        output_sfx.setText(slider_sfx.getValue())
        
        state_music = toggle_music.getValue() 
        state_sfx = toggle_sfx.getValue() 

        if state_music==True:
            music_volume=0
        else:
            music_volume=slider_music.getValue()
        
        
        if state_sfx==True:
            sfx_volume=0
        else:
            sfx_volume=slider_sfx.getValue()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    come_from
                    running=False
        
        sfx_wind.set_volume(sfx_volume/10)
        sfx_rain.set_volume(sfx_volume/10)
        music_starting_menu.set_volume(music_volume/10)

        screen.blit(MBG,(0,0))
        events = pygame.event.get()
        screen.blit(MBGF,(0,0))
        screen.blit(play_img,(0,0))

        clock.tick(120)

        pygame_widgets.update(events)
        pygame.display.update()

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
                    option_menu(play_menu)
        screen.blit(BGB,(0,0))
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
