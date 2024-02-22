class Personaje:
    
    #atributos de poersonaje 
    especie= "Humano"
    nombre="John"
    alruta=2.18
    
    #metodos del personaje
    def correr(self,estado):
        if(estado):
            print("El personaje "+ self.nombre+" esta corriendo")
        else:
            print("El personaje "+ self.nombre+" esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre+" pego una Granada")
        
    def recargarArma(self, municion):
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada al "+ str(cargador)+"%")
 
 #creamos el objeto de la clase de personaje       
spartan = Personaje()

print(spartan.nombre)
print(spartan.nombre)
print(spartan.nombre)
print(spartan.nombre)
        