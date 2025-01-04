
import pygame
import time


class NPC_Detector(pygame.sprite.Sprite):

    def __init__(self, npc_list, random_flag, sprite_sheet_path, screen):
        super().__init__()
        
        self.npc_list = npc_list
        self.random_flag = random_flag
        self.screen = screen
        # Carga la hoja de sprite
        self.wait_box = pygame.image.load(sprite_sheet_path).convert_alpha()
        # NPC activado
        self.npc_activo = None

        
    

    # Función util para depuración
    def show_npc_list(self):
        print(self.npc_list)
        for npc_name in self.npc_list:
            print(npc_name.name)


    # Setea un nuevo número random necesario para la función shooter
    def set_npc_new_random(self, new_random):
        self.random_flag = new_random


    
    # Función principal del NPC_Detector que devuelve True para dar disparo al evento de cola
    def shooter(self):
        
        for npc in self.npc_list:
            if npc.shooter_num == self.random_flag:
                print(f"{npc.name} dice : WAIT!")
                self.npc_activo = npc

                
                return True


    # Muestra el mensaje de WAIT! sobre el NPC activado (trabajar más adelante en esta función)
    def show_wait_box(self):
        self.screen.blit(self.wait_box, (380,90))
        

    # Devuelve el NPC activado para poder trabajar con sus propiedades
    def get_npc_activate(self):
        return self.npc_activo