#programa que genere la serie de collatz de un numero entero solicitado de un numero entro solicitado al usuario se sontruye de la siguiente forma:
#si el numero es par se lo divide entre dos;si es impar, se multiplica por tres y se le suma uno;la serie termina al llegar a uno

def numEnt(n): 
  serie = [n]
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n = 3* n + 1
    serie.append(n)
  return serie
n = int(input("Ingrese cualquier numero entero: "))
serie = numEnt(n)
print("nuestra serie de Collatz de {} es: {}".format(n, serie))