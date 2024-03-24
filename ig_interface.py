import pygame
import pygame_gui

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)
        self.selected = False

    def toggle_selected(self):
        self.selected = not self.selected

class CardDescriptionBar(pygame.sprite.Sprite):
    def __init__(self, description, position):
        super().__init__()
        self.font = pygame.font.SysFont(None, 24)
        self.image = pygame.Surface((400, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(midtop=position)
        self.description = description

    def update_description(self, new_description):
        self.description = new_description

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        text_surface = self.font.render(self.description, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

def create_button(manager, position, size, text, callback_text):
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(position, size),
        text=text,
        manager=manager
    )

    return button

def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))  # Taille de l'écran
    pygame.display.set_caption("Tomb of The Idol")

    manager = pygame_gui.UIManager(screen.get_size())

    clock = pygame.time.Clock()
    is_running = True

    # Cartes
    cards = []
    card_positions = [(400, 700), (600, 700), (800, 700), (1000, 700)]
    for i in range(4):
        card = Card('carte.png', card_positions[i])
        cards.append(card)

    # Barre de description
    card_description_bar = CardDescriptionBar('', (800, 600))

    buttons_info = [
        {"position": (1360, 560), "size": (200, 300), "text": "Défausse", "callback_text": "Défausse"},
        {"position": (60, 560), "size": (200, 300), "text": "Pioche", "callback_text": "Pioche"},
    ]

    buttons = []
    for button_info in buttons_info:
        button = create_button(manager, button_info["position"], button_info["size"], button_info["text"], button_info["callback_text"])
        buttons.append(button)

    while is_running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    for card in cards:
                        if card.rect.collidepoint(event.pos):
                            card.toggle_selected()
                            if card.selected:
                                card_description_bar.update_description("Description de la carte sélectionnée")
                            else:
                                card_description_bar.update_description("")
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    for button in buttons:
                        if event.ui_element == button:
                            print(button.text)  # Afficher le texte du bouton cliqué

            manager.process_events(event)

        manager.update(time_delta)
        screen.fill((0, 0, 0))

        # Affichage des cartes
        for card in cards:
            if card.selected:
                screen.blit(pygame.transform.scale(card.image, (200, 300)), card.rect.topleft)
            else:
                screen.blit(card.image, card.rect.topleft)

        # Affichage de la barre de description
        card_description_bar.draw(screen)

        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
