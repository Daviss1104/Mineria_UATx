import tkinter as tk
from pantalla_uno import PantallaUno
from pantalla_dos import PantallaDos
from pantalla_tres import PantallaTres

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minería de datos")
        self.geometry("900x500")
        self.config(bg="white")
        self.df = None

        # Crear el menú
        menubar = tk.Menu(self, bg="white", fg="black")

        pantalla_menu = tk.Menu(menubar, tearoff=0, bg="white", fg="black")
        pantalla_menu.add_command(label="Abrir", command=self.mostrar_pantalla_uno)
        pantalla_menu.add_command(label="Guardar", command=self.mostrar_pantalla_dos)
        pantalla_menu.add_command(label="Salir", command=self.mostrar_pantalla_dos)
        menubar.add_cascade(label="Archivo", menu=pantalla_menu)

        pantalla_menu = tk.Menu(menubar, tearoff=0, bg="white", fg="black")
        pantalla_menu.add_command(label="Calcular entropía", command=self.mostrar_pantalla_tres)
        pantalla_menu.add_command(label="Valor de Alfa", command=self.mostrar_pantalla_dos)
        pantalla_menu.add_command(label="Cálculo de independencia", command=self.mostrar_pantalla_dos)
        menubar.add_cascade(label="Aprendizaje", menu=pantalla_menu)

        self.config(menu=menubar)
        self.mostrar_pantalla_uno()

    def mostrar_pantalla_uno(self):
        frame = PantallaUno(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


    def mostrar_pantalla_dos(self):
        frame = PantallaDos(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


    def mostrar_pantalla_tres(self):
        frame = PantallaTres(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__ == "__main__":
    app = Menu()
    app.mainloop()
