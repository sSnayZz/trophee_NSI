import pygame 
from sys import exit

#initiation du module Pygame
pygame.init()
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


#expo x^3

BG = pygame.image.load('Background.png').convert()
BG = pygame.transform.scale(BG,Size)

#texture du Player
# player_surface = pygame.image.load('Skin-R.png').convert_alpha()
# player_surface = pygame.transform.scale(player_surface,(display_x,display_y))

font = pygame.font.Font(None, 36)

# Fonction pour créer un bouton
def draw_button(x, y, width, height, color, pressed_color, text, text_color,is_pressed):
    current_color = pressed_color if is_pressed else color
    pygame.draw.rect(screen, current_color, (x, y, width, height))
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, text_rect)

button_color=(255,255,255)  
button_color_pressed=(200,200,200) 
button_text_color=(0,0,0)
running=True


#Initiation du jeu
def main_menu():
    button_pressed = False
    while True:
        pygame.draw.rect(screen, (0,0,0,255), ((0,0)), Size)

        if Run==0:
            break
    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #Vérifier si le clic de la souris est sur le bouton "Jouer"
                if center_x <= event.pos[0] <= center_x+button_width and button_y_play <= event.pos[1] <= button_y_play+button_height:
                    button_pressed = True
                    print("Le bouton 'Jouer' a été cliqué! passer a scene suivante")
                if center_x <= event.pos[0] <= center_x+button_width and button_y_option <= event.pos[1] <= button_y_option+button_height:
                    button_pressed = True
                    print("Le bouton 'truc' a été cliqué! passer a scene suivante")
                if center_x <= event.pos[0] <= center_x+button_width and button_y_leave <= event.pos[1] <= button_y_leave+button_height:
                    button_pressed = True
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button_pressed = False

        screen.blit(BG,(0,0))
        #play
        draw_button(center_x, button_y_play, button_width, button_height, button_color,button_color_pressed, "Jouer", button_text_color, button_pressed)
        
        #option
        draw_button(center_x, button_y_option, button_width, button_height, button_color,button_color_pressed, "option", button_text_color, button_pressed)
        
        #leave
        draw_button(center_x, button_y_leave, button_width, button_height, button_color,button_color_pressed, "quitter", button_text_color, button_pressed)
        pygame.display.update()
        clock.tick(120)

main_menu()