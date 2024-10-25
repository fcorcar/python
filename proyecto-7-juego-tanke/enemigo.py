import pygame, random, constantes, jugador, bala

class Enemigo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = constantes.ANCHO_ENEMIGO
        self.alto = constantes.ALTO_ENEMIGO
        self.color = constantes.COLOR_ENEMIGO
        self.velocidad = 5
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self):
        self.y += self.velocidad

    def detectar_colision(self):
        #Colision Enemigo con jugador
        if pygame.Rect.colliderect(jugador.lista_jugadores[0].rect, self.rect):
            jugador.lista_jugadores[0].restar_vidas()
            self.destruirse()

        #Colision Enemigo con Balas
        for bal in bala.lista_balas:
            if pygame.Rect.colliderect(bal.rect, self.rect):
                jugador.lista_jugadores[0].sumar_puntos(5)
                self.destruirse()
                bal.destruirse()

    def destruirse(self):
        lista_enemigos.remove(self)



#ENEMIGO
lista_enemigos = []
tiempo_pasado = 0
tiempo_entre_enemigos = 30 #Frames por segundo

def crear_enemigos():
    global tiempo_pasado, tiempo_entre_enemigos
    tiempo_pasado += 1

    if tiempo_pasado >= tiempo_entre_enemigos:
        lista_enemigos.append(Enemigo(random.randint(0, constantes.RESOLUCION_VENTANA_ACTUAL[0] - constantes.ANCHO_ENEMIGO), -constantes.ALTO_ENEMIGO))
        tiempo_pasado = 0
        tiempo_entre_enemigos = random.randint(20, 100) #Frames por segundo

def mover_dibujar_enemigos(ventana):
    for enemigo in lista_enemigos:
        enemigo.mover()
        enemigo.dibujar(ventana)

def colisiones_enemigos():
    for enemigo in lista_enemigos:
        enemigo.detectar_colision()

def comprobar_posicion_enemigos():
    for enemigo in lista_enemigos:
        if enemigo.y >= constantes.RESOLUCION_VENTANA_ACTUAL[1] - enemigo.alto:
            enemigo.destruirse()

            if jugador.lista_jugadores[0].puntos > 1:
                jugador.lista_jugadores[0].sumar_puntos(-2)

            jugador.lista_jugadores[0].restar_vida_ciudad(2)