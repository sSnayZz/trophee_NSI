import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((1600, 900))

background = pygame.Surface((1600, 900))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((1600, 900))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1390, 590), (200, 300)),
                                            text='Déffause',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
