#escribe un programa que pida al usuario dos palabras; y que indique cual de ellas es la mas y por cuantas
palabra1=input("Ingresa tu primer palabra:")
palabra2=input("Ingresa tu segunda palabra: ")

if len(palabra1) > len(palabra2):
    print("La palabra mas larga es" ,palabra1, "y es mas larga que ",palabra2, " por " ,len(palabra1) - len(palabra2), " letras.")
elif len(palabra1) < len(palabra2):
    print("La palabra mas larga es ", palabra2, " y es mas larga que ", palabra1, " por " ,len(palabra2) - len(palabra1), " letras.")
else:
    print("las palabras ", palabra1 ," y ", palabra2 ,"tienen la misima longitud")

    
    