import pygame 
from random import randint
from sys import exit

#initiation du module Pygame
pygame.init()
#definition de la taille du jeux
display_x,display_y = 640,640
screen = pygame.display.set_mode((display_x,display_y))
#titre afficher en haut de la page
pygame.display.set_caption('Mein Gott')
#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()

BG = pygame.image.load('Background.png').convert()
BG = pygame.transform.scale(BG,(800,600))

#texture du Player
# player_surface = pygame.image.load('Skin-R.png').convert_alpha()
# player_surface = pygame.transform.scale(player_surface,(100,100))



#position x et y du Player
pl_x_pos = 400
pl_y_pos = 400



#Initiation du jeu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        screen.blit(BG,(0,0))
        # screen.blit(ground_surface,(0,450))
        # screen.blit(player_surface,(pl_x_pos,pl_y_pos))
        

        pygame.display.update()
        clock.tick(120)

main_menu()