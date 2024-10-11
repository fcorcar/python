## 26/09/24

#LIBRERIAS
import tkinter as tk
from tkinter import messagebox as MessageBox

#VARIABLES
input_tiempo_usuario = 0
horas = 0
minutos = 0
segundos = 0
temp_activo = False


#FUNCIONES     
def calcular_tiempo():
    global horas, minutos, segundos
    horas = int(input_tiempo_usuario[0:2])
    minutos = int(input_tiempo_usuario[3:5])
    segundos = int(input_tiempo_usuario[6:8])

def comenzar_tiempo():
    global horas, minutos, segundos, temp_activo
    temp_activo = True
    etiqueta.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
    
    if horas == 00 and minutos == 00 and segundos == 00:
        sonar_alarma()
        temp_activo = False
        return
    
    if minutos == 00 and segundos == 00:
        minutos = 60
        horas -= 1
    
    if segundos == 00:
        segundos = 60
        minutos -= 1
        
    segundos -= 1
    ventana.after(1000, comenzar_tiempo)
         
def sonar_alarma():
    MessageBox.showinfo("¡TIEMPO!", "¡¡BEEP!! ¡¡BEEP!!")

def boton_presionado():
    global input_tiempo_usuario
    input_tiempo_usuario = entrada.get()
    calcular_tiempo()
    
    if not temp_activo:
        comenzar_tiempo()
    
    
#GRAFICOS
ventana = tk.Tk()
ventana.title("Temporizador")
ventana.geometry("350x280")
ventana.resizable(False, False)
ventana.config(bg="black")
ventana.attributes("-alpha", 0.9)

frame1 = tk.Frame(ventana)
frame1.config(width=350, height=400, bg="black", bd=10)
frame1.pack(padx=20, pady=20)

etiqueta = tk.Label(frame1, text="00:00:00")
etiqueta.config(fg="white", bg="black", font=("Arial", 45, "bold"))
etiqueta.pack()

entrada = tk.Entry(frame1)
entrada.config(fg="white", bg="black", bd=0, justify="center", font=("Arial", 22))
entrada.insert(0, "01:20:00")
entrada.pack(padx=20, pady=20)

boton = tk.Button(frame1, text="Iniciar", command=boton_presionado)
boton.config(fg="black", bg="white", font=("Arial", 14, "bold"))
boton.pack(padx=10, pady=10, ipadx=10, ipady=2)


#PROGRAMA
ventana.mainloop()