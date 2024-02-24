import random

def gen_lista():
    return [random.randint(10, 20) for _ in range(30)]

def contar_rep(lst):
    return {num: lst.count(num) for num in set(lst)}

def elim_rep(lst):
    return list(set(lst))

def reemplazar_con_0(lst):
    unicos = set()
    nueva_lst = []
    for num in lst:
        if num not in unicos:
            unicos.add(num)
            nueva_lst.append(num)
        else:
            nueva_lst.append(0)
    return nueva_lst

def main():
    lst = gen_lista()
    print("Lista generada:", lst)

    while True:
        print("\nMenú:")
        print("a. Contar números repetidos")
        print("b. Eliminar números repetidos")
        print("c. Reemplazar números repetidos con 0")
        print("d. Salir")

        opcion = input("Elige una opción: ")

        if opcion == 'a':
            print("Números repetidos y sus frecuencias:", contar_rep(lst))
        elif opcion == 'b':
            print("Lista sin números repetidos:", elim_rep(lst))
        elif opcion == 'c':
            print("Lista con números repetidos reemplazados por 0:", reemplazar_con_0(lst))
        elif opcion == 'd':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
