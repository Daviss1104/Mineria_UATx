import tkinter as tk

class PantallaTres(tk.Frame): 
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.config(bg="white")

        print("Pantalla 3")
        label = tk.Label(self, text="Pantalla de Calcular entropia")
        label.pack(pady=10)

        # Acceder al DataFrame desde la instancia del root
        df = self.master.df
        # Hacer algo con el DataFrame, por ejemplo, imprimir su contenido
        print(df)
