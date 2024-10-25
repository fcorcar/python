import sys, jugador

def has_perdido():
    print("Has perdido.")
    print(f"Has obtenido {jugador.lista_jugadores[0].puntos} puntos.")
    sys.exit()