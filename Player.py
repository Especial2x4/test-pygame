import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 255))  # Color azul para el jugador
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 5

    def move(self, dx, dy, collision_objects):
        # Guardar la posición original
        original_rect = self.rect.copy()

        # Intentar mover al jugador
        self.rect.x += dx
        for obj in collision_objects:
            if self.rect.colliderect(obj):
                self.rect.x = original_rect.x  # Revertir movimiento horizontal
                #print(obj)
                break

        self.rect.y += dy
        for obj in collision_objects:
            if self.rect.colliderect(obj):
                self.rect.y = original_rect.y  # Revertir movimiento vertical
                break

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


    def set_position(self, x, y):

        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
