import pygame, constantes, jugador

class Bala():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = constantes.ANCHO_BALA
        self.alto = constantes.ALTO_BALA
        self.color = constantes.COLOR_BALA
        self.velocidad = 25
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self):
        self.y -= self.velocidad

    def destruirse(self):
        lista_balas.remove(self)



#BALAS
lista_balas = []
tiempo_pasado = 0
tiempo_entre_balas = constantes.TIEMPO_ENTRE_BALAS #Frames por segundo

tiempo_pasado_recarga = 0
tiempo_recarga = constantes.TIEMPO_RECARGA
cantidad_municion = constantes.CANTIDAD_MUNICION
estado_recarga = ""
recargando = False


def crear_balas(teclas):
    global tiempo_pasado, tiempo_entre_balas, cantidad_municion, recargando
    tiempo_pasado += 1

    if not recargando and (teclas[pygame.K_w] or teclas[pygame.K_UP]) and not teclas[pygame.K_a] and not teclas[pygame.K_LEFT] and not teclas[pygame.K_d] and not teclas[pygame.K_RIGHT] and tiempo_pasado >= tiempo_entre_balas:
        lista_balas.append(Bala(jugador.lista_jugadores[0].x + constantes.ANCHO_JUGADOR / 2 - constantes.ANCHO_BALA / 2, jugador.lista_jugadores[0].y - constantes.ALTO_BALA))
        tiempo_pasado = 0

        #Recarga
        cantidad_municion -= 1
        if cantidad_municion <= 0: recargando = True
            

def mover_dibujar_balas(ventana):
    for bala in lista_balas:
        bala.mover()
        bala.dibujar(ventana)


def comprobar_posicion_balas():
    for bal in lista_balas:
        if bal.y <= 0 - constantes.ALTO_BALA:
            bal.destruirse()
            
            #Si la bala no impacta en ningun enemigo te resta 1 punto
            if jugador.lista_jugadores[0].puntos > 0:
                jugador.lista_jugadores[0].sumar_puntos(-1)


def recargar_municion(teclas):
    global tiempo_pasado_recarga, cantidad_municion, recargando, tiempo_recarga, estado_recarga
    
    if teclas[pygame.K_r] or recargando:
        recargando = True
        tiempo_pasado_recarga += 1
        estado_recarga = "Recargando"

        if tiempo_pasado_recarga >= tiempo_recarga: 
            tiempo_pasado_recarga = 0
            recargando = False
            cantidad_municion = constantes.CANTIDAD_MUNICION
            estado_recarga = ""
