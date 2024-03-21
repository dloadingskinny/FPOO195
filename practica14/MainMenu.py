import tkinter as tk
from tkinter import messagebox
from Deposito import InterfazDeposito
from Retiro import InterfazRetiro
from transferencia import InterfazTransferencia
from CrearUsuario import InterfazRegistroUsuario
from ConsultaSaldo import InterfazVerificarSaldo

class MenuBancoPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.configurar_ventana()

    def configurar_ventana(self):
        self.ventana.title('Sistema Bancario Principal')
        self.ventana.geometry('350x400')
        
        tk.Label(self.ventana, text="Sistema Bancario", font=('Arial', 18, 'bold')).pack(pady=20)
        
        self.crear_boton('Abrir Cuenta Nueva', InterfazRegistroUsuario)
        self.crear_boton('Consultar Saldo', InterfazVerificarSaldo)
        self.crear_boton('Hacer un Depósito', InterfazDeposito)
        self.crear_boton('Realizar un Retiro', InterfazRetiro)
        self.crear_boton('Efectuar Transferencia', InterfazTransferencia)

    def crear_boton(self, texto, clase_destino):
        tk.Button(self.ventana, text=texto, 
                  command=lambda: self.abrir_ventana_nueva(clase_destino)).pack(pady=5)

    def abrir_ventana_nueva(self, clase_destino):
        nueva_ventana = tk.Toplevel(self.ventana)
        clase_destino(nueva_ventana)

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    app = MenuBancoPrincipal(ventana_principal)
    ventana_principal.mainloop()
