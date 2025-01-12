
import math
import sys
import pygame


class Combate():

    def __init__(self, screen):
        self.screen = screen


    


    # Lanza la trasición previa al sistema de combate
    def spiral_pixel_transition(self, tile_size=20, speed=5, sound=None):
        """Realiza una transición en espiral pixelada con efecto de sonido."""
        #pygame.init()
        # Dividir la pantalla en una cuadrícula de tiles
        # Usa el tamaño de la pantalla desde self.screen
        height = self.screen.get_height()
        width = self.screen.get_width()
        rows = math.ceil(height / tile_size)
        cols = math.ceil(width / tile_size)

        # Crear una lista con las posiciones de todos los tiles
        tiles = [(x * tile_size, y * tile_size) for y in range(rows) for x in range(cols)]

        # Ordenar los tiles en forma de espiral
        center_x, center_y = width // 2, height // 2
        tiles.sort(key=lambda pos: math.atan2(pos[1] - center_y, pos[0] - center_x))

        clock = pygame.time.Clock()
        revealed_tiles = 0
        total_tiles = len(tiles)

        # Reproducir sonido si se proporciona
        if sound:
            sound.play(-1)  # Reproducir en loop

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fondo negro para cubrir la pantalla
            #self.screen.fill((0, 0, 0))

            # Dibujar los tiles revelados en cada frame
            for i in range(revealed_tiles):
                x, y = tiles[i]
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, tile_size, tile_size))

            pygame.display.flip()
            clock.tick(120)  # Aumentar la tasa de cuadros para mayor fluidez

            # Incrementar la cantidad de tiles revelados
            revealed_tiles += speed
            if revealed_tiles >= total_tiles:
                running = False

        # Detener el sonido al finalizar la transición
        if sound:
            sound.stop()