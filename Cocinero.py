import pygame

class Cocinero(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, path_portrait):
        super().__init__()

        # Cargar la hoja de sprites
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.image = self.sprite_sheet
        self.portrait = pygame.image.load(path_portrait)
        self.portrait = pygame.transform.scale(self.portrait, (350, 350))  # Escala la imagen a 350x350

        self.name = "Jorgelio"



    # Función que obtiene los frames de la hoja de sprites
    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), ((frame * width),0, width, height))
        image.set_colorkey((0,0,0))

        return image
