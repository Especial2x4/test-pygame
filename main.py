
import pygame
import pytmx
import sys
import random

from Player import *
from PC import *
from Compuerta import *
from NPC import *
from NPC_Detector import *

from config import *

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Soportanto-IT")

# Interruptor de nivel
#tag_level = ["sistemas" , "sala" , "toilette", "comedor" , "exterior"]
tag_level = "sistemas"

# Definir eventos personalizados
SHOW_WAIT_BOX_EVENT = pygame.USEREVENT + 1


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
        if obj.name == "colision-computer-player":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("he colisionado con computer player")
        if obj.name == "colision-sala":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-computer-server":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-server":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-computer":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-printer":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-ap":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-mostrador":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-heladera":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-mesa":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
        if obj.name == "colision-toilete":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            #print("voy a ir a la sala")
            

    return collision_objects

# Obtener los objetos de colisión
collision_objects = get_collision_objects(tmx_data)

# Ruta de la hoja de sprites
sprite_sheet_path = 'assets/sprite_sheet.png'
# Ventas
sprite_sheet_zafiro = "src/assets/zafiro.png" # Hoja de sprite que corresponde a la sra zafiro
sprite_sheet_mel = "src/assets/mel.png" # Hoja de sprite que corresponde a mel
sprite_sheet_john = "src/assets/generic.png" # Hoja de sprite que corresponde a john
sprite_sheet_mariana = "src/assets/generic.png" # Hoja de sprite que corresponde a mariana
sprite_sheet_nerea = "src/assets/generic.png" # Hoja de sprite que corresponde a nerea
sprite_sheet_marcelo = "src/assets/generic.png" # Hoja de sprite que corresponde a marcelo
sprite_sheet_nico = "src/assets/generic.png" # Hoja de sprite que corresponde a nico
sprite_sheet_rothwailer = "src/assets/generic.png" # Hoja de sprite que corresponde a sra rothwailer
# Producto ExtraTerrestre
sprite_sheet_florencia1 = "src/assets/generic.png" # Hoja de sprite que corresponde a florencia uno
sprite_sheet_florencia2 = "src/assets/generic.png" # Hoja de sprite que corresponde a florencia dos
sprite_sheet_florencia3 = "src/assets/generic.png" # Hoja de sprite que corresponde a florencia tres
sprite_sheet_daniel = "src/assets/generic.png" # Hoja de sprite que corresponde a daniel
sprite_sheet_chuck = "src/assets/generic.png" # Hoja de sprite que corresponde a chuck
sprite_sheet_jennifer = "src/assets/generic.png" # Hoja de sprite que corresponde a jennifer
sprite_sheet_emilio = "src/assets/generic.png" # Hoja de sprite que corresponde a emilio
sprite_sheet_camorre = "src/assets/generic.png" # Hoja de sprite que corresponde a camorre

# Ruta del alert box
sprite_sheet_wait = "src/assets/wait-box.png"
wait_box = pygame.image.load(sprite_sheet_wait).convert_alpha()


# Crear el jugador y PC
#player = Player(100, 90)
# Crear el jugador
player = Player(sprite_sheet_path, SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites = pygame.sprite.Group(player)
pc = PC()

# === INSTANCIAS DE NPC ==== #

NPC_LISTAO = [
     
     NPC(sprite_sheet_zafiro, "Sra Zafiro", personality=NPC_PERSONALITY_DICT['hostil'], tupla_rect=((162, 110, 44, 49)), shooter_num=10),
     NPC(sprite_sheet_mel, "Mel", personality=NPC_PERSONALITY_DICT['accesible'], tupla_rect=((272, 112, 47, 48)), shooter_num=20)
     
]

# Instancia señora Zafiro
npc1_zafiro = NPC_LISTAO[0]
frame_zafiro = npc1_zafiro.get_image(0, 32, 32) # recorta el frame que se necesita

# Instancia Mel
npc2_mel = NPC_LISTAO[1]
frame_mel = npc2_mel.get_image(0, 32, 32) # recorta el frame que se necesita

# Instancia del NPC-detector
random_flag = 0
npc_detector = NPC_Detector(NPC_LISTAO, random_flag, sprite_sheet_wait, screen) #-> pone el cartelito de wait sobre el NPC activado, retorna dicho NPC y se pasa a la distancia para un duelo


# Crear compuertas

puerta_sala = Compuerta(369, 15)
puerta_comedor = Compuerta(369, 15)

# Grupo de sprites
#all_sprites = pygame.sprite.Group()
#all_sprites.add(player)

print(all_sprites)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SHOW_WAIT_BOX_EVENT:
            print("Imagen wait_box mostrada!")
            screen.blit(wait_box, (0, 0))
            pygame.display.update()
            pygame.time.wait(5000)  # Pausar el bucle durante 5 segundos

        """
        if pc.active:
            pc.handle_event(event)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Interactuar con la PC al presionar la tecla "e"
                    if player.rect.colliderect(pygame.Rect(200, 200, 32, 32)):
                        print("he colisionado con la pc")
                        pc.open()
        """

        # Si colisiona con la PC

        

      
        if pc.active:
            pc.handle_event(event)
        else:
            if player.rect.colliderect(pc.rectangle) and tag_level == "sistemas":
                print("he colisionado con la pc")
                print(pc.rectangle.x, pc.rectangle.y)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        pc.open()
                        pc.draw(screen)
                     

        
        # Si colisiona con la compuerta de la sala puede ir a la sala o volver a sistemas

        if player.rect.colliderect(puerta_sala.rectangle) and tag_level != "sala" and tag_level != "comedor":
                print("voy a la sala")
                tag_level = "sala"
                puerta_sala.set_position(369 , 572)
                player.set_position(380, 532)
                tmx_data = pytmx.load_pygame('src/nivel2/mapa2.tmx')
                collision_objects = get_collision_objects(tmx_data)
                #print(puerta_sala.x, puerta_sala.y)

        if player.rect.colliderect(puerta_sala.rectangle) and tag_level == "sala":
                print("vuelvo a sistemas")
                tag_level = "sistemas"
                puerta_sala.set_position(369, 15)
                player.set_position(380, 48)
                tmx_data = pytmx.load_pygame('src/nivel1/mapa1.tmx')
                collision_objects = get_collision_objects(tmx_data)
                #print(collision_objects)

        # Si colisiona con la compuerta del comedor puede ir al comedor o volver a la sala

        if player.rect.colliderect(puerta_comedor.rectangle) and tag_level != "comedor":
                print("voy al comedor")
                tag_level = "comedor"
                puerta_comedor.set_position(369 , 572)
                player.set_position(380, 532)
                tmx_data = pytmx.load_pygame('src/nivel3/mapa3.tmx')
                collision_objects = get_collision_objects(tmx_data)
                #print(puerta_sala.x, puerta_sala.y)

        if player.rect.colliderect(puerta_comedor.rectangle) and tag_level == "comedor":
                print("vuelvo a la sala")
                tag_level = "sala"
                puerta_comedor.set_position(369, 15)
                player.set_position(380, 48)
                tmx_data = pytmx.load_pygame('src/nivel2/mapa2.tmx')
                collision_objects = get_collision_objects(tmx_data)
                #print(collision_objects)
            


    

    # Obtener las teclas presionadas
    """
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
    """

    if not pc.active:
        #all_sprites.update(keys)
        all_sprites.update()

    # Mover al jugador
    player.move(0, 0, collision_objects)

   

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el mapa
    draw_map(screen, tmx_data)

    # Dibujar el jugador
    #player.draw(screen)

     # Actualizar todos los sprites
    all_sprites.update()

    

    # Dibujar los objetos de colisión (opcional, para depuración)
    #for rect in collision_objects:
        #pygame.draw.rect(screen, (255, 0, 0), rect, 2)

    # Dibujar PC
    
    if (pc.active and tag_level == "sistemas"):
        pc.draw(screen)
        
    
    if (tag_level == "sistemas"):
        # Dibujar la PC en el mapa (rectángulo representando la PC)
        pygame.draw.rect(screen, [0, 0, 0], [144, 126, 36, 36], 1)
        # Todo este código de abajo es para hacer transparente el Rect que está por encima de la PC del player
        #s = pygame.Surface([36,36])  
        #s.convert_alpha()               
        #s.fill((0,0,0,0))           
        #screen.blit(s,(0,0) , (144,126,36,36))
        
        pass

    if (tag_level == "sala"):
        # En esta parte actuará el NPC_Detector
        random_flag = random.randint(1,500)
        npc_detector.npc_new_random(random_flag)
        
        
        screen.blit(frame_zafiro, (175,90)) # pone el frame de zafiro en la ventana
        screen.blit(frame_mel, (280,90)) # pone el frame de mel en la ventana
        
        if npc_detector.shooter():
             pygame.event.post(pygame.event.Event(SHOW_WAIT_BOX_EVENT))
             
             
             
        #screen.blit(wait_box, (380, 90))

        # Colisiones de prueba
        if player.rect.colliderect(npc1_zafiro.rectangle) and tag_level == "sala":
                print(f"He colisionado con {npc1_zafiro.name}")
        if player.rect.colliderect(npc2_mel.rectangle) and tag_level == "sala":
                print(f"He colisionado con {npc2_mel.name}")
                
                
        
        

                

        #frame_wait = npc_detector.get_image(0, 32, 32)


    # Dibujar la compuerta de la sala

    #puerta_sala = Compuerta(screen, 61, 20)
    if pc.active == False: # Se dibuja la compuerta de la sala solo si no se ha ingresado a la pc
        pygame.draw.rect(screen, (0,255,0), puerta_sala.rectangle)
    
    #pygame.draw.rect(screen, (0,255,0), [370, 16, puerta_sala.x, puerta_sala.y], 1)
    #s = pygame.Surface([36,36])  
    #s.convert_alpha()               
    #s.fill((0,0,0,0))           
    #screen.blit(s,(0,0) , (144,126,36,36))

    # Dibujar la compuerta del comedor

    #puerta_sala = Compuerta(screen, 61, 20)
    if pc.active == False and tag_level != "sistemas": # Se dibuja la compuerta de la sala solo si no se ha ingresado a la pc
        pygame.draw.rect(screen, (255,0,0), puerta_comedor.rectangle)
    
    #pygame.draw.rect(screen, (0,255,0), [370, 16, puerta_sala.x, puerta_sala.y], 1)
    #s = pygame.Surface([36,36])  
    #s.convert_alpha()               
    #s.fill((0,0,0,0))           
    #screen.blit(s,(0,0) , (144,126,36,36))

    # Dibuja los sprites agregados al grupo
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de cuadros por segundo
    pygame.time.Clock().tick(50)

# Salir del programa
pygame.quit()
sys.exit()

