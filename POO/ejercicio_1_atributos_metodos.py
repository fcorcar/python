## 11/10/24

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando.")


nombre = input("Nombre: ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante_1 = Estudiante(nombre, edad, grado)


accion = input("Que quieres hacer: ").lower()
if accion == "estudiar":
    estudiante_1.estudiar()
