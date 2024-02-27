from Personaje import * 
from Armas import * 



#solicitar datos 
nombreS= input("Escribe el nombre de tu Spartan ")
especieS= input("Escribe la especie de tu Spartan ")
alturaS= float(input("Escribe la altura de tu Spartan "))

#solicitar datos de tu nemesis
nombreN= input("Escribe el nombre de tu Nemesis ")
especieN= input("Escribe la especie de tu Nemesis ")
alturaN= float(input("Escribe la altura de tu Nemesis "))

#creamos el objeto para la clase
spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(nombreN,especieN,alturaN)
Arma = Armas()
    
#usamos los tributos Spartan
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#usamos los tributos Nemesis
print(Nemesis.nombre)
print(Nemesis.especie)
print(Nemesis.altura)

#Usamos los metodos del Spartan
spartan.correr(False)
spartan.lanzarGranada()


Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(25)
