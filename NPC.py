
import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, name, personality):
        super().__init__()
        # Cargar la hoja de sprites
        #self.sprite_sheet = pygame.image.load("src/assets/generic.png").convert_alpha()
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.image = self.sprite_sheet

        #Propiades de los NPC's
        self.name = name
        self.personality = personality
        self.HP = 10
        
        # Dimensiones de los sprites
        self.sprite_width = 32
        self.sprite_height = 32
        self.num_frames = 3


    # Función que obtiene los frames de la hoja de sprites
    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), ((frame * width),0, width, height))
        #image = pygame.transform.scale(image,(width * 2 , height * 2))
        image.set_colorkey((0,0,0))

        return image