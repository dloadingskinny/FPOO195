import tkinter as tk
from tkinter import messagebox

class ConversorNumeros:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de números")
        
        self.label = tk.Label(root, text="Ingresar un numero entre el 1 y el 50")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.convert_button = tk.Button(root, text="Convertir", command=self.convertir_numero)
        self.convert_button.pack()
    
    def convertir_numero(self):
        numero = self.entry.get()
        if not numero.isdigit():
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return
        
        numero = int(numero)
        if numero < 1 or numero > 50:
            messagebox.showerror("Error", "El número debe estar entre 1 y 50.")
            return
        
        resultado = self.convertir_a_romano(numero)
        messagebox.showinfo("Resultado", f"El número convertido es: {resultado}")
    
    def convertir_a_romano(self, numero):
        valores = [50, 40, 10, 9, 5, 4, 1]
        romanos = ['L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        romano = ''
        i = 0
        while numero > 0:
            if numero >= valores[i]:
                romano += romanos[i]
                numero -= valores[i]
            else:
                i += 1
        return romano

root = tk.Tk()
app = ConversorNumeros(root)
root.mainloop()