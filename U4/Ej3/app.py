import requests
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

class aplicacion():
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Conversor de moneda")
        self.__ventana.geometry("500x200")

        mainframe = ttk.Frame(self.__ventana, padding=5, relief="sunken")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.place(relx=0.5, rely=0.46, anchor=tk.CENTER)

        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__dolar = StringVar()
        self.__dolares.trace("w", self.calcula)
        ttk.Label(mainframe, text="Es equivalente a: ").grid(row=1, column=0)
        self.dolaresEntry = ttk.Entry(mainframe, textvariable=self.__dolares)
        self.dolaresEntry.grid(row=0, column=1)
        ttk.Label(mainframe, textvariable=self.__pesos).grid(row=1, column=1)
        ttk.Label(mainframe, text="dolares").grid(row=0, column=2)
        ttk.Label(mainframe, text="pesos").grid(row=1, column=2)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy).grid(row=2, column=2)

        for child in mainframe.winfo_children():
            child['width'] = 20
            child.grid(padx=10, pady=10)

        self.getValorDolar()

        self.__ventana.mainloop()

    def getValorDolar(self):
        try:

            response = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
            data = response.json()

            i = 0
            dolar = None
            while dolar == None and i < len(data):
                if data[i]['casa']['nombre'] == "Oficial":
                    dolar = data[i]['casa']['venta']
            
            self.__dolar = float(dolar.replace(",", "."))

        except requests.RequestException:
            messagebox.showerror("Error", "No se pudo obtener el valor del dólar")


    def calcula(self, *args):
        try:
            if self.__dolares.get() != "":
                dolares = float(self.__dolares.get())
                self.__pesos.set(dolares*self.__dolar)

        except ValueError:
            messagebox.showerror("Error", "Debe ser un valor numerico")

        

def testAPP():
    app = aplicacion()

if __name__ == '__main__':
    testAPP()