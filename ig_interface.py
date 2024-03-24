import pygame
import pygame_gui
import random

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path, position, description):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)
        self.original_rect = self.rect.copy()  # Sauvegarde de la position originale
        self.selected = False
        self.description = description

    def toggle_selected(self):
        self.selected = not self.selected

class CardDescriptionBar(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.font = pygame.font.SysFont(None, 24)
        self.image = pygame.Surface((800, 70))
        self.image.fill((128, 128, 128))  # Gris
        self.rect = self.image.get_rect(topleft=(position_x, position_y))
        self.description = ""

    def update_description(self, new_description):
        self.description = new_description

    def draw(self, screen):
        pygame.draw.rect(screen, (128, 128, 128), self.rect)  # Remplacer la couleur de fond avec du gris
        text_surface = self.font.render(self.description, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))
        screen.blit(text_surface, text_rect)

def create_button(manager, position, size, text, callback_text):
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(position, size),
        text=text,
        manager=manager
    )

    return button

def reposition_cards(cards):
    # Calcul de la largeur totale occupée par les cartes
    total_width = sum(card.rect.width for card in cards)
    # Calcul de l'espace entre chaque carte
    space_between = 20  # Espacement réduit entre les cartes
    # Position horizontale initiale pour la première carte
    x_position = (1600 - total_width - space_between * (len(cards) - 1)) / 2
    # Recentrage des cartes horizontalement
    for card in cards:
        card.rect.x = x_position
        x_position += card.rect.width + space_between
    # Position verticale pour toutes les cartes
    y_position = 560
    # Recentrage des cartes verticalement
    for card in cards:
        card.rect.y = y_position



def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("The Temple of The Idol")

    manager = pygame_gui.UIManager(screen.get_size())

    clock = pygame.time.Clock()
    is_running = True

    available_cards = [
        {"image_path": "carte.png", "position": (400, 700), "description": "Carte 1"},
        {"image_path": "carte.png", "position": (600, 700), "description": "Carte 2"},
        {"image_path": "carte.png", "position": (800, 700), "description": "Carte 3"},
        {"image_path": "carte.png", "position": (1000, 700), "description": "Carte 4"},
        {"image_path": "carte.png", "position": (1200, 700), "description": "Carte 5"},
        {"image_path": "carte.png", "position": (1400, 700), "description": "Carte 6"},
        {"image_path": "carte.png", "position": (1600, 700), "description": "Carte 7"},
        {"image_path": "carte.png", "position": (1800, 700), "description": "Carte 8"},
        {"image_path": "carte.png", "position": (2000, 700), "description": "Carte 9"},
    ]

    cards_info = random.sample(available_cards, 4)
    cards = [Card(**info) for info in cards_info]
    reposition_cards(cards)

    card_description_bar = CardDescriptionBar(400, 470)

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
                            for other_card in cards:
                                if other_card.selected and other_card != card:
                                    other_card.toggle_selected()
                            card.toggle_selected()
                            if card.selected:
                                card_description_bar.update_description(card.description)
                            else:
                                card_description_bar.update_description("")
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    for button in buttons:
                        if event.ui_element == button:
                            if button.text == "Défausse":
                                for card in cards[:]:
                                    if card.selected:
                                        cards.remove(card)
                                reposition_cards(cards)  # Recentre les cartes après la défausse
                            elif button.text == "Pioche":
                                # Vérifie si moins de 4 cartes sont actuellement présentes avant de piocher
                                if len(cards) < 4:
                                    # Choix aléatoire d'une carte parmi les cartes
                                    if available_cards:
                                        random_card_info = random.choice(available_cards)
                                        new_card = Card(**random_card_info)
                                        cards.append(new_card)
                                        available_cards.remove(random_card_info)  # Retire la carte sélectionnée de la liste des cartes disponibles
                                    reposition_cards(cards)  # Recentre les cartes après la pioche

            manager.process_events(event)

        manager.update(time_delta)
        screen.fill((0, 0, 0))

        for card in cards:
            if card.selected:
                screen.blit(pygame.transform.scale(card.image, (230, 330)), card.rect.topleft)
            else:
                screen.blit(card.image, card.rect.topleft)

        card_description_bar.draw(screen)

        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
