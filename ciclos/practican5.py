# #1
# num = int(input("Ingrese un número entero positivo: "))
# if num < 1:
#     print("Por favor, ingrese un número entero positivo.")
# else:
#     impares = [str(i) for i in range(1, num + 1, 2)]
#     resultado = ', '.join(impares)
#     print("Números impares " , num , resultado)

#2
# num=int(input("Ingresa un numero entero positivo: "))
# if num > 1:
#     cuenta_atras = ', '.join(map(str, range(num, -1, -1)))
#     print("Cuenta atrás:", cuenta_atras)

#3
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")

#4
# altura = int(input("Introduce la altura del triángulo: "))

# for i in range(1, altura + 1):
#     print("*" * i)

#5
# frase = input("Introduce una frase: ")
# letra = input("Introduce una letra: ")

# contador = frase.count(letra)
# print(f"La letra '{letra}' aparece {contador} veces en la frase.")

#6
saldo = 0

while True:
    operacion = input("Introduce una operación (D para depósito, R para retiro, o deja vacío para finalizar): ")
    
    if not operacion:
        break
    
    cantidad = float(input("Introduce la cantidad: "))
    
    if operacion == "D":
        saldo += cantidad
    elif operacion == "R":
        saldo -= cantidad

print(f"Saldo final: {saldo}")

#7
altura_base = int(input("Introduce la cantidad de * de la base: "))

for i in range(1, altura_base + 1):
    espacios = " " * (altura_base - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
