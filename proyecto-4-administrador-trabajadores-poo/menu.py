import tkinter as tk
import iniciar_sesion

class Menu():
    def __init__(self, nombre_usuario):

        self.nombre_usuario = nombre_usuario

        #####################################################################
        # --------------------- CONFIGURACION VENTANA --------------------- #
        #####################################################################

        self.root = tk.Tk()
        self.root.title("Menu Principal")

        self.ancho_ventana = 550
        self.alto_ventana = 650

        self.x_ventana = self.root.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.root.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = str(self.ancho_ventana) + "x" + str(self.alto_ventana) + "+" + str(self.x_ventana) + "+" + str(self.y_ventana)

        self.root.geometry(self.posicion)
        self.root.resizable(False, False)
        self.root.config(bg="gray85")


        #####################################################################
        # ----------------------------- FRAME1 ---------------------------- #
        #####################################################################

        self.frame1 = tk.Frame(self.root)
        self.frame1.config(bg="gray85")
        self.frame1.place(x=25, y=25, width=400, height=160)



        #####################################################################
        # ----------------------------- FRAME2 ---------------------------- #
        #####################################################################

        self.frame2 = tk.Frame(self.root)
        self.frame2.config(bg="white")
        self.frame2.place(x=25, y=210, width=400, height=315)

        self.etiqueta_usuario = tk.Label(self.frame2, text=f"Bienvenido {self.nombre_usuario.capitalize()}.")
        self.etiqueta_usuario.config(bg="white", font=("Arial", 22, "bold"))
        self.etiqueta_usuario.place(x=25, y=25)

        self.boton_cerrar_sesion = tk.Button(self.frame2, text="Cerrar sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.config(bg="black", fg="white", font=("Arial", 14, "bold"))
        self.boton_cerrar_sesion.place(x=25, y=200, width=350, height=50)
        #self.boton_cerrar_sesion.bind('<Return>', self.tecla_enter_pulsada)


        self.root.mainloop()

    
    def cerrar_sesion(self):
        self.root.destroy()
        iniciar_sesion.Login()
        


