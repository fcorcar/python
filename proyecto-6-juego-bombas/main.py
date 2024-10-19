import tkinter as tk
import random

ancho_ventana = 900
alto_ventana = 500

ancho_enemigo = 40
alto_enemigo = 40
posX_inicial_enemigo = ancho_ventana // 2 - ancho_enemigo
posY_inicial_enemigo = alto_ventana // 2 - alto_enemigo

moviendo_enemigo = False
tiempo = 0
mover_enX = 0
mover_enY = 1

def posicion_raton_clic(event):
    enemigo.posX_clic, enemigo.posY_clic = event.x, event.y
    mover_enemigo(event)

def mover_enemigo(event):
    global moviendo_enemigo
    posX_puntero = root.winfo_pointerx() - root.winfo_rootx()
    posY_puntero = root.winfo_pointery() - root.winfo_rooty()

    #Limite horizontal
    if posX_puntero - enemigo.posX_clic > 0 and posX_puntero - enemigo.posX_clic + ancho_enemigo < ancho_ventana:
        enemigo.place(x= enemigo.winfo_x() - enemigo.posX_clic + event.x)
        moviendo_enemigo = True

    elif enemigo.winfo_x() < ancho_ventana and enemigo.winfo_x() > ancho_ventana // 2:
        enemigo.place(x= ancho_ventana - ancho_enemigo)

    elif enemigo.winfo_x() > 0 and enemigo.winfo_x() < ancho_ventana // 2:
        enemigo.place(x= 0)

    #Limite_vertical
    if posY_puntero - enemigo.posY_clic > 0 and posY_puntero - enemigo.posY_clic + alto_enemigo < alto_ventana:
        enemigo.place(y= enemigo.winfo_y() - enemigo.posY_clic + event.y)
        moviendo_enemigo = True
    
    elif enemigo.winfo_y() < alto_ventana and enemigo.winfo_y() > alto_ventana // 2:
        enemigo.place(y= alto_ventana - alto_enemigo)

    elif enemigo.winfo_y() > 0 and enemigo.winfo_y() < alto_ventana // 2:
        enemigo.place(y= 0)


    

def presionado(self):
    global moviendo_enemigo
    moviendo_enemigo = False


def comprobar_limiteX():
    if enemigo.winfo_x() > 0 and enemigo.winfo_x() + ancho_enemigo < ancho_ventana:
        return True

    else:
        return False
    
def comprobar_limiteY():
    if enemigo.winfo_y() > 0 and enemigo.winfo_y() + alto_enemigo < alto_ventana:
        return True

    else:
        return False


def movimiento_enemigo():
    global tiempo, mover_enX, mover_enY

    tiempo += 1
    if tiempo >= 20:
        tiempo = 0
        mover_enX = random.choice([-1,1])
        mover_enY = random.choice([-1,1])

        print(f"x:{mover_enX}, y:{mover_enY}")


    if comprobar_limiteX() and not moviendo_enemigo:
        enemigo.place(x=enemigo.winfo_x() + mover_enX)

    elif enemigo.winfo_x() == 0 and not moviendo_enemigo:
            enemigo.place(x=enemigo.winfo_x() + 1)

    elif enemigo.winfo_x() == ancho_ventana - ancho_enemigo and not moviendo_enemigo:
            enemigo.place(x=enemigo.winfo_x() + -1)

    
    if comprobar_limiteY() and not moviendo_enemigo:
        enemigo.place(y=enemigo.winfo_y() + mover_enY)

    elif enemigo.winfo_y() == 0 and not moviendo_enemigo:
            enemigo.place(y=enemigo.winfo_y() + 1)

    elif enemigo.winfo_y() == alto_ventana - alto_enemigo and not moviendo_enemigo:
            enemigo.place(y=enemigo.winfo_y() + -1)




    


    




root = tk.Tk()
root.title("Juego")
x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
resolucion_ventana = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(resolucion_ventana)
root.resizable(False, False)

enemigo = tk.Frame(root)
enemigo.config(bg="red")



enemigo.bind("<Button-1>", posicion_raton_clic)
enemigo.bind('<B1-Motion>', mover_enemigo)

enemigo.bind('<ButtonRelease>', presionado)




def upd():
    movimiento_enemigo()

    root.after(10, upd)

upd()




enemigo.place(x=posX_inicial_enemigo, y=posY_inicial_enemigo, width=ancho_enemigo, height=alto_enemigo)


root.mainloop()