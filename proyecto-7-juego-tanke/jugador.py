import pygame, constantes, sys, acciones

class Jugador():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = constantes.ANCHO_JUGADOR
        self.alto = constantes.ALTO_JUGADOR
        self.color = constantes.COLOR_JUGADOR
        self.velocidad = 15
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.vidas = 3
        self.puntos = 0

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self, teclas):
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.velocidad

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.velocidad

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
        



#JUGADOR
lista_jugadores = []

def crear_jugador():
    lista_jugadores.append(Jugador(300, constantes.RESOLUCION_VENTANA_ACTUAL[1] - constantes.ALTO_JUGADOR))

def mover_dibujar_jugador(ventana, teclas):
    lista_jugadores[0].mover(teclas)
    lista_jugadores[0].dibujar(ventana)