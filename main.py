import pygame
import pytmx
import sys

from Player import *

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Nivel con Tiled y Colisiones")

# Cargar el archivo TMX
tmx_data = pytmx.load_pygame('src/nivel1/mapa1.tmx')

# Función para dibujar el mapa
def draw_map(screen, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

# Función para obtener los objetos de colisión
def get_collision_objects(tmx_data):
    collision_objects = []
    for obj in tmx_data.objects:
        if obj.name == "colision-pared":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
    return collision_objects

# Obtener los objetos de colisión
collision_objects = get_collision_objects(tmx_data)

# Crear el jugador
player = Player(100, 100)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT]:
        dx = -player.speed
    if keys[pygame.K_RIGHT]:
        dx = player.speed
    if keys[pygame.K_UP]:
        dy = -player.speed
    if keys[pygame.K_DOWN]:
        dy = player.speed

    # Mover al jugador
    player.move(dx, dy, collision_objects)

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el mapa
    draw_map(screen, tmx_data)

    # Dibujar el jugador
    player.draw(screen)

    # Dibujar los objetos de colisión (opcional, para depuración)
    #for rect in collision_objects:
        #pygame.draw.rect(screen, (255, 0, 0), rect, 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de cuadros por segundo
    pygame.time.Clock().tick(60)

# Salir del programa
pygame.quit()
sys.exit()

