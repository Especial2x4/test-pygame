
import math
import sys
import pygame


class Combate():

    def __init__(self, screen):
        
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        
        self.battle_log = []
        self.menu_options = ["Resolver", "Escapar"]
        self.selected_option = 0  # Índice de la opción seleccionada
        self.sra_zafiro_text = "Dale que me anda para la Mi3rda la computadora!"  # Texto inicial de Sra Zafiro    
        self.menu_state = "main_menu"  # Estados posibles: "main_menu", "resolver_menu", "reward_screen"
            

    


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


    
    # Función para dibujar el menú con opciones resaltadas
    def draw_menu(self,options, selected_index, x, y, color=(0,0,0), selected_color=(255,255,255), rect_color=(0,0,255)):
        """
        Dibuja un menú con opciones y resalta la opción seleccionada con un rectángulo.
        :param options: Lista de opciones.
        :param selected_index: Índice de la opción seleccionada.
        :param x: Posición x del menú.
        :param y: Posición y del menú.
        :param color: Color del texto no seleccionado.
        :param selected_color: Color del texto seleccionado.
        :param rect_color: Color del rectángulo de selección.
        """
        for i, option in enumerate(options):
            option_text = f"> {option}" if i == selected_index else option
            text_surface = self.font.render(option_text, True, selected_color if i == selected_index else color)
            text_width, text_height = text_surface.get_size()

            # Dibuja el rectángulo si es la opción seleccionada
            if i == selected_index:
                pygame.draw.rect(self.screen, rect_color, (x - 10, y + i * 40 - 5, text_width + 20, text_height + 10))

            # Dibuja el texto
            self.screen.blit(text_surface, (x, y + i * 40))



    
    # Función para dibujar texto
    def draw_text(self, text, x, y, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))


    # Función para wrappear el texto en ventana
    def draw_wrapped_text(self, text, x, y, max_width, color=(0, 0, 0)):
        """
        Dibuja texto ajustado a un ancho máximo.
        :param text: El texto a dibujar.
        :param x: Posición x en la pantalla.
        :param y: Posición y en la pantalla.
        :param max_width: Ancho máximo permitido para el texto.
        :param color: Color del texto.
        """
        words = text.split()  # Divide el texto en palabras
        lines = []  # Almacena las líneas ajustadas
        current_line = ""

        # Crea líneas ajustadas al ancho máximo
        for word in words:
            test_line = current_line + " " + word if current_line else word
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        # Agrega la última línea
        if current_line:
            lines.append(current_line)

        # Dibuja las líneas ajustadas
        for i, line in enumerate(lines):
            line_surface = self.font.render(line, True, color)
            self.screen.blit(line_surface, (x, y + i * self.font.get_linesize()))


    # Función hardcodeada para volver el menú al estado inicial
    def volver_estado_inicial(self, npc):

        self.menu_state = "main_menu"
        self.battle_log = []
        self.sra_zafiro_text = "Dale que me anda para la Mi3rda la computadora!"
        self.menu_options = ["Resolver", "Escapar"]
        


    # Función que lanza el sistema de combate -------------------------------------------------------------

    def system_combat(self, npc):


        width = self.screen.get_width()

        running = True
        while running:
            self.screen.fill((255, 255, 255))
            
            # Detener o reproducir música según el estado del menú
            if self.menu_state == "reward_screen":
                if pygame.mixer.music.get_busy():  # Si la música está sonando
                    pygame.mixer.music.pause()  # Pausa la música

            # Dibujar los elementos según el estado del menú
            if self.menu_state == "main_menu":
                self.screen.blit(npc.portrait, (50, 50))  # Posición del retrato en la pantalla
                self.draw_text(f"{npc.name} - HP: {npc.current_hp}/{npc.max_hp}", 50, 10)
                self.draw_text(f"{npc.name} dice: ", 430, 50)
                self.draw_wrapped_text(self.sra_zafiro_text, 430, 90, width - 440)
                self.draw_text("Elegir una opción :", 60, 420)
                #draw_text("1> Resolver  2> Escapar", 60, 360)
                self.draw_menu(self.menu_options, self.selected_option, 60, 460)  # Dibuja el menú con opciones
            elif self.menu_state == "resolver_menu":
                self.menu_options = ["Reiniciar la PC"]
                self.screen.blit(npc.portrait, (50, 50))  # Posición del retrato en la pantalla
                self.draw_text(f"{npc.name} - HP: {npc.current_hp}/{npc.max_hp}", 50, 10)
                self.draw_text(f"{npc.name} dice: ", 430, 50)
                self.draw_wrapped_text(self.sra_zafiro_text, 430, 90, width - 440)  # Asegurarse de que el texto se actualice aquí también.
                self.draw_text("Elegir una opción :", 60, 420)
                #draw_text("1> Reiniciar la PC", 60, 360)
                self.draw_menu(self.menu_options, self.selected_option, 60, 460)  # Dibuja el menú con opciones
            elif self.menu_state == "reward_screen":
                self.draw_text("Bien hecho!", 60, 60)
                self.draw_text("Recompensas:", 60, 100)
                self.draw_text("Has ganado 100 de experiencia", 60, 140)
                self.draw_text("Ahora eres un Junior", 60, 180)
                self.draw_text("Has ganado 1000 pe", 60, 220)
                self.draw_text("Has destrabado gpupdate", 60, 260)
                self.draw_text("Presiona enter para continuar.", 120, 320)
                self.draw_text("...Fin...", 60, 420)
                

            # Dibujar registros de batalla solo si no estamos en la pantalla de recompensas
            if self.menu_state != "reward_screen":
                log_pos_x = 60
                log_pos_y = 500
                interlineado = 30
                for i, log in enumerate(self.battle_log[-3:]):  # Solo muestra los últimos 3 mensajes
                    self.draw_text(log, log_pos_x, log_pos_y + i * interlineado)

            # Manejo de eventos
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if self.menu_state == "main_menu":
                        if event.key == pygame.K_UP:
                            self.selected_option = (self.selected_option - 1) % len(self.menu_options)  # Mover hacia arriba
                        elif event.key == pygame.K_DOWN:
                            self.selected_option = (self.selected_option + 1) % len(self.menu_options)  # Mover hacia abajo
                        elif event.key == pygame.K_RETURN:  # Seleccionar opción
                            if self.selected_option == 0:  # Resolver
                                self.menu_state = "resolver_menu"
                                print("has elegido resolver")
                            elif self.selected_option == 1:  # Escapar
                                self.battle_log.append("¡Has escapado!")
                                self.volver_estado_inicial()
                                npc.current_hp = 10
                                running = False
                    elif self.menu_state == "resolver_menu":
                        if event.key == pygame.K_RETURN and self.sra_zafiro_text != "chau":  # Reiniciar la PC
                            self.battle_log.append("Reiniciar la PC fue efectivo...")
                            npc.take_damage(10)
                            self.sra_zafiro_text = "chau"  # Actualiza el texto de Sra Zafiro
                            self.battle_log.append("Presiona enter para continuar...")
                        elif event.key == pygame.K_RETURN and self.sra_zafiro_text == "chau":  # Presionar Enter después de "chau"
                            self.menu_state = "reward_screen"
                    elif self.menu_state == "reward_screen":
                        if event.key == pygame.K_RETURN:  # Presionar Enter en la pantalla de recompensas
                            self.volver_estado_inicial(npc)
                            npc.current_hp = 10
                            running = False  # O puedes cambiar a otro estado o acción

            pygame.display.flip()
        