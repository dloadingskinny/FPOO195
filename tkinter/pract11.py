from tkinter import Tk, Frame, Button, messagebox

#metodos para ejecutar mensjaes con los botones
def mostrarMensaje():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    print(messagebox.askquestion(message="¿desea continuar?"))
    
# 
def addbtn():
    botonVerde.config(text="+")
    botonrosa=Button(seccion3,text="rosa", fg="#FFFFFF", bg="#C11A96")
    botonrosa.configure(height=2, width=10)
    botonrosa.pack()
    

#1.Creamos la ventana
Ventana = Tk() #uso de POO creando un objeto ventana
Ventana.title("ejemplo con 3 frames")
Ventana.geometry("600x400")

#2. colocamos frames de la ventana
seccion1 =Frame(Ventana, bg="Black")
seccion1.pack(expand= True, fill='both')

seccion2 = Frame(Ventana, bg="white")
seccion2.pack(expand= True, fill='both')

seccion3 = Frame(Ventana, bg="Gray")
seccion3.pack(expand= True, fill='both')

#agregar botones

botonAzul=Button(seccion1,text="azul", fg="#55483D")
botonAzul.place(x=60, y=60, width=100,height=30)

#grid
botonNegro=Button(seccion2,text="negro", fg="#6E5417", bg="#BFAC10")
botonNegro.configure(height=2, width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo=Button(seccion2,text="amarillo", fg="#FFE402", bg="#157C0C",command=mostrarMensaje)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=8 ,column=100)

#pack
botonVerde=Button(seccion3,text="verde", fg="#FFFFFF", bg="#0C5F7C",command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()



#ejecuta la ventana
Ventana.mainloop()