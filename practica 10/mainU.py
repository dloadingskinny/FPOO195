from Usuarios import *

NombreU= input("Escribe el nombre de tu usuario: ")
ApellidoP=input("Escribe tu apellido paterno de tu usuario: ")
ApellidoM=input("Escribe tu apellido Materno usuario: ")
correo=input("Escribe el correo de tu usuario: ")
PassU= input("Crea una contraseña: ")

#Creamos el objeto de la clase Usuarios 
Usuarios = Usuarios(NombreU,ApellidoP,ApellidoM,correo,PassU)

#Usamos losatributos de Usuario con sus repectivos getters y setters
Usuarios.setNombre("Nuevo Nombre")
Usuarios.setCorreo("nuevo@correo.com")
print(Usuarios.getNombre())
print(Usuarios.getCorreo())

#Usamos los metodos del Usuario 
Usuarios.CrearUsuario()
Usuarios.EliminarUsuario()
Usuarios.EditarUsuario()
Usuarios.ConsultarUsuario()


