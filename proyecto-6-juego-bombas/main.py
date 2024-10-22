import tkinter as tk
import random

has_perdido = False
puntos = 0

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
root.config(bg="gray32")


ancho_casa = ancho_ventana // 5
alto_casa = alto_ventana // 2

posX_casa_izq = 0
posY_casa_izq = alto_ventana // 2 - alto_casa // 2

posX_casa_der = ancho_ventana - ancho_casa
posY_casa_der = alto_ventana // 2 - alto_casa // 2

casa_izq = tk.Frame(root)
casa_izq.config(bg="#ff8a8a", highlightthickness=4, highlightbackground = "red")
casa_izq.place(x=posX_casa_izq, y=posY_casa_izq, width=ancho_casa, height=alto_casa)

casa_der = tk.Frame(root)
casa_der.config(bg="#8ad6ff", highlightthickness=4, highlightbackground = "blue")
casa_der.place(x=posX_casa_der, y=posY_casa_der, width=ancho_casa, height=alto_casa)

etiqueta_puntos = tk.Label(root, text="PUNTOS: 0")
etiqueta_puntos.config(bg="gray32", fg="white", font=("Arial", 22, "bold"))
etiqueta_puntos.place(x=10, y=10)

class Enemigo():
    ancho_enemigo = 55
    alto_enemigo = 55
    arrastrando_enemigo = False
    tiempo_explosion = 10
    
    def __init__(self, posX_inicial_enemigo, posY_inicial_enemigo, direccion_enemigo_x, direccion_enemigo_y, velocidad_enemigo):
        self.posX_inicial_enemigo = posX_inicial_enemigo
        self.posY_inicial_enemigo = posY_inicial_enemigo
        self.direccion_enemigo_x = direccion_enemigo_x
        self.direccion_enemigo_y = direccion_enemigo_y
        self.velocidad_enemigo = velocidad_enemigo
        self.color = random.choice(["blue", "red"])
        self.enemigo_eliminado = False

        self.contador_explosion()
    

    def crear_enemigo(self):
        self.enemigo = tk.Frame(root)
        self.enemigo.config(bg=self.color)
        self.enemigo.place(x=self.posX_inicial_enemigo, y=self.posY_inicial_enemigo, width=self.ancho_enemigo, height=self.alto_enemigo)

        self.enemigo.bind("<Button-1>", self.posicion_raton_clic)
        self.enemigo.bind('<B1-Motion>', self.arrastrar_enemigo)
        self.enemigo.bind('<ButtonRelease>', self.enemigo_soltado)


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
    

    def enemigo_soltado(self, event):
        global has_perdido, puntos
        self.arrastrando_enemigo = False

        #Soltado a la izquierda
        if self.enemigo.winfo_x() >= 0 and self.enemigo.winfo_x() <= ancho_casa - self.ancho_enemigo and self.enemigo.winfo_y() >= posY_casa_izq and self.enemigo.winfo_y() <= posY_casa_izq + alto_casa - self.alto_enemigo:
            
            if self.color == "red":
                self.eliminar_enemigo()
                puntos += 1
                etiqueta_puntos.config(text=f"PUNTOS: {puntos}")
            else:
                print("HAS PERDIDO!!!")
                has_perdido = True

        #Soltado a la derecha
        elif self.enemigo.winfo_x() >= posX_casa_der and self.enemigo.winfo_x() <= ancho_ventana - self.ancho_enemigo and self.enemigo.winfo_y() >= posY_casa_der and self.enemigo.winfo_y() <= posY_casa_der + alto_casa - self.alto_enemigo:
            if self.color == "blue":
                self.eliminar_enemigo()
                puntos += 1
                etiqueta_puntos.config(text=f"PUNTOS: {puntos}")
            else:
                print("HAS PERDIDO!!!")
                has_perdido = True


    def movimiento_enemigo(self):
        #Mueve al enemigo siempre que el jugador no lo este arrastrando
        if not self.arrastrando_enemigo:
            self.enemigo.place(x=self.enemigo.winfo_x() + self.direccion_enemigo_x, y=self.enemigo.winfo_y() + self.direccion_enemigo_y * self.velocidad_enemigo)

        #Cambia la direccion al chocar a la IZQUIERDA
        if self.enemigo.winfo_x() < ancho_casa:
            self.direccion_enemigo_x = 1

        #Cambia la direccion al chocar a la DERECHA
        elif self.enemigo.winfo_x() > ancho_ventana - self.ancho_enemigo - ancho_casa:
            self.direccion_enemigo_x = -1
            

        #Cambia la direccion al chocar a la ARRIBA
        if self.enemigo.winfo_y() < 0:
            self.direccion_enemigo_y = 1

        #Cambia la direccion al chocar a la ABAJO
        elif self.enemigo.winfo_y() > alto_ventana - self.alto_enemigo:
            self.direccion_enemigo_y = -1

    def eliminar_enemigo(self):
        self.enemigo_eliminado = True
        self.enemigo.destroy()
        lista_enemigos.remove(self)


    def contador_explosion(self):
        global has_perdido

        self.tiempo_explosion -= 1

        if self.tiempo_explosion == 5:
            self.animacion()

        if self.tiempo_explosion <= 0:
            print("HAS PERDIDO!!!")
            has_perdido = True
        
        if not has_perdido and not self.enemigo_eliminado:
            root.after(1000, self.contador_explosion)

    
    def animacion(self):
        if not self.enemigo_eliminado and not has_perdido:
            if self.enemigo.cget('bg') == self.color:
                self.enemigo.config(bg="white")
            
            else:
                self.enemigo.config(bg=self.color)

            root.after(500, self.animacion)










lista_enemigos = []
tiempo_spawn = 200
relog = tiempo_spawn
spawn_anterior = direccion_anterior = None

class CrearEnemigo():
    
    def crear_enemigos(self):
        global spawn_anterior, direccion_anterior
        cambiar_spawn = random.choice([True, False])
        direccion_x = random.choice([-1,1])

        if cambiar_spawn == spawn_anterior and direccion_x == direccion_anterior:
            if direccion_x == -1:
                direccion_x = 1
            else:
                direccion_x = -1

        spawn_anterior = cambiar_spawn
        direccion_anterior = direccion_x

        if cambiar_spawn:
            lista_enemigos.append(Enemigo(ancho_ventana // 2 - Enemigo.ancho_enemigo // 2, 0, direccion_x, 1, 1.5))

        else:
            lista_enemigos.append(Enemigo(ancho_ventana // 2 - Enemigo.ancho_enemigo // 2, alto_ventana - Enemigo.alto_enemigo, direccion_x, -1, 1.5))

        lista_enemigos[-1].crear_enemigo()

    def actualizar_movimientos_enemigos(self):
        for i in lista_enemigos:
            i.movimiento_enemigo()

    def spawn_enemigo(self, t_spawn):
        global relog, tiempo_spawn
        relog -= 1
        
        if relog <= 0:
            relog = t_spawn
            if tiempo_spawn <= 180: ##MOD
                self.crear_enemigos()
                self.crear_enemigos()
            else:
                self.crear_enemigos()
            
            if tiempo_spawn >= 140:
                tiempo_spawn -= 2

            print(tiempo_spawn)






#Acualizar movimientos
def update():
    if not has_perdido:
        CrearEnemigo().actualizar_movimientos_enemigos()
        CrearEnemigo().spawn_enemigo(tiempo_spawn)  

    root.after(10, update)


CrearEnemigo().crear_enemigos()
root.after(50, update)
root.mainloop()