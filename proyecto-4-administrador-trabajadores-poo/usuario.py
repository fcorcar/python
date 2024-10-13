class Usuario:
    lista_usuarios = []

    def __init__(self, nombre, passwd):
        self.nombre = nombre
        self.passwd = passwd 

    def crear_usuario(self):
        Usuario.lista_usuarios.append(Usuario(self.nombre, self.passwd))

    def verificar_sesion(self):
        for i in self.lista_usuarios:

            if i.nombre == self.nombre and i.passwd == self.passwd:
                return True, self.nombre
        
        return False, None

                


Usuario("paco", "pepe").crear_usuario()
Usuario("admin", "1234").crear_usuario()


#Usuario("admin", "1234").verificar_sesion()






