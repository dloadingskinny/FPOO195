class Personaje:
    
    #atributos de poersonaje 
    def __init__(self,nom,esp,alt) :   
        self.nombre = nom
        self.especie = esp
        self.altura= alt
    
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