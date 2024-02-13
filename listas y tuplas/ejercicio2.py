import random

def llenar_lista():
    return [random.randint(10, 20) for _ in range(30)]

def contar_repetidos(lista):
    return {num: lista.count(num) for num in set(lista)}

def eliminar_repetidos(lista):
    return list(set(lista))

def reemplazar_repetidos_con_cero(lista):
    numeros_unicos = set()
    nueva_lista = []
    for num in lista:
        if num not in numeros_unicos:
            numeros_unicos.add(num)
            nueva_lista.append(num)
        else:
            nueva_lista.append(0)
    return nueva_lista

def main():
    lista = llenar_lista()
    print("Lista generada:", lista)

    while True:
        print("\nMenú:")
        print("a. Contar números repetidos")
        print("b. Eliminar números repetidos")
        print("c. Reemplazar números repetidos con 0")
        print("d. Salir")

        opcion = input("Elige una opción: ")

        if opcion == 'a':
            print("Números repetidos y sus frecuencias:", contar_repetidos(lista))
        elif opcion == 'b':
            print("Lista sin números repetidos:", eliminar_repetidos(lista))
        elif opcion == 'c':
            print("Lista con números repetidos reemplazados por 0:", reemplazar_repetidos_con_cero(lista))
        elif opcion == 'd':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
