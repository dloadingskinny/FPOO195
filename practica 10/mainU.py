import sys
from Persona import Persona

objectPeople = Persona()

while True:
    print("Menu")
    print("1. Insertar Persona")
    print("2. Consultar todos")
    print("3. Buscar una Persona")
    print("4. Eliminar una Persona")
    print("5. Editar una Persona")
    print("6. Salir")
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        print("Ingresa los datos del usuario:")
        id = input("Escribe el Id: ")
        nom = input("Escribe el nombre: ")
        eda = input("Escribe la edad: ")
        objectPeople.Insertar(id, nom, eda)
        print("Persona agregada correctamente")
        
    elif opcion == "2":
        print("Estas son las personas guardadas:")
        objectPeople.ConsultarTodos()
        
    elif opcion == "3":
        id = input("Escribe el ID a buscar: ")
        objectPeople.buscarUsuario(id)
        
    elif opcion == "4":
        id = input("Introduce ID de la persona a eliminar: ")
        objectPeople.eliminar(id)
        
    elif opcion == "5":
        id = input("Introduce ID de la persona a editar: ")
        nom = input("Nuevo nombre: ")
        eda = input("Nueva edad: ")
        objectPeople.editar(id, nom, eda)
        
    elif opcion == "6":
        print("Hasta luego")
        sys.exit()
        
    else:
        print("Opción no válida. Intenta de nuevo")

        

