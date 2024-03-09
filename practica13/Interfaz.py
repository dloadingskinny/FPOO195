import tkinter as tk
from tkinter import messagebox
    
        
class Interfaz:
    def __init__(self,ventana,generar):
        self.ventana=ventana
        self.generar=generar
        self.ventana.title("GENERADOR PASSWORDS")
        
        self.Button(self.ventana, text="Generar Contraseña", command=self.generarContraseña)
        
    def generarContraaseña(self):
        longitud=int(input("Ingrese la lomgitud de la contrseña(min. 8): "))
        contrasena= "Contraseña"[:longitud]
        messagebox.showinfo("Contraseña Gnerada: {contrasena}")
    
        
   