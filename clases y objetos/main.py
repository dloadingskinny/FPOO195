from Personaje import * 
from Armas import * 

spartan = Personaje()
Arma = Armas()
    
print(spartan.nombre)
print(spartan.nombre)
print(spartan.nombre)
print(spartan.nombre)
#usamos los tributos Spartan
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Usamos los metodos del Spartan
spartan.correr(False)
spartan.lanzarGranada()


Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(25)
