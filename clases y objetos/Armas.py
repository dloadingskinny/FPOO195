class Armas:
    
    def seleccionarArma(self, nombre):
        seleccion = int(input("Selecciona el arma \n 1= Rifle de asalt \n 2= Espada energia \n 3= Rifle M392"))
        
        if(seleccion == 1):
            print("Rifle de asalto asignado a "+ nombre)
            print("municiones 7.62 * 52mm; sin mira")
        
        if(seleccion == 2):
            print("Espada de energia asignado a "+ nombre)
            print("Arma creada por los Shagheili")
        
        if(seleccion == 3):
            print("Rfle M392 asignado a "+ nombre)
            print("municiones 7.62 * 52mm; sin mira")
   
    def recargarArma(self, municion):
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada al "+ str(cargador)+"%")   