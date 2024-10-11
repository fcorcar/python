## 04/10/24
##VERSION-LINUX##

#LIBRERIAS
import tkinter as tk
import random
import time
import threading
import pygame


#VARIABLES
boton_actual = ""
secuencia_cpu = ""

numero_ejecuciones_secuencia_cpu = 0
posicion_actual_secuencia_cpu = 0

numero_ejecuciones_secuencia_usuario = 0
posicion_actual_secuencia_usuario = 0

puntos = 0

pygame.mixer.init()
sonido_1 = pygame.mixer.Sound("sounds/do.mp3")
sonido_2 = pygame.mixer.Sound("sounds/re.mp3")
sonido_3 = pygame.mixer.Sound("sounds/mi.mp3")
sonido_4 = pygame.mixer.Sound("sounds/fa.mp3")
sonido_win = pygame.mixer.Sound("sounds/win.mp3")
sonido_game_over = pygame.mixer.Sound("sounds/gameover.mp3")


#FUNCIONES
def activar_desactivar_boton(estado_botones): #Cambia el color
    if estado_botones:
        boton_azul.config(state=tk.NORMAL)
        boton_rojo.config(state=tk.NORMAL)
        boton_verde.config(state=tk.NORMAL)
        boton_amarillo.config(state=tk.NORMAL)
    
    else:
        boton_azul.config(state=tk.DISABLED)
        boton_rojo.config(state=tk.DISABLED)
        boton_verde.config(state=tk.DISABLED)
        boton_amarillo.config(state=tk.DISABLED)


def restaurar_color(): #Finaliza o continua la secuencia
    global boton_actual, posicion_actual_secuencia_cpu, numero_ejecuciones_secuencia_cpu
    
    cambiar_color(boton_azul, "blue")
    cambiar_color(boton_rojo, "red")
    cambiar_color(boton_verde, "green")
    cambiar_color(boton_amarillo, "yellow")
    
    numero_ejecuciones_secuencia_cpu -= 1 #Resta el numero de ejecuciones de la secuencia_cpu

    if numero_ejecuciones_secuencia_cpu != 0: #Si el numero de ejecuciones no es igual a 0, pasa a la siguiente secuencia_cpu
        posicion_actual_secuencia_cpu += 1
        boton_actual = secuencia_cpu[posicion_actual_secuencia_cpu]
        time.sleep(0.4)
        mostrar_secuencia()

    else: #Si termina la secuencia_cpu, activa los botones permitiendo al usuario interactuar
        activar_desactivar_boton(True)
    

def cambiar_color(boton, color): #Cambia el color
    boton.config(bg=color)


def mostrar_secuencia(): #Inicia la secuencia_cpu
    if boton_actual == "1":
        cambiar_color(boton_azul, "white")
        sonido_1.play()
    
    elif boton_actual == "2":
        cambiar_color(boton_rojo, "white")
        sonido_2.play()

    elif boton_actual == "3":
        cambiar_color(boton_verde, "white")
        sonido_3.play()

    elif boton_actual == "4":
        cambiar_color(boton_amarillo, "white")
        sonido_4.play()
    

    t = threading.Timer(0.5, restaurar_color)
    t.start()
    
           
def crear_secuencia(): #Crea la secuencia que muestra al usuario
    global boton_actual, boton_azul, boton_rojo, boton_verde, boton_amarillo, secuencia_cpu, numero_ejecuciones_secuencia_cpu, posicion_actual_secuencia_cpu, posicion_actual_secuencia_usuario, numero_ejecuciones_secuencia_usuario
    
    secuencia_cpu += str(random.randint(1,4)) #Obtiene y suma un boton aleatorio a la secuencia
    
    numero_ejecuciones_secuencia_cpu = len(secuencia_cpu) #Obtiene el numero de caracteres de la secuencia_cpu para saber cuando detenerse
    posicion_actual_secuencia_cpu = 0 #Inicia en 0 para empezar mostrando el primer valor de la secuencia_cpu
    boton_actual = secuencia_cpu[posicion_actual_secuencia_cpu] #Guarda el primer valor de la secuencia_cpu

    numero_ejecuciones_secuencia_usuario = numero_ejecuciones_secuencia_cpu #Obtiene el numero de caracteres de la secuencia_cpu para saber cuando iniciar la siguiente
    posicion_actual_secuencia_usuario = 0 #Inicia en 0 para comparar los inputs de usuario
    
    etiqueta.config(text=f"Nivel: {puntos}") #Refresca los puntos cuando se inicia la siguiente secuencia

    activar_desactivar_boton(False) #Desactiva los botones mientras la secuencia se esta mostrando
    
    m = threading.Timer(1, mostrar_secuencia)
    m.start()
        
        
def boton_pulsado(valor):
    global posicion_actual_secuencia_usuario, numero_ejecuciones_secuencia_usuario, puntos, secuencia_cpu

    if valor == "1":
        sonido_1.play()
    
    elif valor == "2":
        sonido_2.play()

    elif valor == "3":
        sonido_3.play()

    elif valor == "4":
        sonido_4.play()

    if secuencia_cpu[posicion_actual_secuencia_usuario] == valor: #Si el boton que ha sido pulsado corresponde con el actual de la secuencia_cpu, ganas
        posicion_actual_secuencia_usuario += 1
        numero_ejecuciones_secuencia_usuario -= 1

        if numero_ejecuciones_secuencia_usuario == 0: #Si el numero de ejecuciones llega a 0 significa que la secuencia ha sido completada exitosamente, y pasa a la siguiente
            puntos += 1 
            time.sleep(0.3)
            sonido_win.play()     
            crear_secuencia()
    
    else: #Si pierdes se desactivan los botones
        etiqueta.config(text=f"¡Has perdido!  Nivel alcanzado: {puntos}")
        sonido_game_over.play() 
        activar_desactivar_boton(False)

        boton_comenzar.config(state=tk.NORMAL)

        cambiar_color(boton_azul, "black")
        cambiar_color(boton_rojo, "black")
        cambiar_color(boton_verde, "black")
        cambiar_color(boton_amarillo, "black")
        

def iniciar_juego(): #Inicia el juego
    global secuencia_cpu, puntos 

    secuencia_cpu = "" #Reestablece la secuencia para rejugar
    puntos = 0 #Reestablece los puntos para rejugar

    boton_comenzar.config(state=tk.DISABLED)

    cambiar_color(boton_azul, "blue")
    cambiar_color(boton_rojo, "red")
    cambiar_color(boton_verde, "green")
    cambiar_color(boton_amarillo, "yellow")

    crear_secuencia()


#GRAFICOS
ventana = tk.Tk()
ventana.title("Juego de Memoria")
ventana.geometry("755x830")
ventana.resizable(False, False)
ventana.config(bg="cyan")

frame1 = tk.Frame(ventana)
frame1.config(width=705, height=80, bg="cyan3")
frame1.place(x=25, y=25)

etiqueta = tk.Label(frame1, text="Nivel: 0")
etiqueta.config(fg="black", bg="cyan3", font=("Arial", 21, "bold"))
etiqueta.place(x=15, y=22)

boton_comenzar = tk.Button(frame1, text="JUGAR", command=iniciar_juego)
boton_comenzar.config(fg="cyan", bg="black", activebackground="cyan", activeforeground="black", font=("Arial", 23, "bold"))
boton_comenzar.place(x=550, y=16)

boton_azul = tk.Button(ventana, command= lambda: boton_pulsado("1"))
boton_azul.config(width=35, height=15, bg="blue", bd=15, activebackground="blue", state="disabled")
boton_azul.place(x=25, y=130)

boton_rojo = tk.Button(ventana, command= lambda: boton_pulsado("2"))
boton_rojo.config(width=35, height=15, bg="red", bd=15, activebackground="red", state="disabled")
boton_rojo.place(x=390, y=130)

boton_verde = tk.Button(ventana, command= lambda: boton_pulsado("3"))
boton_verde.config(width=35, height=15, bg="green", bd=15, activebackground="green", state="disabled")
boton_verde.place(x=25, y=480)

boton_amarillo = tk.Button(ventana, command= lambda: boton_pulsado("4"))
boton_amarillo.config(width=35, height=15, bg="yellow", bd=15, activebackground="yellow", state="disabled")
boton_amarillo.place(x=390, y=480)


#PROGRAMA
ventana.mainloop()