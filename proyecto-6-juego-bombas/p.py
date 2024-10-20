import tkinter as tk
import random

#Ventana
ancho_ventana = 1500
alto_ventana = 800

root = tk.Tk()
root.title("Juego")
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
resolucion_ventana = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"
root.geometry(resolucion_ventana)
root.resizable(False, False)


class Enemigo():
    ancho_enemigo = 45
    alto_enemigo = 45
    arrastrando_enemigo = False
    
    def __init__(self, posX_inicial_enemigo, posY_inicial_enemigo, direccion_enemigo_x, direccion_enemigo_y, velocidad_enemigo):
        self.posX_inicial_enemigo = posX_inicial_enemigo
        self.posY_inicial_enemigo = posY_inicial_enemigo
        self.direccion_enemigo_x = direccion_enemigo_x
        self.direccion_enemigo_y = direccion_enemigo_y
        self.velocidad_enemigo = velocidad_enemigo
        self.color = random.choice(["blue", "red"])
    

    def crear_enemigo(self):
        self.enemigo = tk.Frame(root)
        self.enemigo.config(bg=self.color)
        self.enemigo.place(x=self.posX_inicial_enemigo, y=self.posY_inicial_enemigo, width=self.ancho_enemigo, height=self.alto_enemigo)
        
        self.enemigo.bind("<Button-1>", self.posicion_raton_clic)
        self.enemigo.bind('<B1-Motion>', self.arrastrar_enemigo)
        self.enemigo.bind('<ButtonRelease>', self.enemigo_presionado)


    def posicion_raton_clic(self, event):
        self.enemigo.posX_clic, self.enemigo.posY_clic = event.x, event.y
        self.arrastrar_enemigo(event)


    def arrastrar_enemigo(self, event):
        posX_puntero = root.winfo_pointerx() - root.winfo_rootx()
        posY_puntero = root.winfo_pointery() - root.winfo_rooty()

        #Limite horizontal
        if posX_puntero - self.enemigo.posX_clic > 0 and posX_puntero - self.enemigo.posX_clic + self.ancho_enemigo < ancho_ventana:
            self.enemigo.place(x=posX_puntero - self.enemigo.posX_clic)

        elif self.enemigo.winfo_x() < ancho_ventana and self.enemigo.winfo_x() > ancho_ventana // 2:
            self.enemigo.place(x= ancho_ventana - self.ancho_enemigo)

        elif self.enemigo.winfo_x() > 0 and self.enemigo.winfo_x() < ancho_ventana // 2:
            self.enemigo.place(x= 0)

        #Limite_vertical
        if posY_puntero - self.enemigo.posY_clic > 0 and posY_puntero - self.enemigo.posY_clic + self.alto_enemigo < alto_ventana:
            self.enemigo.place(y=posY_puntero - self.enemigo.posY_clic)
        
        elif self.enemigo.winfo_y() < alto_ventana and self.enemigo.winfo_y() > alto_ventana // 2:
            self.enemigo.place(y= alto_ventana - self.alto_enemigo)

        elif self.enemigo.winfo_y() > 0 and self.enemigo.winfo_y() < alto_ventana // 2:
            self.enemigo.place(y= 0)

        self.arrastrando_enemigo = True
    

    def enemigo_presionado(self, event):
        self.arrastrando_enemigo = False

    def movimiento_enemigo(self):
        #Mueve al enemigo siempre que el jugador no lo este arrastrando
        if not self.arrastrando_enemigo:
            self.enemigo.place(x=self.enemigo.winfo_x() + self.direccion_enemigo_x, y=self.enemigo.winfo_y() + self.direccion_enemigo_y * self.velocidad_enemigo)

        #Cambia la direccion al chocar a la IZQUIERDA
        if self.enemigo.winfo_x() < 0:
            self.direccion_enemigo_x = 1

        #Cambia la direccion al chocar a la DERECHA
        elif self.enemigo.winfo_x() > ancho_ventana - self.ancho_enemigo:
            self.direccion_enemigo_x = -1
            

        #Cambia la direccion al chocar a la ARRIBA
        if self.enemigo.winfo_y() < 0:
            self.direccion_enemigo_y = 1

        #Cambia la direccion al chocar a la ABAJO
        elif self.enemigo.winfo_y() > alto_ventana - self.alto_enemigo:
            self.direccion_enemigo_y = -1



tiempo_spawn = 200
relog = tiempo_spawn

class CrearEnemigo():
    lista_enemigos = []
   
    def crear_enemigos(self):
        cambiar_spawn = random.choice([True, False])
        direccion_x = random.choice([-1,1])

        if cambiar_spawn:
            self.lista_enemigos.append(Enemigo(ancho_ventana // 2 - Enemigo.ancho_enemigo // 2, 0, direccion_x, 1, 1.5))

        else:
            self.lista_enemigos.append(Enemigo(ancho_ventana // 2 - Enemigo.ancho_enemigo // 2, alto_ventana - Enemigo.alto_enemigo, direccion_x, -1, 1.5))

        self.lista_enemigos[-1].crear_enemigo()

    def actualizar_movimientos_enemigos(self):
        for i in self.lista_enemigos:
            i.movimiento_enemigo()

    def spawn_enemigo(self, tiempo_spawn):
        global relog
        relog -= 1
        if relog <= 0:
            relog = tiempo_spawn
            self.crear_enemigos()






#Acualizar movimientos
def update():
    CrearEnemigo().actualizar_movimientos_enemigos()
    CrearEnemigo().spawn_enemigo(tiempo_spawn)  

    root.after(10, update)


CrearEnemigo().crear_enemigos()
root.after(50, update)
root.mainloop()