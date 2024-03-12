import tkinter as tk
from tkinter import messagebox
    
        
class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("GENERADOR PASSWORDS")
        
        tk.Button(self.ventana, text="Generar Contraseña", command=self.generarContraseña).pack()
        
    def generarContraseña(self):
        longitud=int(input("Ingrese la longitud de la contrseña(min. 8): ")or 8)
        contrasena= "Contraseña"[:longitud]
        messagebox.showinfo("Contraseña Gnerada: {contrasena}")
    
        
   