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
button_width,button_height=200,50
center_x,center_y = (Size[0] - button_width) // 2,(Size[1] - button_height) // 2
button_y_play,button_y_option,button_y_leave=center_y//2,center_y,center_y+center_y//2

#titre afficher en haut de la page
pygame.display.set_caption('The Temple Of The Idol')

#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()

MBG = pygame.image.load('Background.png').convert()
MBG = pygame.transform.scale(MBG,Size)

BBG = pygame.image.load('black_background.png').convert()
BBG = pygame.transform.scale(BBG,Size)
#texture du Player
# player_surface = pygame.image.load('Skin-R.png').convert_alpha()
# player_surface = pygame.transform.scale(player_surface,(display_x,display_y))

font = pygame.font.Font(None, 36)
button_color=(255,255,255)  
button_color_pressed=(200,200,200) 
button_text_color=(0,0,0)

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
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, text_rect)
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
    count,alpha = 1,0
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if count==1:
            wait(1)
            music_starting_menu.play(-1)
            sfx_rain.play(-1)
            sfx_wind.play(-1)
            sfx_wind.set_volume(1)
            sfx_rain.set_volume(1)
            music_starting_menu.set_volume(0.5)
        MBG.set_alpha(alpha)
        screen.blit(MBG,(0,0))
        alpha = int(255 * (count/100)**2)
        count+=1
        if alpha >= 255 and count>=11:
            running = Falsen
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

    starting_menu()
    
    button_Play_pressed,button_Options_pressed,button_Leave_pressed , running = False,False,False,True
    while running:
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #Vérifier si le clic de la souris est sur le bouton "Jouer"
                if center_x <= event.pos[0] <= center_x+button_width and button_y_play <= event.pos[1] <= button_y_play+button_height:
                    button_Play_pressed = True
                    print("Le bouton 'Jouer' a été cliqué! passer a scene suivante")
                if center_x <= event.pos[0] <= center_x+button_width and button_y_option <= event.pos[1] <= button_y_option+button_height:
                    button_Options_pressed = True
                    print("Le bouton 'truc' a été cliqué! passer a scene suivante")
                if center_x <= event.pos[0] <= center_x+button_width and button_y_leave <= event.pos[1] <= button_y_leave+button_height:
                    button_Leave_pressed = True
                    pygame.mixer.music.stop()
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button_Play_pressed,button_Options_pressed,button_Leave_pressed = False,False,False
        
        
        screen.blit(MBG,(0,0))
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
main_menu()