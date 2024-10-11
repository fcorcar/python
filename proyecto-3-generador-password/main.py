## 10/10/24

## LIBRERIAS
import string
import random
import tkinter as tk
import os


## VARIABLES
esMasDe512 = False
longitud_maxima_pass = 512 # AJUSTABLE
longitud_minima_pass = 1
logitud_por_defecto = 16 # AJUSTABLE

conjunto = []
abecedario_low = string.ascii_lowercase
abecedario_up = string.ascii_uppercase
caracteres_especiales = string.punctuation
numeros = string.digits

longitud_pass = 0
password_generada = ""


## FUNCIONES
def generar_password():
    global conjunto, longitud_pass, password_generada

    conjunto.clear()
    longitud_pass = int(entrada_longitud.get())
    password_generada = ""

    if abecedario_min_bool.get():
        conjunto.append(abecedario_low)

    if abecedario_max_bool.get():
        conjunto.append(abecedario_up)

    if numeros_bool.get():
        conjunto.append(numeros)

    if caracteres_especiales_bool.get():
        conjunto.append(caracteres_especiales)

    
    for i in range(longitud_pass):
        grupos = random.randint(0,len(conjunto)-1)
        password_generada += random.choice(conjunto[grupos])
    
    resultado_pass.config(text=password_generada)
    

def verificar_input(input): #Verifica la entrada por teclado. Si es True permite la entrada, si es False no.
    global esMasDe512

    if input.isdigit(): #Si es un numero permite la entrada
        if int(input) < longitud_minima_pass: return False #No permite escribir menos de "longitud_minima_pass"
        if int(input) > longitud_maxima_pass: #Si es mas de "longitud_maxima_pass" no lo permite y activa el bool para sobreescribir la caja de texto
            esMasDe512 = True
            return False
        return True
                          
    elif input == "": #Permite estar en blanco (Luego "reescribir_imput()" lo sustiye por "longitud_minima_pass")
        return True
  
    else: #Si no son numeros no permite introducirlos
        return False


def reescribir_input(e): #Sustituye el texto de la caja de texto por el adecuado.
    global esMasDe512
    input = entrada_longitud.get()
                          
    if input == "": #Si esta vacio lo cambia por "longitud_minima_pass". Ej: 8
        entrada_longitud.delete(0, tk.END)
        entrada_longitud.insert(0, longitud_minima_pass)
    
    elif esMasDe512: #Si es mas de "longitud_maxima_pass", establece el maximo
        esMasDe512 = False
        entrada_longitud.delete(0, tk.END)
        entrada_longitud.insert(0, longitud_maxima_pass)


def establecer_input_botones(input_boton): #Establece la longitud mediante los botones
    valor_entrada = int(entrada_longitud.get()) #Obtiene la longitud de la caja de texto

    valor_entrada += input_boton #Suma o resta la longitud

    if valor_entrada <= longitud_minima_pass: valor_entrada = longitud_minima_pass #Establece un limite minimo
    if valor_entrada >= longitud_maxima_pass: valor_entrada = longitud_maxima_pass #Establece un limite maximo

    entrada_longitud.delete(0, tk.END) #Elimina el valor en el widget
    entrada_longitud.insert(0, valor_entrada) #Establece el nuevo valor en el widget


def habilitar_caracteres():
    contador = 0

    if abecedario_min_bool.get(): contador += 1

    if abecedario_max_bool.get(): contador += 1

    if numeros_bool.get(): contador += 1

    if caracteres_especiales_bool.get(): contador += 1

    if contador == 1:
        if abecedario_min_bool.get():
            check_abecedario_min.config(state="disabled")

        elif abecedario_max_bool.get():
            check_abecedario_max.config(state="disabled")

        elif numeros_bool.get():
            check_numeros.config(state="disabled")

        elif caracteres_especiales_bool.get():
            check_caracteres_especiales.config(state="disabled")
    
    else:
        check_abecedario_min.config(state="normal")
        check_abecedario_max.config(state="normal")
        check_numeros.config(state="normal")
        check_caracteres_especiales.config(state="normal")


## GRAFICOS
ventana = tk.Tk()
ventana.title("Generados de contraseñas")
ventana.geometry("896x324")
ventana.resizable(False, False)
ventana.config(bg="gray63")

frame0 = tk.Frame(ventana, highlightthickness=3)
frame0.config(bg="gray85", highlightbackground = "gray63")
frame0.place(x=22, y=22, width=852, height=280)

# Frame 1 
frame1 = tk.Frame(ventana)
frame1.config(bg="gray85")
frame1.place(x=25, y=25, width=846, height=122)

entrada_longitud = tk.Entry(frame1, validate="key", validatecommand=(ventana.register(verificar_input), "%P"))
entrada_longitud.config(fg="white", bg="black", justify="center", font=("Arial", 22))
entrada_longitud.insert(0, logitud_por_defecto)
entrada_longitud.place(x=25, y=25, width=90, height=72)
entrada_longitud.bind("<KeyRelease>", reescribir_input)

boton_mas_logitud = tk.Button(frame1, text="⬆️", command= lambda: establecer_input_botones(1))
boton_mas_logitud.config(bg="black", fg="white", font=("Arial", 16))
boton_mas_logitud.place(x=118, y=25, width=30, height=34)

boton_menos_longitud = tk.Button(frame1, text="⬇️", command= lambda: establecer_input_botones(-1))
boton_menos_longitud.config(bg="black", fg="white", font=("Arial", 16))
boton_menos_longitud.place(x=118, y=63, width=30, height=34)

resultado_pass = tk.Label(frame1, text="B^Cf7w6eB^Cf7w6e")
resultado_pass.config(fg="black", bg="white", font=("Arial", 22))
resultado_pass.place(x=173, y=25, width=500, height=72)

boton_copiar = tk.Button(frame1, text="Copiar", command= lambda: os.system("echo '{}' | xclip -selection clipboard".format(password_generada)))
boton_copiar.config(bg="black", fg="white", font=("Arial", 18))
boton_copiar.place(x=698, y=25, width=123, height=72)

# Frame 2
frame2 = tk.Frame(ventana)
frame2.config(bg="gray85")
frame2.place(x=185, y=147, width=525, height=65)

abecedario_min_bool = tk.BooleanVar()
check_abecedario_min = tk.Checkbutton(frame2, text="a - z", variable=abecedario_min_bool, command=habilitar_caracteres)
check_abecedario_min.config(font=("Arial", 18), bg="gray85", activebackground="gray85", relief="flat")
check_abecedario_min.place(x=25, y=0, width=100, height=40)

abecedario_max_bool = tk.BooleanVar()
check_abecedario_max = tk.Checkbutton(frame2, text="A - Z", variable=abecedario_max_bool, command=habilitar_caracteres)
check_abecedario_max.select()
check_abecedario_max.config(font=("Arial", 18), bg="gray85", activebackground="gray85", relief="flat")
check_abecedario_max.place(x=150, y=0, width=100, height=40)

numeros_bool = tk.BooleanVar()
check_numeros = tk.Checkbutton(frame2, text="0 - 9", variable=numeros_bool, command=habilitar_caracteres)
check_numeros.select()
check_numeros.config(font=("Arial", 18), bg="gray85", activebackground="gray85", relief="flat")
check_numeros.place(x=275, y=0, width=100, height=40)

caracteres_especiales_bool = tk.BooleanVar()
check_caracteres_especiales = tk.Checkbutton(frame2, text="@ - ?", variable=caracteres_especiales_bool, command=habilitar_caracteres)
check_caracteres_especiales.config(font=("Arial", 18), bg="gray85", activebackground="gray85", relief="flat")
check_caracteres_especiales.place(x=400, y=0, width=100, height=40)

# Frame 3
frame3 = tk.Frame(ventana)
frame3.config(bg="gray85")
frame3.place(x=292, y=212, width=310, height=87)

boton_generar_pass = tk.Button(frame3, text="Generar contraseña", command=generar_password)
boton_generar_pass.config(bg="black", fg="white", font=("Arial", 18))
boton_generar_pass.place(x=25, y=0, width=260, height=62)




#PROGRAMA
generar_password()
ventana.mainloop()