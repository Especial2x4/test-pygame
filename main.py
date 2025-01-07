
import pygame
import pytmx
import sys
import random

from Player import *
from PC import *
from Compuerta import *
from NPC import *
from NPC_Detector import *
from Cocinero import *
from Barra import *

from config import *

# Inicializar Pygame
pygame.init()

# CONFIGURACIÓN DE LA VENTANA -------------------------------------------------------------------------------------------

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Soportando-IT")

# -----------------------------------------------------------------------------------------------------------------------

# Interruptor de nivel
tag_level = "sistemas"

# Interruptor de menú comedor
tag_show_menu = False

# Definir eventos personalizados
SHOW_WAIT_BOX_EVENT = pygame.USEREVENT + 1 # Evento que muestra el mensaje de de WAIT cuando se activa el NPC_Detector
SHOW_COMIDA_MENU_EVENT = pygame.USEREVENT + 2

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
            
        if obj.name == "colision-sala":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-computer-server":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-server":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-computer":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-printer":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-ap":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-mostrador":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-heladera":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-mesa":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
        if obj.name == "colision-toilete":
            rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
            collision_objects.append(rect)
            
            

    return collision_objects

# Obtener los objetos de colisión
collision_objects = get_collision_objects(tmx_data)

# RUTAS DE HOJAS DE SPRITE --------------------------------------------------------------------------------------------------------------------

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
# Cocinero
sprite_sheet_cocinero = "src/assets/cocinero.png" # Hoja de sprite que corresponde a camorre
# Ruta del alert box
sprite_sheet_wait = "src/assets/wait-box.png"
wait_box = pygame.image.load(sprite_sheet_wait).convert_alpha()


# INSTANCIA DE PLAYER -----------------------------------------------------------------------------------------------------------------------
player = Player(sprite_sheet_path, SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites = pygame.sprite.Group(player)
pc = PC()

# -------------------------------------------------------------------------------------------------------------------------------------------

NPC_LISTAO = [
     
     NPC(sprite_sheet_zafiro, "Sra Zafiro", personality=NPC_PERSONALITY_DICT['hostil'], tupla_rect=((162, 110, 44, 49)), shooter_num=10),
     NPC(sprite_sheet_mel, "Mel", personality=NPC_PERSONALITY_DICT['accesible'], tupla_rect=((272, 112, 47, 48)), shooter_num=20)
     
]

# INSTANCIAS DE NPC´s -----------------------------------------------------------------------------------------------------------------------

# Instancia señora Zafiro
npc1_zafiro = NPC_LISTAO[0]
frame_zafiro = npc1_zafiro.get_image(0, 32, 32) # recorta el frame que se necesita

# Instancia Mel
npc2_mel = NPC_LISTAO[1]
frame_mel = npc2_mel.get_image(0, 32, 32) # recorta el frame que se necesita

# INSTANCIA DE Cocinero -----------------------------------------------------------------------------------------------------------------------
cocinero = Cocinero(sprite_sheet_cocinero, "src/assets/portraits/cocinero.png")
frame_cocinero = cocinero.get_image(0, 32, 32)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Instancia del NPC-detector ------------------------------------------------------------------------------------------------------------------
random_flag = 0
npc_detector = NPC_Detector(NPC_LISTAO, random_flag, sprite_sheet_wait, screen) #-> pone el cartelito de wait sobre el NPC activado, retorna dicho NPC y se pasa a la distancia para un duelo


# Crear compuertas -----------------------------------------------------------------------------------------------------------------------------

puerta_sala = Compuerta(369, 15)
puerta_comedor = Compuerta(369, 15)

# Crear la barra del comedor --------------------------------------------------------------------------------------------------------------------
barra_comedor = Barra(80, 100)


print(all_sprites)

# BUCLE PRINCIPAL DEL JUEGO -------------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SHOW_WAIT_BOX_EVENT: # Se ejecuta la lógica del evento personalizado
            print("Imagen wait_box mostrada!")
            print(f"el NPC que se activó es : {npc_detector.get_npc_activate().name}")
            print(f"posición de {npc_detector.get_npc_activate().name} : {npc_detector.get_npc_activate().rectangle}")
            offset_left = npc_detector.get_npc_activate().rectangle.left + 10
            offset_top = npc_detector.get_npc_activate().rectangle.top - 60
            screen.blit(wait_box, (offset_left, offset_top))
            pygame.display.update()
            pygame.time.wait(5000)  # Pausar el bucle durante 5 segundos
        """
        elif event.type == SHOW_COMIDA_MENU_EVENT: # Se muestra el menú de comida
            if tag_show_menu == True:
                screen.fill((0, 0, 0))
                text = pygame.font.Font(None, 36).render("Welcome to the PC!", True, (255, 255, 255))
                screen.blit(text, (50, 50))
                text = pygame.font.Font(None, 36).render("Press Enter to exit", True, (255, 255, 255))
                screen.blit(text, (50, 100))
                pygame.display.update()
                #tag_show_menu = False
        """    
            
            
            
            

      

        
        # Si colisiona con la PC ---------------------------------------------------------------------------------------------------------------
      
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

        
        # Si colisiona con la barra ------------------------------------------------------------------------------------------------------------
      
        if barra_comedor.active:
            barra_comedor.handle_event(event)
        else:
            if player.rect.colliderect(barra_comedor.rectangle) and tag_level == "comedor":
                print("he colisionado con la barra y voy a pedir comida")
                print(barra_comedor.rectangle.x, barra_comedor.rectangle.y)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        barra_comedor.open()
                        barra_comedor.draw(screen, cocinero)
                     

        
        # Si colisiona con la compuerta de la sala puede ir a la sala o volver a sistemas

        if player.rect.colliderect(puerta_sala.rectangle) and tag_level != "sala" and tag_level != "comedor":
                print("voy a la sala")
                tag_level = "sala"
                puerta_sala.set_position(369 , 572)
                player.set_position(380, 532)
                tmx_data = pytmx.load_pygame('src/nivel2/mapa2.tmx')
                collision_objects = get_collision_objects(tmx_data)
                

        if player.rect.colliderect(puerta_sala.rectangle) and tag_level == "sala":
                print("vuelvo a sistemas")
                tag_level = "sistemas"
                puerta_sala.set_position(369, 15)
                player.set_position(380, 48)
                tmx_data = pytmx.load_pygame('src/nivel1/mapa1.tmx')
                collision_objects = get_collision_objects(tmx_data)
                

        # Si colisiona con la compuerta del comedor puede ir al comedor o volver a la sala

        if player.rect.colliderect(puerta_comedor.rectangle) and tag_level != "comedor":
                print("voy al comedor")
                tag_level = "comedor"
                puerta_comedor.set_position(369 , 572)
                player.set_position(380, 532)
                tmx_data = pytmx.load_pygame('src/nivel3/mapa3.tmx')
                collision_objects = get_collision_objects(tmx_data)
                

        if player.rect.colliderect(puerta_comedor.rectangle) and tag_level == "comedor":
                print("vuelvo a la sala")
                tag_level = "sala"
                puerta_comedor.set_position(369, 15)
                player.set_position(380, 48)
                tmx_data = pytmx.load_pygame('src/nivel2/mapa2.tmx')
                collision_objects = get_collision_objects(tmx_data)


        """
        if player.rect.colliderect(barra_comedor.rectangle) and tag_level == "comedor":
                print("He colisionado con la barra y voy a pedir comida")
                
                if tag_show_menu == False:
                     pygame.event.post(pygame.event.Event(SHOW_COMIDA_MENU_EVENT))
                     tag_show_menu = True
        """
                        
                
                
                
            


    if not pc.active and not barra_comedor.active:
        all_sprites.update()
        # Mover al jugador si la PC y la barra del comedor no están activas
        player.move(0, 0, collision_objects)

    

   

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el mapa
    draw_map(screen, tmx_data)

    

    # Actualizar todos los sprites ( Analizar esta linea más adelante)
    #all_sprites.update()

    

    # BLOQUE NECESARIO PARA INGRESAR AL INVENTARIO DE LA PC --------------------------------------------------------------------------------------
    
    if (pc.active and tag_level == "sistemas"):
        pc.draw(screen)

        
    
    if (tag_level == "sistemas"):
        # Dibujar la PC en el mapa (rectángulo representando la PC)
        pygame.draw.rect(screen, [0, 0, 0], [144, 126, 36, 36], 1)
        
        
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    if (tag_level == "sala"):
        
        # PRECONFIGURACIÓN DEL NPC_DETECTOR --------------------------------------------------------------------------------------------------
        random_flag = random.randint(1,500) # Genera un número aleatorio el cual al coincidir con el shooter_num del NPC se dispara el shooter
        npc_detector.set_npc_new_random(random_flag) # Se setea el nuevo número random flag en el NPC_Detector
        
        # EN ESTA PARTE SE COLOCAN LOS NPC EN EL SCREEN -------------------------------------------------------------------------------------- 
        screen.blit(frame_zafiro, (175,90)) # pone el frame de zafiro en la ventana
        screen.blit(frame_mel, (280,90)) # pone el frame de mel en la ventana
        
        # SI EL SHOOTER DEVUELVE TRUE SE DISPARA LA COLA DE EVENTO PERSONALIZADO ACTIVANDO EL NPC_DETECTOR -----------------------------------
        if npc_detector.shooter():
             pygame.event.post(pygame.event.Event(SHOW_WAIT_BOX_EVENT))
             
   

        # Colisiones de prueba
        if player.rect.colliderect(npc1_zafiro.rectangle) and tag_level == "sala":
                print(f"He colisionado con {npc1_zafiro.name}")
        if player.rect.colliderect(npc2_mel.rectangle) and tag_level == "sala":
                print(f"He colisionado con {npc2_mel.name}")
                

    if (tag_level == "comedor"):
         # SI ESTÁ EN EL COMEDOR SE DIBUJA EL COCINERO
         screen.blit(frame_cocinero, (135,60)) # pone el frame de zafiro en la ventana
         



    # Dibujar la compuerta de la sala
    if pc.active == False: # Se dibuja la compuerta de la sala solo si no se ha ingresado a la pc
        pygame.draw.rect(screen, (0,255,0), puerta_sala.rectangle)
    

    # Dibujar la compuerta del comedor
    if pc.active == False and tag_level != "sistemas": # Se dibuja la compuerta de la sala solo si no se ha ingresado a la pc
        pygame.draw.rect(screen, (255,0,0), puerta_comedor.rectangle)
    

    # BLOQUE NECESARIO PARA INGRESAR AL MENÚ DEL COMEDOR --------------------------------------------------------------------------------------

    if (barra_comedor.active and tag_level == "comedor"):
        barra_comedor.draw(screen, cocinero)


    # Dibujar la barra del comedor
    if barra_comedor.active == False and tag_level == "comedor": # Se dibuja la barra del comedor
        pygame.draw.rect(screen, (0,0,255), barra_comedor.rectangle)
        
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    # Dibuja los sprites agregados al grupo (player) solo si la pc y la barra del comedor no están activas
    if not pc.active and not barra_comedor.active:
         all_sprites.draw(screen)
        
         
    

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de cuadros por segundo
    pygame.time.Clock().tick(50)

# Salir del programa
pygame.quit()
sys.exit()

