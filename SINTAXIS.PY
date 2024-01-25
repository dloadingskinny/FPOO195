
#Practica2: sintaxis python

#1. comentarios

#soy un comentario de 1 linea

'''soy un 
comentarios
de 
varias lineas
'''  

#2. cadenas
"""
print('soy una cadena')
print("soy una cadena")

a=  'mi banda \n favorita es '
b=  'deftones'
print(a+b)
print(a,b)

#contar los caracteres
print(len(a))

print(b[2:5])
print(b[:5])
print(b[2:])
"""
#3 variables 
"""
x=int(3)
y=str("3")
z=float(3.2)

print(type(x))
print(type(y))
print(type(z))

import random 
numero= random.randrange(1,15)
print(numero)
"""

#4.solicitud de datos
"""
var1= input("introducir cualquier dato")
var2= str(input("introducir cadena"))
var3= int(input("introducir solo enteros"))
var4= input("introducir solo decimales")

print(var1, var2, var3, var4)
"""
#5 booleans, Operadores de comparacion
"""
print(10>9)
print(10== 9)
print(10< 9)
print(10>=9)
print(10!=9)
print(10<=9)
"""

x=1
print(x< 5 and x< 10)
print(not(x< 5 and x< 10))

x=1
print(x< 5 & x< 10)
print(x< 5 | x< 10)
print(not(x< 5 & x< 10))