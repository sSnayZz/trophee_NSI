import pygame
import pygame_gui

def create_button(manager, position, size, text, image_path, callback_text):
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(position, size),
        text=text,
        manager=manager
    )
    
    if image_path:  # Si un chemin d'image est fourni, chargez l'image
        normal_image = pygame.image.load(image_path)
        button.set_image(normal_image)

    return button

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))  # Taille de l'écran
    pygame.display.set_caption("Tomb of The Idol")

    manager = pygame_gui.UIManager(screen.get_size())

    clock = pygame.time.Clock()
    is_running = True

    buttons_info = [
        {"position": (1340, 540), "size": (250, 350), "text": "", "image_path": "defausse_button_image.png", "callback_text": "Déffause"},
        {"position": (10, 540), "size": (250, 350), "text": "", "image_path": "pioche_button_image.png", "callback_text": "Pioche"}
    ]

    buttons = []
    for button_info in buttons_info:
        button = create_button(manager, button_info["position"], button_info["size"], button_info["text"], button_info["image_path"], button_info["callback_text"])
        buttons.append(button)

    while is_running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    for button in buttons:
                        if event.ui_element == button:
                            print(button.text)  # Afficher le texte du bouton cliqué

            manager.process_events(event)

        manager.update(time_delta)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
