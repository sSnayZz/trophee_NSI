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



#textures des fonds différents jour/nuit que l'on appelle puis recadre/transforme
skyday_surface = pygame.image.load('Paysage-jour.png').convert()
skyday_surface = pygame.transform.scale(skyday_surface,(800,600))
skynight_surface = pygame.image.load('Paysage-nuit.png').convert()
skynight_surface = pygame.transform.scale(skynight_surface,(800,600))

#texture du 'sol' pour le Player
ground_surface = pygame.image.load('Sol-jour.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface,(2000,200))

#texture du Player
player_surface = pygame.image.load('Skin-R.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface,(100,100))



#position x et y du Player
pl_x_pos = 400
pl_y_pos = 400



#Initiation du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(skyday_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    screen.blit(player_surface,(pl_x_pos,pl_y_pos))
    

    pygame.display.update()
    clock.tick(120)