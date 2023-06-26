from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana = None

    def __init__(self):

        self.__ventana = Tk()
        self.__ventana.geometry('350x350')
        self.__ventana.title('Calculo de IVA')
        mainframe = ttk.Frame(self.__ventana, padding=(60,30,0,0))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.__precioSinIVA = StringVar()
        self.__valorIVA = IntVar()
        self.__valorIVA.set(-1)
        self.__IVA = StringVar()
        self.__precioConIVA = StringVar()

        ttk.Label(mainframe, text="PRECIO SIN IVA").grid(column=0, row=0)
        self.PrecioSinIVAEntry = ttk.Entry(mainframe, textvariable=self.__precioSinIVA, width=10)
        self.PrecioSinIVAEntry.grid(column=1, row=0)
        ttk.Radiobutton(mainframe, text="IVA 21%", value=0, variable=self.__valorIVA).grid(column=0, row=1)
        ttk.Radiobutton(mainframe, text="IVA 10.5%", value=1, variable=self.__valorIVA).grid(column=0, row=2)
        ttk.Label(mainframe, text="IVA").grid(column=0, row=3)
        ttk.Label(mainframe, textvariable=self.__IVA, background="white", width=10, relief="sunken").grid(column=1,row=3)
        ttk.Label(mainframe, text="PRECIO CON IVA").grid(column=0, row=4)
        ttk.Label(mainframe, textvariable=self.__precioConIVA, background="white", width=10, relief="sunken").grid(column=1,row=4)

        btnCalcular = Button(mainframe, text="Calcular", command=self.calcularIVA, bg='green')
        btnCalcular.grid(column=0, row=5)
        btnSalir = Button(mainframe, text="Salir", command=self.__ventana.destroy, bg="red")
        btnSalir.grid(column=1, row=5)

        for child in mainframe.winfo_children():
            child.grid_configure(pady=10, padx=10)
            
        
        self.PrecioSinIVAEntry.focus

        self.__ventana.mainloop()
        
        
    def calcularIVA(self):
        try:
            
            if self.__valorIVA.get()==0:
                p=0.21 
            elif self.__valorIVA.get()==1:
                p=0.105
        
            iva=float(self.__precioSinIVA.get())*p
            self.__IVA.set(iva)
            precio = float(self.__precioSinIVA.get()) + iva

            self.__precioConIVA.set(precio)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numerico")
            self.PrecioSinIVAEntry.focus



def testAPP():
    mi_app = Aplicacion()

    
if __name__ == '__main__':
    testAPP()