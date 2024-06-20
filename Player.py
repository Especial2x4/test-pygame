import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 255))  # Color azul para el jugador
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, dx, dy, collision_objects):
        # Guardar la posición original
        original_rect = self.rect.copy()

        # Intentar mover al jugador
        self.rect.x += dx
        for obj in collision_objects:
            if self.rect.colliderect(obj):
                self.rect.x = original_rect.x  # Revertir movimiento horizontal
                break

        self.rect.y += dy
        for obj in collision_objects:
            if self.rect.colliderect(obj):
                self.rect.y = original_rect.y  # Revertir movimiento vertical
                break

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
