import tkinter as tk
from tkinter import messagebox
from GestorDatos import GestorDatos

class InterfazVerificarSaldo:
    def __init__(self, master):
        self.master = master
        self.gestor = GestorDatos()
        self.master.title("Verificación de Saldo")
        self.master.geometry("300x150")

        tk.Label(self.master, text="Número de cuenta:").pack()
        self.cuenta_entry = tk.Entry(self.master)
        self.cuenta_entry.pack()

        tk.Button(self.master, text="Verificar", command=self.verificar_saldo).pack()

    def verificar_saldo(self):
        cuenta = self.cuenta_entry.get()
        # Aquí se invocaría al método de gestión de datos para verificar el saldo
        messagebox.showinfo("Saldo disponible", "El saldo de la cuenta es: $XXX.XX")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.cuenta_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazVerificarSaldo(root)
    root.mainloop()
