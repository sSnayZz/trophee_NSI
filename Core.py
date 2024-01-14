import pygame 
from sys import exit

#initiation du module Pygame
pygame.init()
#definition de la taille du jeux
Size = (1920/2,1080/2)
screen = pygame.display.set_mode(Size)
button_width,button_height=100,50
center_x,center_y = (Size[0] - button_width) // 2,(Size[1] - button_height) // 2
button_y_play,button_y_option,button_y_leave=center_y//2,center_y,center_y*2

#titre afficher en haut de la page
pygame.display.set_caption('Mein Gott')

#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()




BG = pygame.image.load('Background.png').convert()
BG = pygame.transform.scale(BG,Size)

#texture du Player
# player_surface = pygame.image.load('Skin-R.png').convert_alpha()
# player_surface = pygame.transform.scale(player_surface,(display_x,display_y))

font = pygame.font.Font(None, 36)

# Fonction pour créer un bouton
def draw_button(x, y, width, height, color, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, text_rect)
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)    

#Initiation du jeu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #Vérifier si le clic de la souris est sur le bouton "Jouer"
                if center_x <= event.pos[0] <= center_x+button_width and 100 <= event.pos[1] <= 150:
                    print("Le bouton 'Jouer' a été cliqué! passer a scene suivante")
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #Vérifier si le clic de la souris est sur le bouton "Jouer"
                if center_x <= event.pos[0] <= center_x+button_width and 100 <= event.pos[1] <= 150:
                    print("Le bouton 'Jouer' a été cliqué! passer a scene suivante")
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #Vérifier si le clic de la souris est sur le bouton "Jouer"
                if center_x <= event.pos[0] <= center_x+button_width and 100 <= event.pos[1] <= 150:
                    print("Le bouton 'Jouer' a été cliqué! passer a scene suivante")
        
        screen.blit(BG,(0,0))
        draw_button(center_x, button_y_play, button_width, button_height, GREEN, "Jouer", BLACK)
        draw_button(center_x, button_y_option, button_width, button_height, GREEN, "option", BLACK)
        draw_button(center_x, button_y_leave, button_width, button_height, GREEN, "quitter", BLACK)
        pygame.display.update()
        clock.tick(120)

main_menu()