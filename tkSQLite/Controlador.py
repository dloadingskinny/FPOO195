from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("C:/Users/danie/OneDrive/Escritorio/FPOO195/tkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se puede conectar")

    def encriptapass(self,cont):
        passPlana = cont
        PassPlana = passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(PassPlana,sal)

        return passHash

    def insertUsuario(self,nom,corr,cont):
        conexion=self.conexion()

        if(nom=="" or corr=="" or cont==""):
            messagebox.showwarning("Cuidado","Inputs vacios")
            conexion.close()

        else:
            cursor = conexion.cursor()
            conH=self.encriptapass(cont)
            datos = (nom,corr,conH)
            sqlInsert ="insert into tbUsuarios(nombre,correo,contrasena) values(?,?,?)"

            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito")

    def buscarUsuario(self,id):
        conex=self.conexion()

        if(id==""):
            messagebox.showwarning("Tus inputs estan vacios")
            conex.close()
        else:
            try:
                cursor= conex.cursor()
                sqlSelect="select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario=cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("Nose puede ejcutar la busqueda")

    def mostrarTodosUsuarios(self):
        conex = self.conexion()
        cursor = conex.cursor()
        try:
            cursor.execute("SELECT * FROM tbUsuarios")
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("No se puede ejecutar la consulta")
            conex.close()
            return []

    
        
