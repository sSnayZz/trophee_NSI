import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Stupid Choices aaaaaaaaaaa')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Sky.png').convert()
sky_surface = pygame.transform.scale(sky_surface,(800,600))

ground_surface = pygame.image.load('Ground.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface,(800,600))

player_surface = pygame.image.load('Player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface,(160,120))
player_rect = player_surface.get_rect(midbottom = (80,300))

pl_x_pos = 400
pl_y_pos = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        pl_x_pos+=3
        
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        pl_x_pos-=3

    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        if pl_y_pos<=410:
            pl_y_pos=410
        else:
            pl_y_pos-=2

    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        if pl_y_pos>=500:
            pl_y_pos=500
        else:
            pl_y_pos+=2

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,100))
    screen.blit(player_surface,(pl_x_pos,pl_y_pos))
    

    pygame.display.update()
    clock.tick(120)