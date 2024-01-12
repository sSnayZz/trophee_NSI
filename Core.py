import pygame 
from sys import exit

#initiation du module Pygame
pygame.init()
#definition de la taille du jeux
display_x,display_y = 1920/2,1080/2
screen = pygame.display.set_mode((display_x,display_y))
#titre afficher en haut de la page
pygame.display.set_caption('Mein Gott')
#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()

BG = pygame.image.load('Background.png').convert()
BG = pygame.transform.scale(BG,(display_x,display_y))

#texture du Player
# player_surface = pygame.image.load('Skin-R.png').convert_alpha()
# player_surface = pygame.transform.scale(player_surface,(display_x,display_y))

def draw_button(x, y, width, height, color, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, text_rect)
    
font = pygame.font.Font(None, 36)


#Initiation du jeu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Vérifier si le clic de la souris est sur le bouton "Jouer"
                if 150 <= event.pos[0] <= 250 and 100 <= event.pos[1] <= 150:
                    print("Le bouton 'Jouer' a été cliqué!")



        screen.blit(BG,(0,0))
        pygame.display.update()
        clock.tick(120)

main_menu()