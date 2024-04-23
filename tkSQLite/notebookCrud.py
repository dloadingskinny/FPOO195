from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import Controlador
from tkinter import messagebox
from GeneradorPDF import *
import os

objControlador = Controlador()
objPDF=GeneradorPDF()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    if usuarioBD==[]:
        messagebox.showwarning("Nada","id no existe")
    else:
        print(usuarioBD)

def mostrarUsuarios():
    usuarios = objControlador.mostrarTodosUsuarios()
    texto_usuarios = ''
    for usuario in usuarios:
        texto_usuarios += f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Contrasena: {usuario[3]}\n"
    
    # Limpia el área de texto antes de insertar los nuevos datos
    text_area.delete(1.0, "end")
    text_area.insert("end", texto_usuarios)
    
def ejecutapdf():
    if varTitulo== "":
        messagebox.showwarning("El campo esta vacio")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")
        rutaPDF="C:/Users/danie/OneDrive/Escritorio/FPOO195/tkSQLite"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado","PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")
    

#1 Crear la ventana
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2. Preparar el notebook para pestañas
panel=ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

#3. Definir las pestañas de notebook
pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)
pestana6=ttk.Frame(panel)

#4 Agregamos las pestañas al panel
panel.add(pestana1,text="Crear Usuario")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Editar Usuario")
panel.add(pestana5,text="Eliminar Usuario")
panel.add(pestana6,text="Generador PDF")

#5. Pestaña 1: Formulario de Insert
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

#6. Pestaña 2: BUSCAR USUARIO
Label(pestana2, text="Buscar Usuario",fg="red", font=("Mono",18)).pack()

varBus= tk.StringVar()
Label(pestana2,text="ID:").pack()
Entry(pestana2,textvariable=varBus).pack()

Button(pestana2, text="Consultar usuario", command=busUsuario).pack()

#7. Pestaña 3: CONSULTAR USUARIOS
Label(pestana3, text="Consultar Usuarios", fg="green", font=("Arial", 18)).pack()

Button(pestana3, text="Mostrar usuarios", command=mostrarUsuarios).pack()

Label(pestana3, text="Listado de Usuarios:", fg="black", font=("Arial", 16)).pack()
text_area = tk.Text(pestana3, height=5, width=52)
text_area.pack()

#8 Pestaña 4: editar usuario
Label(pestana4, text="Editar Usuarios", fg="green", font=("Arial", 18)).pack()

Button(pestana4, text="Mostrar usuarios", command=mostrarUsuarios).pack()

Label(pestana4, text="Listado de Usuarios:", fg="black", font=("Arial", 16)).pack()
text_area = tk.Text(pestana3, height=5, width=52)

#9 pestaña 5: Borrar usuario 

#10 Pestaña 6: Reportes usuario 
Label(pestana6,text="Usuarios en PDF",fg="purple", font=("Mono,18")).pack()

varTitulo= tk.StringVar()
Label(pestana6, text=" Escribe el titulo de archivo:").pack()
Entry(pestana6,textvariable=varTitulo).pack()
Button(pestana6, text="Crear PDF", command=ejecutapdf).pack()
   


Ventana.mainloop()
