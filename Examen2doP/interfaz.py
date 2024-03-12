import tkinter as Tk
from tkinter import Tk,messagebox,Button,Frame
from Estudiante import *

class Interfaz:
    def __init__(self,ventana):
        self.ventana= ventana
        self.ventana.title("Ventana")
        self.ventana.geometry("600x600")

    def SolicitudDatos(self):
        nombre=input("Ingresa tu primer nombre")
        apellidoPaterno=input("Ingresa tu apellido paterno")
        apellidoMaterno=input("Ingresa tu apellido Materno")
        añoNacimiento=input("Ingresa tu año de nacimiento")
        carrera=input("Ingresa tu carrera")
        

def main(ventana):   
    ventana.mainloop()
        
        
        
        
        
        