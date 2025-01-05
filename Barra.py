import pygame


class Barra:
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.active = False
        self.rectangle = pygame.Rect(pos_x, pos_y, 142, 18)

    

    def set_position(self, pos_x, pos_y):
        
        self.rectangle = pygame.Rect(pos_x,pos_y, 142, 18)


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
            text = self.font.render("Acá va a ir el menú del comedor", True, (255, 255, 255))
            screen.blit(text, (50, 50))
            text = self.font.render("Press Enter to exit", True, (255, 255, 255))
            screen.blit(text, (50, 100))
    
