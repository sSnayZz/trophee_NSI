import pygame 
from random import randint
from sys import exit

#initiation du module Pygame
pygame.init()
#definition de la taille du jeux
display_x,display_y = 192,108
screen = pygame.display.set_mode((display_x,display_y))
#titre afficher en haut de la page
pygame.display.set_caption('Mein Gott')
#utile pour éviter que la fenetre ne se ferme ///PAS TOUCHEE
clock = pygame.time.Clock()



#textures des fonds différents jour/nuit que l'on appelle puis recadre/transforme
Menu_surface = pygame.image.load('menu.png').convert()
Menu_surface = pygame.transform.scale(Menu_surface,(192,108))


#texture du Player
#player_surface = pygame.image.load('Skin-R.png').convert_alpha()
#player_surface = pygame.transform.scale(player_surface,(100,100))



#position x et y du Player
pl_x_pos = 400
pl_y_pos = 400



#Initiation du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(Menu_surface,(0,0))
    #screen.blit(player_surface,(pl_x_pos,pl_y_pos))
    

    pygame.display.update()
    clock.tick(120)