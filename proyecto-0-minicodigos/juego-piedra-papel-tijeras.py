import random
import os

opciones = ["Piedra", "Papel", "Tijeras"]
input_jugador = ""
input_ia = ""
puntuacion_jugador = 0
puntuacion_ia = 0
jugando = True
nombre = ""


def borrarConsola():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def asignarValor(valor):
        if valor == "Piedra":
            return 3
        
        elif valor == "Tijeras":
            return 2
        
        elif valor == "Papel":
            return 1


def puntuar_jugadores(p):
    if p == "jugador":
        global puntuacion_jugador
        puntuacion_jugador += 1

    elif p == "ia":
        global puntuacion_ia
        puntuacion_ia += 1

    print(f"{nombre} {puntuacion_jugador} - IA {puntuacion_ia}\n")


def mostrar_titulo_puntos(j):
    borrarConsola()
    print("¡¡¡JUEGO DE PIEDRA, PAPEL O TIJERAS!!!")
    puntuar_jugadores(j)


def mostrar_resultados(ganador):
    print(f"{nombre}: {input_jugador}")
    print(f"IA: {input_ia}")
    print(ganador)

        
def jugar():
    mostrar_titulo_puntos("0")

    opcion = int(input("1. PIEDRA \n2. PAPEL \n3. TIJERAS \nIntroduce una opción (1-3): "))

    if not (opcion > 0 and opcion < 4):
        borrarConsola()
        print("¡ERROR! Introduce una opción del 1 al 3.")
        return

    global input_jugador
    global input_ia
    input_jugador = opciones[opcion - 1]
    input_ia = random.choice(opciones)


    if asignarValor(input_jugador) > asignarValor(input_ia) and input_jugador[0] != input_ia[0] or asignarValor(input_jugador) < asignarValor(input_ia) and input_jugador[0] == input_ia[0]:
        mostrar_titulo_puntos("jugador")
        mostrar_resultados(f"\nGana {nombre}")       

    elif asignarValor(input_jugador) == asignarValor(input_ia):
        mostrar_titulo_puntos("0")
        mostrar_resultados("\nEMPATE")

    else:
        mostrar_titulo_puntos("ia")
        mostrar_resultados("\nGana la IA")


borrarConsola()
print("¡¡¡JUEGO DE PIEDRA, PAPEL O TIJERAS!!!")
nombre = input("Introduce tu nombre: ")
jugar()


while jugando:
    if puntuacion_jugador == 3:
        jugando = False
        mostrar_titulo_puntos("0")
        print(f"¡¡¡Has ganado {nombre}!!!")
        break

    elif puntuacion_ia == 3:
        jugando = False
        mostrar_titulo_puntos("0")
        print("¡¡¡Ha ganado la IA!!!")
        break

    input("\nPulsa ENTER para continuar...")
    jugar()

