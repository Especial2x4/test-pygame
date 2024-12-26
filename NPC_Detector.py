
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

        
    


    def show_npc_list(self):
        print(self.npc_list)
        for npc_name in self.npc_list:
            print(npc_name.name)


    def npc_new_random(self, new_random):
        self.random_flag = new_random


    
    def shooter(self):
        #print(self.random_flag)
        for npc in self.npc_list:
            if npc.shooter_num == self.random_flag:
                print(f"{npc.name} dice : WAIT!")
                self.npc_activo = npc
                # Dibujar el cuadro de diálogo encima del NPC
                #wait_box_frame = self.get_image(0, 32, 32)
                #self.screen.blit(self.wait_box, (380,90))
                
                return True

    def show_wait_box(self):
        self.screen.blit(self.wait_box, (380,90))
        #time.sleep(5)


    def get_npc_activate(self):
        return self.npc_activo