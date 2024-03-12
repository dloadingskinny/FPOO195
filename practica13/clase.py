import tkinter as tk 
from Interfaz import Interfaz 

def main():
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
if __name__ == "__main__":
    main()
