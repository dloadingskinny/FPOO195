import tkinter as tk
from tkinter import messagebox
from GestorDatos import GestorDatos

class InterfazTransferencia:
    def __init__(self, master):
        self.master = master
        self.gestor = GestorDatos() 
        self.master.title("Transferencia entre Cuentas")
        self.master.geometry("300x250")

        tk.Label(self.master, text="Cuenta origen:").pack()
        self.origen_entry = tk.Entry(self.master)
        self.origen_entry.pack()

        tk.Label(self.master, text="Cuenta destino:").pack()
        self.destino_entry = tk.Entry(self.master)
        self.destino_entry.pack()

        tk.Label(self.master, text="Cantidad a transferir:").pack()
        self.cantidad_entry = tk.Entry(self.master)
        self.cantidad_entry.pack()

        tk.Button(self.master, text="Transferir", command=self.realizar_transferencia).pack()

    def realizar_transferencia(self):
        origen = self.origen_entry.get()
        destino = self.destino_entry.get()
        cantidad = self.cantidad_entry.get()

        try:
            monto = float(cantidad)
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
                
            if self.gestor.realizarTransferencia(origen, destino, monto):
                messagebox.showinfo("Éxito", f"Transferencia completada. {monto} ha sido transferido de la cuenta {origen} a {destino}.")
            else:
                messagebox.showerror("Error", "La transferencia no pudo ser completada. Verifique los números de cuenta y el saldo disponible.")
                
        except ValueError as e:
            messagebox.showerror("Error", f"Error en la transferencia: {e}")
            
        self.limpiar_campos()

    def limpiar_campos(self):
        self.origen_entry.delete(0, tk.END)
        self.destino_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTransferencia(root)
    root.mainloop()

