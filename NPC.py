
import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, path_portrait, name, personality, tupla_rect, shooter_num):
        super().__init__()
        # Cargar la hoja de sprites
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.image = self.sprite_sheet
        top, left, width, height = tupla_rect # Desenpaquetando la tupla
        self.rectangle = pygame.Rect(tupla_rect)
        self.portrait = pygame.image.load(path_portrait)
        self.portrait = pygame.transform.scale(self.portrait, (350, 350))  # Escala la imagen a 350x350

        #Propiades de los NPC's
        self.name = name
        self.personality = personality
        self.max_hp = 10
        self.current_hp = 10
        self.HP = 10
        self.shooter_num = shooter_num
        
        # Dimensiones de los sprites
        self.sprite_width = 32
        self.sprite_height = 32
        self.num_frames = 3

    # Función para quitar HP a NPC
    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)

    # Función que obtiene los frames de la hoja de sprites
    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), ((frame * width),0, width, height))
        image.set_colorkey((0,0,0))

        return image