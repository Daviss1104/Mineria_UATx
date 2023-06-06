import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pantalla_dos import PantallaDos

class PantallaUno(tk.Frame): 
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.config(bg="white")

        self.button = tk.Button(self, text="Seleccionar archivo", command=self.abrir_excel)
        self.button.pack(pady=10)

    def abrir_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if filepath:
            # Leer el archivo de Excel usando pandas
            df = pd.read_excel(filepath)
            # Hacer algo con los datos, por ejemplo, imprimirlos en la consola
            print(df)
            self.master.df = df
            # Abrir la siguiente pantalla y pasar el DataFrame
            PantallaDos(self.master)



