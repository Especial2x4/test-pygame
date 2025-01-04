
import pygame

class Compuerta():
    def __init__(self, pos_x, pos_y):

        self.rectangle = pygame.Rect(pos_x, pos_y, 62, 24)
        self.active = False

    

    def set_position(self, pos_x, pos_y):
        
        self.rectangle = pygame.Rect(pos_x,pos_y, 62, 24)

        