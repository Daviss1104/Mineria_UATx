import tkinter as tk

class PantallaDos(tk.Frame): 
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.config(bg="white")

        label = tk.Label(self, text="Pantalla de Alfa")
        label.pack(pady=10)

        # Acceder al DataFrame desde la instancia del root
        df = self.master.df
        # Hacer algo con el DataFrame, por ejemplo, imprimir su contenido
        print(df)

        # Crear el OptionMenu
        opciones = ["0,001", "0,0025", "0,005", "0,01", "0,025", "0,05", "0,1"]
        self.valor_seleccionado = tk.StringVar(self)
        self.valor_seleccionado.set(opciones[0])  # Establecer la opción predeterminada

        option_menu = tk.OptionMenu(self, self.valor_seleccionado, *opciones)
        option_menu.pack(pady=10)

        button = tk.Button(self, text="Seleccionar", command=self.mostrar_seleccion)
        button.pack()

    def mostrar_seleccion(self):
        seleccion = self.valor_seleccionado.get()
        print("Opción seleccionada:", seleccion)


