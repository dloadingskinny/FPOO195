import tkinter as tk
from tkinter import messagebox
from GestorDatos import GestorDatos

class InterfazDeposito:
    def __init__(self, master):
        self.master = master
        self.master.title("Depósito")
        self.master.geometry("250x200")

        tk.Label(master, text="Número de cuenta:").pack()
        self.cuenta_entry = tk.Entry(master)
        self.cuenta_entry.pack()

        tk.Label(master, text="Cantidad a depositar:").pack()
        self.cantidad_entry = tk.Entry(master)
        self.cantidad_entry.pack()

        tk.Button(master, text="Depositar", command=self.realizar_deposito).pack()

    def realizar_deposito(self):
        cuenta = self.cuenta_entry.get()
        cantidad = self.cantidad_entry.get()
        # Aquí se invocaría a la lógica de negocio para realizar el depósito
        messagebox.showinfo("Éxito", f"Se ha depositado {cantidad} en la cuenta {cuenta}.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.cuenta_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gd = GestorDatos()
    app = InterfazDeposito(root)
    root.mainloop()
