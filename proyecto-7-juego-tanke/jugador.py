import pygame, constantes, acciones
rotacion = 0
class Jugador():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = constantes.ANCHO_JUGADOR
        self.alto = constantes.ALTO_JUGADOR
        self.color = constantes.COLOR_JUGADOR
        self.velocidad = 18
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.vidas = 3
        self.vida_ciudad = 100
        self.puntos = 0
        self.imagen = jugador_imagen
        self.rueda = rueda_imagen

    def dibujar(self, ventana):

        ventana.blit(self.imagen, (self.x-36, self.y - 194))

        #Rota la imagen
        img_rotada1 = pygame.transform.rotozoom(self.rueda, rotacion, 1.0)

        # Centrar la imagen rotada en la posición deseada
        img_rect1 = img_rotada1.get_rect(center=(self.x + 35, self.y + 30))
        ventana.blit(img_rotada1, img_rect1)

        # Centrar la imagen rotada en la posición deseada
        img_rect2 = img_rotada1.get_rect(center=(self.x + 224, self.y + 30))
        ventana.blit(img_rotada1, img_rect2)

        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self, teclas):
        global rotacion
        
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
            rotacion += 16

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
            rotacion -= 16

        #Limite movimiento jugador en pantalla
        if self.x <= 0:
            self.x = 0

        elif self.x >= constantes.RESOLUCION_VENTANA_ACTUAL[0] - self.ancho:
            self.x = constantes.RESOLUCION_VENTANA_ACTUAL[0] - self.ancho

    def restar_vidas(self):
        self.vidas -= 1
        if self.vidas == 0: acciones.has_perdido()
    
    def sumar_puntos(self, p_suma):
        self.puntos += p_suma

    def restar_vida_ciudad(self, v_resta):
        self.vida_ciudad -= v_resta
        if self.vida_ciudad == 0: acciones.has_perdido()
        
#
escala = 0.33
jugador_imagen = pygame.image.load("./images/jugador/GIRO_CABEZA_LUIS_00.png")
jugador_imagen = pygame.transform.scale(jugador_imagen,
                                        (jugador_imagen.get_width()*escala,
                                        jugador_imagen.get_height()*escala))

rueda_imagen = pygame.image.load("./images/jugador/ruedaF.png")
rueda_imagen = pygame.transform.scale(rueda_imagen,
                                        (rueda_imagen.get_width()*escala,
                                        rueda_imagen.get_height()*escala))




#JUGADOR
lista_jugadores = []

def crear_jugador():
    lista_jugadores.append(Jugador(300, constantes.RESOLUCION_VENTANA_ACTUAL[1] - constantes.ALTO_JUGADOR))

def mover_dibujar_jugador(ventana, teclas):
    lista_jugadores[0].mover(teclas)
    lista_jugadores[0].dibujar(ventana)

