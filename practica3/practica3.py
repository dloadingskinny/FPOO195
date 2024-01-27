#1
"""var1=(int(input("¿cuantas horas trabajaste?")))
T1= "El coste de hora es de 100"
b=100 * var1
print(T1)
print("se te pagara",b)"""

#2 
nombre = input("Introduce tu nombre completo: ")

print("En minúsculas:", nombre.lower())
print("En mayúsculas:", nombre.upper())
print("Primera letra en mayúscula:", nombre.title())

#3
x = int(input("Introduce un número entero X: "))
suma = sum(range(1, x + 1))
print("La suma de todos los enteros desde 1 hasta", x, "es:", suma)
#4
n = input("Introduce tu nombre: ")

n_upper = n.upper()
n_letras = len(n)

print(f"{n_upper} tiene {n_letras} letras.")

#5
p = int(input("Número de payasos vendidos: "))
m = int(input("Número de muñecas vendidas: "))

pp = 112  
pm = 75   

pt = (p * pp) + (m * pm)

print(f"Peso total del paquete: {pt} g")

#6
frase = input("Introduce una frase: ")

frase_invertida = frase[::-1]

print("Frase invertida:", frase_invertida)

