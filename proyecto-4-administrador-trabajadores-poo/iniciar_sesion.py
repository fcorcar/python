import tkinter as tk
from PIL import ImageTk, Image
import usuario
import menu



class Login():
    def __init__(self):

        #####################################################################
        # --------------------- CONFIGURACION VENTANA --------------------- #
        #####################################################################

        self.root = tk.Tk()
        self.root.title("Iniciar Sesión")

        self.ancho_ventana = 450
        self.alto_ventana = 550

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

        self.imagen_login = Image.open("./images/logo_login.png")
        self.imagen_login = self.imagen_login.resize((390, 250))
        self.img_login = ImageTk.PhotoImage(self.imagen_login)

        self.etiqueta_logo = tk.Label(self.frame1, image=self.img_login)
        self.etiqueta_logo.config(bg="gray85")
        self.etiqueta_logo.place(x=4, y=-45)


        #####################################################################
        # ----------------------------- FRAME2 ---------------------------- #
        #####################################################################

        self.frame2 = tk.Frame(self.root)
        self.frame2.config(bg="white")
        self.frame2.place(x=25, y=210, width=400, height=315)

        self.etiqueta_usuario = tk.Label(self.frame2, text="Nombre de usuario")
        self.etiqueta_usuario.config(bg="white", font=("Arial", 15, "bold"))
        self.etiqueta_usuario.place(x=25, y=25)

        self.entrada_usuario = tk.Entry(self.frame2)
        self.entrada_usuario.config(bg="white", font=("Arial", 15), relief="flat")
        self.entrada_usuario.place(x=25, y=55, width=350, height=40)
        self.entrada_usuario.bind('<Return>', self.tecla_enter_pulsada)

        self.etiqueta_passwd = tk.Label(self.frame2, text="Contraseña")
        self.etiqueta_passwd.config(bg="white", font=("Arial", 15, "bold"))
        self.etiqueta_passwd.place(x=25, y=110)

        self.entrada_passwd = tk.Entry(self.frame2, show="*")
        self.entrada_passwd.config(bg="white", font=("Arial", 15), relief="flat")
        self.entrada_passwd.place(x=25, y=140, width=350, height=40)
        self.entrada_passwd.bind('<Return>', self.tecla_enter_pulsada)

        self.boton_acceder = tk.Button(self.frame2, text="Acceder", command=self.iniciar_sesion)
        self.boton_acceder.config(bg="black", fg="white", font=("Arial", 14, "bold"))
        self.boton_acceder.place(x=25, y=200, width=350, height=50)
        self.boton_acceder.bind('<Return>', self.tecla_enter_pulsada)

        self.etiqueta_verificacion = tk.Label(self.frame2)
        self.etiqueta_verificacion.config(bg="white", font=("Arial", 12))
        self.etiqueta_verificacion.place(x=25, y=265)

        #####################################################################
        # -------------------------- FRAME DISEÑO ------------------------- #
        #####################################################################

        self.frame_estilo1 = tk.Frame(self.root)
        self.frame_estilo1.config(bg="black")
        self.frame_estilo1.place(x=25, y=520, width=400, height=5)

        self.root.mainloop()

    def tecla_enter_pulsada(self, event):
        Login.iniciar_sesion(self)

    def iniciar_sesion(self):
        user = self.entrada_usuario.get()
        passwd = self.entrada_passwd.get()
        usuario_passwd_correcto, nombre_usuario = usuario.Usuario(user, passwd).verificar_sesion()

        if user == "" or passwd == "":
            self.etiqueta_verificacion.config(text="Introduce un nombre de usuario y contraseña.", fg="red")
        
        elif usuario_passwd_correcto: #Accion a realizar si es correcto el usuario y contraseña
            self.etiqueta_verificacion.config(text="Sesion iniciada.", fg="green")
            self.root.destroy()
            menu.Menu(nombre_usuario)
        
        else:
            self.etiqueta_verificacion.config(text="Nombre de usuario o contraseña incorrectos.", fg="red")


