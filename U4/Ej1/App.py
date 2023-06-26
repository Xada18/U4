from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('575x400')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding=(25,0,0,0))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


        ttk.Label(mainframe, text="Item", width=10).grid(column=0, row=0, padx=10, pady=10)
        ttk.Label(mainframe, text="Cantidad", width=20).grid(column=1, row=0, padx=10)
        ttk.Label(mainframe, text="Precio año base",width=20).grid(column=2, row=0, padx=10)
        ttk.Label(mainframe, text="Precio año actual",width=20).grid(column=3, row=0, padx=10)


        ttk.Label(mainframe, text="Vestimenta", width=10).grid(column=0, row=1, pady=10)

        self.__vCant = StringVar()
        self.vCantEntry = ttk.Entry(mainframe, width=10, textvariable=self.__vCant)
        self.vCantEntry.grid(column=1, row=1, sticky=(W,E), padx=20)
        
        self.__vPrecioBase = StringVar()
        self.vPrecioBaseEntry = ttk.Entry(mainframe, width=10, textvariable=self.__vPrecioBase)
        self.vPrecioBaseEntry.grid(column=2, row=1, sticky=(W,E), padx=20)
        
        self.__vPrecioActual = StringVar()
        self.vPrecioActualEntry = ttk.Entry(mainframe, width=10, textvariable=self.__vPrecioActual)
        self.vPrecioActualEntry.grid(column=3, row=1, sticky=(W,E), padx=20)
        

        ttk.Label(mainframe, text="Alimentos",width=10).grid(column=0, row=2, pady=10)

        self.__aCant = StringVar()
        self.aCantEntry = ttk.Entry(mainframe, width=10, textvariable=self.__aCant)
        self.aCantEntry.grid(column=1, row=2, sticky=(W,E), padx=20)

        self.__aPrecioBase = StringVar()
        self.aPrecioBaseEntry = ttk.Entry(mainframe, width=10, textvariable=self.__aPrecioBase)
        self.aPrecioBaseEntry.grid(column=2, row=2, sticky=(W,E), padx=20)

        self.__aPrecioActual = StringVar()
        self.aPrecioActualEntry = ttk.Entry(mainframe, width=10, textvariable=self.__aPrecioActual)
        self.aPrecioActualEntry.grid(column=3, row=2, sticky=(W,E), padx=20)


        ttk.Label(mainframe, text="Educacion",width=10).grid(column=0, row=3, pady=10)

        self.__eCant = StringVar()
        self.eCantEntry = ttk.Entry(mainframe, width=10, textvariable=self.__eCant)
        self.eCantEntry.grid(column=1, row=3, sticky=(W,E), padx=20)

        self.__ePrecioBase = StringVar()
        self.ePrecioBaseEntry = ttk.Entry(mainframe, width=10, textvariable=self.__ePrecioBase)
        self.ePrecioBaseEntry.grid(column=2, row=3,sticky=(W,E), padx=20)

        self.__ePrecioActual = StringVar()
        self.ePrecioActualEntry = ttk.Entry(mainframe, width=10, textvariable=self.__ePrecioActual)
        self.ePrecioActualEntry.grid(column=3, row=3,sticky=(W,E), padx=20)


        self.__IPC = StringVar()
        ttk.Button(mainframe, text="Calcular IPC", command=self.calcularIPC, width=20).grid(column=1, row=4, pady=20)
        ttk.Button(mainframe, text="Salir", command=self.__ventana.destroy, width=20).grid(column=2, row=4, pady=20)

        ttk.Label(mainframe, text="IPC % ", width=10).grid(column=0, row=5)
        ttk.Label(mainframe, textvariable=self.__IPC, width=20).grid(column=1,row=5)

        self.vCantEntry.focus()
        self.__ventana.mainloop()

    def calcularIPC(self):
        try:
            vc = int(self.vCantEntry.get())
            vpb = float(self.vPrecioBaseEntry.get())
            vpa = float(self.vPrecioActualEntry.get())

            ac = int(self.aCantEntry.get())
            apb = float(self.aPrecioBaseEntry.get())
            apa = float(self.aPrecioActualEntry.get())

            ec = int(self.eCantEntry.get())
            epb = float(self.ePrecioBaseEntry.get())
            epa = float(self.ePrecioActualEntry.get())

            
            y = vc * vpb + ec * epb + ac * apb

            x = vc * vpa + ec * epa + ac * apa

            ipc = x//y

            

            self.__IPC.set(int(ipc*100))




        except ValueError:
            pass
            messagebox.showerror(title="Error de tipo", message="Inserte solo valores numericos")   
            self.vCantEntry.focus()

        




if __name__ == '__main__':
    app = Aplicacion()

