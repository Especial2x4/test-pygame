import pygame


class Barra:
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.active = False
        self.rectangle = pygame.Rect(pos_x, pos_y, 142, 18)

        #self.listao_menu = ["Lomito de atún a la provenzal", "Macarrones con salsa Boloñesa", "Sanguchito de queso"]
        self.dict_menu = {
        "Lomito de atún a la provenzal": 15,
        "Macarrones con salsa Boloñesa": 10,
        "Sanguchito de queso": 1
        }
        self.selected_option = 0


    # Función para dibujar el menú con opciones resaltadas
    def draw_menu(self, screen, options, selected_index, x, y, color, selected_color, rect_color):
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
                pygame.draw.rect(screen, rect_color, (x - 10, y + i * 40 - 5, text_width + 20, text_height + 10))

            # Dibuja el texto
            screen.blit(text_surface, (x, y + i * 40))


    # Función para dibujar texto
    def draw_text(self, screen, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        screen.blit(text_surface, (x, y))


    # Función para wrappear el texto en ventana
    def draw_wrapped_text(self,screen, text, x, y, max_width, color):
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
            screen.blit(line_surface, (x, y + i * self.font.get_linesize()))


    

    def set_position(self, pos_x, pos_y):
        
        self.rectangle = pygame.Rect(pos_x,pos_y, 142, 18)


    def open(self):
        self.active = True

    def close(self):
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(f"voy a comer {self.get_selected_option_name()}") # Imprime la comida elegida
                self.close()
            elif event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.dict_menu)  # Mover hacia arriba
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.dict_menu)  # Mover hacia abajo

    
    def draw(self, screen, cocinero):
        if self.active:
            screen.fill((255, 255, 255))
            #text = self.font.render("Acá va a ir el menú del comedor", True, (255, 255, 255))
            #screen.blit(text, (50, 50))
            #text = self.font.render("Press Enter to exit", True, (255, 255, 255))
            #screen.blit(text, (50, 100))
            screen.blit(cocinero.portrait, (50, 50))  # Posición del retrato en la pantalla
            self.draw_text(screen, "Hola que vas a comprar?", 430, 90, (0,0,0))
            self.draw_menu(screen, self.dict_menu, self.selected_option, 60, 460, (0,0,0), (255,255,255), (0,0,255))  # Dibuja el menú con opciones


    # Retorna el nombre de la opción elegida en el menú
    def get_selected_option_name(self):
        #comida_elegida = self.selected_option
        #print(f"voy a comer {comida_elegida}")
        comida_elegida_name = list(self.dict_menu.keys())[self.selected_option] # Transforma el diccionario en una lista de claves para que pueda ser accedido por el índice

        return comida_elegida_name
            

    # Retorna el valor de la opción elegida en el menú
    def get_selected_option_price(self):

        comida_elegida_price = list(self.dict_menu.values())[self.selected_option] # Transforma el diccionario en una lista de valores para que pueda ser indexado
        return comida_elegida_price