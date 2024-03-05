#Creal clase Usuarios para hacer un CRUD
class Usuarios:
    
    def _init_(self,nom,ApeP,ApeM,Corr,Pass):
        self.__Nombre = nom
        self.__ApellidoPaterno = ApeP
        self.__ApellidoMaterno = ApeM
        self.__correo = Corr
        self.__Contraseña = Pass
        
    def CrearUsuario(self,estado):
        if(estado):
            print('Usuario creado')
        else:
            print('Usuario no creado')
    
    def EliminarUsuario(self,estado):
        if(estado):
            print('Usuario eliminado')
        else:
            print('Usuario no eliminado')

    def EditarUsuario(self,estado):
        if(estado):
            print('Usuario editado')
        else:
            print('Usuario no editado')

    def ConsultarUsuario(self,estado):
        if(estado):
            print('Usuario consultado')
        else:
            print('Usuario no consultado')

            
#getters
    def getNombre(self):
        return self.__Nombre
    
    def getApellidoPaterno(self):
        return self.__ApellidoPaterno
    
    def getApellidoMaterno(self):
        return self.__ApellidoMaterno
    
    def getCorreo(self):
        return self.__correo
    
    def getContraseña(self):
        return self.__Contraseña
    
#setters
def setNombre(self, nom):
    self.__Nombre = nom
def setApellidoPaterno(self, ApeP):
    self.__ApellidoPaterno = ApeP
def setApellidoMaterno(self, ApeM):
    self.__ApellidoMaterno = ApeM
def setCorreo(self, Corr):
    self.__correo = Corr
def setContraseña(self, Pass):
    self.__Contraseña = Pass






        

        
    



