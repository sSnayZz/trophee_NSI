import pygame 
from sys import exit

#initiation du module Pygame
pygame.init()
#definition de la taille du jeux
screen = pygame.display.set_mode((800,600))
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
ground_surface = pygame.transform.scale(ground_surface,(800,600))

#texture du Player
player_surface = pygame.image.load('Player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface,(160,120))

#position x et y du Player
pl_x_pos = 400
pl_y_pos = 400

#Initiation du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    #controles des mouvements x y du Player
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        pl_x_pos+=2
        
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        pl_x_pos-=2

    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        if pl_y_pos<=410:
            pl_y_pos=410
        else:
            pl_y_pos-=1

    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        if pl_y_pos>=500:
            pl_y_pos=500
        else:
            pl_y_pos+=1

    screen.blit(skyday_surface,(0,0))
    screen.blit(ground_surface,(0,100))
    screen.blit(player_surface,(pl_x_pos,pl_y_pos))
    

    pygame.display.update()
    clock.tick(120)