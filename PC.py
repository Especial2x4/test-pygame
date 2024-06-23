import pygame

class PC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.active = False

    def open(self):
        self.active = True

    def close(self):
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.close()

    def draw(self, screen):
        if self.active:
            screen.fill((0, 0, 0))
            text = self.font.render("Welcome to the PC!", True, (255, 255, 255))
            screen.blit(text, (50, 50))
            text = self.font.render("Press Enter to exit", True, (255, 255, 255))
            screen.blit(text, (50, 100))
