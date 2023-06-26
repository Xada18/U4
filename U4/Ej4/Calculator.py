from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter as tk
class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __primerOperando=None
    __segundoOperando=None
    __imaginario=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora")
        self.__ventana.geometry("450x250")
        
        mainframe = ttk.Frame(self.__ventana, padding=10, relief="raised")
        mainframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.__panel = StringVar()
        self.__operador = StringVar()

        operardorEntry = ttk.Entry(mainframe, textvariable=self.__operador, justify="center", state="disabled")
        operardorEntry.grid(row=0, column=0, pady=(0,10))
        panelEntry = ttk.Entry(mainframe, textvariable=self.__panel, justify="right", state="disabled")
        panelEntry.grid(row=0, column=1, columnspan=2, pady=(0,10))
        

        ttk.Button(mainframe, text="1", command=partial(self.ponerNumero,   "1"), width=20).grid(column=0, row=1)
        ttk.Button(mainframe, text="2", command=partial(self.ponerNumero,   "2"), width=20).grid(column=1, row=1)
        ttk.Button(mainframe, text="3", command=partial(self.ponerNumero,   "3"), width=20).grid(column=2, row=1)
        ttk.Button(mainframe, text="4", command=partial(self.ponerNumero,   "4")).grid(column=0, row=2)
        ttk.Button(mainframe, text="5", command=partial(self.ponerNumero,   "5")).grid(column=1, row=2)
        ttk.Button(mainframe, text="6", command=partial(self.ponerNumero,   "6")).grid(column=2, row=2)
        ttk.Button(mainframe, text="7", command=partial(self.ponerNumero,   "7")).grid(column=0, row=3)
        ttk.Button(mainframe, text="8", command=partial(self.ponerNumero,   "8")).grid(column=1, row=3)
        ttk.Button(mainframe, text="9", command=partial(self.ponerNumero,   "9")).grid(column=2, row=3)
        ttk.Button(mainframe, text="0", command=partial(self.ponerNumero,   "0")).grid(column=0, row=4)
        ttk.Button(mainframe, text="+", command=partial(self.ponerOperador, "+")).grid(column=1, row=4)
        ttk.Button(mainframe, text="-", command=partial(self.ponerOperador, "-")).grid(column=2, row=4)
        ttk.Button(mainframe, text="*", command=partial(self.ponerOperador, "*")).grid(column=0, row=5)
        ttk.Button(mainframe, text="/", command=partial(self.ponerOperador, "/")).grid(column=1, row=5)
        ttk.Button(mainframe, text="=", command=partial(self.ponerOperador, "=")).grid(column=2, row=5)
        ttk.Button(mainframe, text="i", command=partial(self.ponerNumero,   "i")).grid(column=0, row=6)
        ttk.Button(mainframe, text="Borrar", command=partial(self.borrar)       ).grid(column=1, row=6)
        ttk.Button(mainframe, text="Reset", command=partial(self.reset)         ).grid(column=2, row=6)
        
        for child in mainframe.winfo_children():
            child.grid_configure(sticky=(W,E))

        self.__panel.set("0")

        self.__ventana.mainloop()

    def ponerNumero(self, numero):
        valor = self.__panel.get()

        if valor == "0":
            valor = ""
        elif valor == "i":
            self.__imaginario=True

        self.__panel.set(valor+numero)

            
    def resolverOperacion(self, op=""):
        if "i" in self.__primerOperando or "i" in self.__segundoOperando:
            pass
        elif self.__operador.get() == "+":
            resultado = int(self.__primerOperando) + int(self.__segundoOperando)
        elif self.__operador.get() == "-":
            resultado = int(self.__primerOperando) - int(self.__segundoOperando)
        elif self.__operador.get() == "*":
            resultado = int(self.__primerOperando) * int(self.__segundoOperando)
        elif self.__operador.get() == "/":
            resultado = int(self.__primerOperando) / int(self.__segundoOperando)
        else:
            resultado = self.__panel.get()

        self.__operador.set(op)
        self.__panel.set(str(resultado))
            

    def ponerOperador(self, op):
        if op == "=":
            self.__segundoOperando = self.__panel.get()
            self.resolverOperacion()

        else:
            if self.__operador.get() in ["+", "-", "*", "/"]:
                self.__segundoOperando = self.__panel.get()
                self.resolverOperacion(self.__operador.get())
            else:
                self.__primerOperando = self.__panel.get()
                self.__panel.set("0")
                self.__operador.set(op)

    def ponerImaginario(self):
        pass

    def borrar(self):
        pass

    def reset(self):
        self.__operador.set("")
        self.__panel.set("0")

def testAPP():
    app = Calculadora()

if __name__ == '__main__':
    testAPP()