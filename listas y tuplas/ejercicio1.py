def suma(tupla):
    return sum(tupla)

def maximo(tupla):
    return max(tupla)

def minimo(tupla):
    return min(tupla)

def promedio(tupla):
    return sum(tupla) / len(tupla)

def moda(tupla):
    return max(set(tupla), key=tupla.count)

def rango(tupla):
    return max(tupla) - min(tupla)

def main():
    numeros = tuple(map(float, input("Ingrese los números separados por espacios: ").split()))

    print("\nMenú funcional:")
    print("1. Sumatoria de los elementos de la lista")
    print("2. Numero mayor de la lista")
    print("3. Numero menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        print("Sumatoria de los elementos de la lista:", suma(numeros))
    elif opcion == '2':
        print("Numero mayor de la lista:", maximo(numeros))
    elif opcion == '3':
        print("Numero menor de la lista:", minimo(numeros))
    elif opcion == '4':
        print("Promedio de los elementos de la lista:", promedio(numeros))
    elif opcion == '5':
        print("Moda de la lista:", moda(numeros))
    elif opcion == '6':
        print("Rango de la lista:", rango(numeros))
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
