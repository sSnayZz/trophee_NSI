import pygame 
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle

pygame.init()

Size = (1920/2,1080/2)
screen = pygame.display.set_mode(Size)
MBG = pygame.image.load('Background_Main_Menu.jpg').convert()
MBG = pygame.transform.scale(MBG,Size)

#x y tx ty
toggle_music = Toggle(screen, 475, 400, 100, 40)
output_music = TextBox(screen, 750, 100, 40, 40, fontSize=20)
slider_music = Slider(screen, 100, 100, 600, 40, min=0, max=100, step=1)

toggle_sfx = Toggle(screen, 475, 450, 100, 40)
slider_sfx = Slider(screen, 100, 200, 800, 40, min=0, max=100, step=1)
output_sfx = TextBox(screen, 475, 250, 50, 50, fontSize=30)

output_music.disable()  # Act as label instead of textbox
output_sfx.disable()  # Act as label instead of textbox



run,state_music,state_sfx=True,True,True

while run:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			run = False
			quit()

	screen.fill((255, 255, 255))
	
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
		
		
	print(sfx_volume)
	print(music_volume)
	screen.blit(MBG,(0,0))

	pygame_widgets.update(events)
	pygame.display.update()

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

