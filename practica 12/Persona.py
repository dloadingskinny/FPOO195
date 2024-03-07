class Persona:
    # Constructor
    def __init__(self):
        self.__listaBD = []

    # Métodos del CRUD
    def Insertar(self, id, nom, edad):
        self.__listaBD.append({"id": id, "Nombre": nom, "Edad": edad})

    def ConsultarTodos(self):
        print(self.__listaBD)

    def buscarUsuario(self, id):
        encontrado = False
        for usuario in self.__listaBD:
            if usuario['id'] == id:
                print(usuario)
                encontrado = True
                break
        if not encontrado:
            print("Usuario no encontrado")

    def eliminar(self, id):
        for usuario in self.__listaBD:
            if usuario['id'] == id:
                self.__listaBD.remove(usuario)
                print("Usuario eliminado")
                break
        else:
            print("Usuario no encontrado")

    def editar(self, id, nom, edad):
        for usuario in self.__listaBD:
            if usuario['id'] == id:
                usuario['Nombre'] = nom
                usuario['Edad'] = edad
                print("Usuario editado")
                break
        else:
            print("Usuario no encontrado")
