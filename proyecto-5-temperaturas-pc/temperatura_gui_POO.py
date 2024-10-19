import tkinter as tk
import psutil

NOMBRE_GPU, NOMBRE_CPU = psutil.sensors_temperatures().keys()
diccionario_colores = {}
r = 255
g = 0
b = 0


class Temperatura():

    def __init__(self, nombre_componente_dic, etiqueta, componente):
        self.temperatura = psutil.sensors_temperatures()[nombre_componente_dic][0].current
        self.etiqueta = etiqueta 
        self.componente = componente

    def actualizar_datos(self):

        self.etiqueta.config(text=f"{self.componente}: {self.temperatura:.1f} ºC")

        for i in diccionario_colores:
            i_float = float(i)

            if self.temperatura >= i_float:
                self.etiqueta.config(bg=diccionario_colores[i])
                break


class RangoColor():

    def __init__(self, valor_color_pri, nombre_color_pri, operador, max, min):  #(variable r,g,b ,, -13,13)    #-r 
        self.valor_color_pri = valor_color_pri
        self.nombre_color_pri = nombre_color_pri
        self.operador = operador
        self.max = max
        self.min = min

    def crear_rango(self):
        global diccionario_colores, r, g, b

        for i in range(self.max, self.min, -1):

            diccionario_colores[i] = '#%02x%02x%02x' % (r, g, b) 

            self.valor_color_pri += self.operador

            if self.valor_color_pri > 255:
                self.valor_color_pri = 255

            elif self.valor_color_pri < 0:
                self.valor_color_pri = 0

            if self.nombre_color_pri == "r": r = self.valor_color_pri
            elif self.nombre_color_pri == "g": g = self.valor_color_pri
            elif self.nombre_color_pri == "b": b = self.valor_color_pri


def crear_ventana(): 
    root = tk.Tk()
    root.title("Monitor de Temperatura")
    root.geometry("300x205")
    root.resizable(False, False)
    root.config(bg="gray55")

    frame1 = tk.Frame(root)
    frame1.config(bg="gray10")
    frame1.place(x=25, y=25, width=250, height=155)

    etiqueta_cpu = tk.Label(frame1, text="CPU: 20.23ºC")
    etiqueta_cpu.config(bg="green", fg="gray10", font=("Arial", 20, "bold"))
    etiqueta_cpu.place(x=25, y=25, width=200, height=40)

    etiqueta_gpu = tk.Label(frame1, text="GPU: 20.23ºC")
    etiqueta_gpu.config(bg="green", fg="gray10", font=("Arial", 20, "bold"))
    etiqueta_gpu.place(x=25, y=90, width=200, height=40)

    def actualizar():
        Temperatura(NOMBRE_CPU, etiqueta_cpu, "CPU").actualizar_datos()
        Temperatura(NOMBRE_GPU, etiqueta_gpu, "GPU").actualizar_datos()
        root.after(100, actualizar)

    actualizar()
    root.mainloop()


RangoColor(g, "g", 13, 60, 40).crear_rango() #valor, nombre, restaosuma, intervalo_max, intervalo_min
RangoColor(r, "r", -13, 40, 20).crear_rango()
RangoColor(b, "b", 13, 20, -1).crear_rango()
crear_ventana()








    
    









    




