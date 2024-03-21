import tkinter as tk
from tkinter import messagebox
from GestorDatos import GestorDatos

class InterfazRegistroUsuario:
    def __init__(self, master):
        self.master = master
        self.gestor = GestorDatos()
        self.master.title("Registro de Usuario")
        self.master.geometry("300x200")

        tk.Label(self.master, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.master)
        self.nombre_entry.pack()

        tk.Label(self.master, text="Edad:").pack()
        self.edad_entry = tk.Entry(self.master)
        self.edad_entry.pack()

        tk.Button(self.master, text="Registrar", command=self.registrar_usuario).pack()

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        # Aquí se invocaría al método de gestión de datos para registrar al usuari
        messagebox.showinfo("Registro exitoso", f"El usuario {nombre} ha sido registrado.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazRegistroUsuario(root)
    root.mainloop()
