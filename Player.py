# player.py

import pygame
import math

# Función para cargar los fotogramas desde la hoja de sprites
def load_frames(sheet, frame_width, frame_height, num_frames, row):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface((i * frame_width, row * frame_height, frame_width, frame_height))
        frames.append(frame)
    return frames

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, screen_width, screen_height):
        super().__init__()
        # Cargar la hoja de sprites
        sprite_sheet = pygame.image.load("src/assets/player.png").convert_alpha()
        
        # Dimensiones de los sprites
        self.sprite_width = 32
        self.sprite_height = 32
        self.num_frames = 3
        
        # Cargar las animaciones de caminar
        self.walk_down = load_frames(sprite_sheet, self.sprite_width, self.sprite_height, self.num_frames, 0)
        self.walk_up = load_frames(sprite_sheet, self.sprite_width, self.sprite_height, self.num_frames, 1)
        self.walk_left = load_frames(sprite_sheet, self.sprite_width, self.sprite_height, self.num_frames, 2)
        self.walk_right = load_frames(sprite_sheet, self.sprite_width, self.sprite_height, self.num_frames, 3)
        
        # Estado inicial del jugador
        self.image = self.walk_down[0]
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.current_frame = 0
        self.animation_speed = 0.5   # controla la velocidad de frames
        self.desplazamiento_speed = 3 # controla la velocidad de desplazamiento
        self.last_update = pygame.time.get_ticks()
        self.walking = False
        self.direction = 'down'
        
    def update(self):
        keys = pygame.key.get_pressed()
        self.walking = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.desplazamiento_speed
            self.walking = True
            self.direction = 'left'
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.desplazamiento_speed
            self.walking = True
            self.direction = 'right'
        if keys[pygame.K_UP]:
            self.rect.y -= self.desplazamiento_speed
            self.walking = True
            self.direction = 'up'
        if keys[pygame.K_DOWN]:
            self.rect.y += self.desplazamiento_speed
            self.walking = True
            self.direction = 'down'

        # Animar el personaje
        if self.walking:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.animation_speed * 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % self.num_frames
                
                if self.direction == 'down':
                    self.image = self.walk_down[self.current_frame]
                    print(self.current_frame)
                if self.direction == 'up':
                    self.image = self.walk_up[self.current_frame]
                    print(self.current_frame)
                if self.direction == 'left':
                    self.image = self.walk_left[self.current_frame]
                    print(self.current_frame)
                if self.direction == 'right':
                    self.image = self.walk_right[self.current_frame]
                    print(self.current_frame)

        # Si no está caminando el frame será el de reposo

        if not self.walking:
            if self.direction == 'down':
                    self.image = self.walk_down[0]
                    #print(self.current_frame)
            if self.direction == 'up':
                    self.image = self.walk_up[0]
                    #print(self.current_frame)
            if self.direction == 'left':
                    self.image = self.walk_left[0]
                    #print(self.current_frame)
            if self.direction == 'right':
                    self.image = self.walk_right[1]
                    #print(self.current_frame)

              

        # Limitar el movimiento del jugador dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600


    
    def move(self, dx, dy, collision_objects):
        # Guardar la posición original
        original_rect = self.rect.copy()

        # setear distancia de rebote
        distancia_rebote = 10

        # Intentar mover al jugador
        #self.rect.x += dx
        for obj in collision_objects:
            if self.rect.colliderect(obj) and self.direction == "left":
                self.rect.x = original_rect.x + distancia_rebote # Revertir movimiento horizontal izquierda
                #self.rect.left = 0
                print(obj)
                print(original_rect.x)
                break
            if self.rect.colliderect(obj) and self.direction == "right":
                self.rect.x = original_rect.x - distancia_rebote # Revertir movimiento horizontal derecha
                #self.rect.left = 0
                print(obj)
                print(original_rect.x)
                break
            if self.rect.colliderect(obj) and self.direction == "up":
                self.rect.y = original_rect.y + distancia_rebote # Revertir movimiento vertical arriba
                #self.rect.left = 0
                print(obj)
                print(original_rect.y)
                break
            if self.rect.colliderect(obj) and self.direction == "down":
                self.rect.y = original_rect.y - distancia_rebote # Revertir movimiento vertical arriba
                #self.rect.left = 0
                print(obj)
                print(original_rect.y)
                break
        """
        self.rect.y += dy
        for obj in collision_objects:
            if self.rect.colliderect(obj):
                self.rect.y = original_rect.y - 10  # Revertir movimiento vertical
                print(obj)
                break
        """  

    def set_position(self, x, y):

        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))         