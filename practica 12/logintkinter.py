import tkinter as tk
from tkinter import messagebox
from Persona import Persona

class Login:
    def __init__(self, correo, contraseña):
        self.correo = correo
        self.contraseña = contraseña

    def validar(self, correo_ingresado, contraseña_ingresada):
        return correo_ingresado == self.correo and contraseña_ingresada == self.contraseña

class InterfazLogin:
    def __init__(self, ventana, login):
        self.ventana = ventana
        self.login = login
        self.ventana.title("Login")

        self.crear_widgets()

    def crear_widgets(self):
        self.frame = tk.Frame(self.ventana)
        self.frame.pack(padx=20, pady=20)

        tk.Button(self.frame, text="Ingresar", command=self.verificar_login).grid(row=3, column=0, columnspan=2, pady=5)

    def verificar_login(self):
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")

        if not correo or not contraseña:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        if self.login.validar(correo, contraseña):
            messagebox.showinfo("Bienvenido", "¡Acceso concedido! Bienvenido.")
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos. Por favor, revise sus datos.")

def main():
    ventana = tk.Tk()
    ventana.geometry("200x100")
    
    # Configura tu correo y contraseña para la prueba
    correo_valido = "usuario@example.com"
    contraseña_valida = "password123"

    login = Login(correo_valido, contraseña_valida)
    app = InterfazLogin(ventana, login)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()