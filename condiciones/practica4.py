#1
passGuardada = input( "Ingresa una contraseña: ")

passUsuario = input("Introduce tu contraseña: ")

if passGuardada.lower() == passUsuario.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo.")

#2
"""numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    print(numero," es par.")
else:
    print(numero," es impar.")"""
#3
"""edad = int(input("Ingresa la edad del cliente: "))

if edad < 4:
    PEntrada = 0  
elif 4 <= edad <= 18:
    PEntrada = 110  
else:
    PEntrada = 190  

print("El precio de la entrada es: $ ", PEntrada)"""

#4
"""cadena = input("Ingresa una cadena de caracteres: ")

cadenaProcesada = cadena.replace(" ", "").lower()

if cadenaProcesada == cadenaProcesada[::-1]:
    print(cadena, "es palíndromo.")
else:
    print(cadena, "no es palíndromo.")
"""