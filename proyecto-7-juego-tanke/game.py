import pygame, sys, constantes, enemigo, jugador, bala

pygame.init()

#JUEGO
reloj = pygame.time.Clock()

#VENTANA
ventana = pygame.display.set_mode(constantes.TAMANO_VENTANA)
constantes.establecer_resolucion(pygame.display.get_window_size())
pygame.display.set_caption("TANKE LOCO")

#JUGADOR
jugador.crear_jugador()


while True:

    #JUEGO
    reloj.tick(constantes.FPS)

    #VENTANA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        sys.exit()

    ventana.fill(constantes.COLOR_VENTANA)

    #JUGADOR
    jugador.mover_dibujar_jugador(ventana, pygame.key.get_pressed())

    #ENEMIGOS
    enemigo.crear_enemigos()
    enemigo.mover_dibujar_enemigos(ventana)
    enemigo.colisiones_enemigos()
    enemigo.comprobar_posicion_enemigos()

    #BALAS
    bala.crear_balas(pygame.key.get_pressed())
    bala.mover_dibujar_balas(ventana)
    bala.comprobar_posicion_balas()
    bala.recargar_municion(pygame.key.get_pressed())

    #HUD
    texto_vidas = constantes.FUENTE.render(f"Vidas: {jugador.lista_jugadores[0].vidas}", True, "black")
    ventana.blit(texto_vidas, (20, 20))

    texto_ciudad = constantes.FUENTE.render(f"Ciudad: {jugador.lista_jugadores[0].vida_ciudad}%", True, "black")
    ventana.blit(texto_ciudad, (140, 20))

    texto_puntos = constantes.FUENTE.render(f"Puntos: {jugador.lista_jugadores[0].puntos}", True, "black")
    ventana.blit(texto_puntos, (330, 20))

    texto_municion = constantes.FUENTE.render(f"Munición: {bala.cantidad_municion}", True, "black")
    ventana.blit(texto_municion, (constantes.RESOLUCION_VENTANA_ACTUAL[0] - 175, 20))

    texto_recarga = constantes.FUENTE.render(f"{bala.estado_recarga}", True, "black")
    ventana.blit(texto_recarga, (constantes.RESOLUCION_VENTANA_ACTUAL[0] - 175, 50))
    

    #UPDATE
    pygame.display.update()