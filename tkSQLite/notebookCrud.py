from  tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador = Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    if usuarioBD==[]:
        messagebox.showwarning("Nada","id no existe")
    else:
        print(usuarioBD)    
    
    

#1 crear la ventana
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2. preparar el notebook para pestañas
panel=ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3. definir las pestañas de notebook
pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

#4 agragamos las pestañas
panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Eliminar Usuario")

#5. pestaña 1: Formulario de Insert 
Label(pestana1, text="Registro de Usuarios",fg="blue", font=("Modern",18)).pack()

var1= tk.StringVar()
Label(pestana1,text="Nombre:").pack()
Entry(pestana1,textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1,text="Correo:").pack()
Entry(pestana1,textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1,text="Contraseña:").pack()
Entry(pestana1,textvariable=var3).pack()

Button(pestana1, text="Guardar usuario", command=ejecutaInsert).pack()

#6.pestaña 2:BUSCAR USUARIO
Label(pestana2, text="Buscar Usuario",fg="red", font=("Mono",18)).pack()

varBus= tk.StringVar()
Label(pestana2,text="Nombre:").pack()
Entry(pestana2,textvariable=varBus).pack()

Button(pestana2, text="Consultar usuario", command=busUsuario ).pack()

Label(pestana2, text="Registrados:",fg="blue", font=("Mono",16)).pack()
tk.Text(pestana2, height=5, width=52).pack()

#7 Pestaña 3:Consultar Usuario
Label(pestana3, text="Consultar Usuarios", fg="green", font=("Arial", 18)).pack()

Button(pestana3, text="Mostrar usuarios").pack()

Label(pestana3, text="Listado de Usuarios:", fg="black", font=("Arial", 16)).pack()
tk.Text(pestana3, height=5, width=52).pack()







Ventana.mainloop()



