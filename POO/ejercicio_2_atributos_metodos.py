## 11/10/24

class Persona:
    def __init__(self, nombre, edad:int):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
        print(f"Es el cumple años de {self.nombre}. Hoy cumple {self.edad}.")

    def mostrar_datos(self):
        print(f"""
        DATOS DE {self.nombre.upper()}:
        Nombre: {self.nombre}
        Edad: {self.edad}
        """)

lista_objetos = []

lista_objetos.append(Persona("Juan", 22))
lista_objetos.append(Persona("Jose", 42))
lista_objetos.append(Persona("Luis", 35))


for i in lista_objetos:

    i.mostrar_datos()