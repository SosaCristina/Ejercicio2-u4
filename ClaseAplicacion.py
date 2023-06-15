from tkinter import *
from tkinter import ttk, font
import tkinter as tk
class Aplicacion(tk.Tk):
    __ventana=None
    __pSinIva=None
    __pConIva=None
    __iva=None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Calculo de IVA")
        #self.__ventana.resizable(0,0) permite ampliar la ventana
        self.marco=ttk.Frame(self.__ventana,padding=(10,10))
        
        #self.valor=tk.IntVar()
        
        self.sinivaLbl=ttk.Label(self.__ventana,text="Precio sin IVA")
        self.conivaLbl=ttk.Label(self.__ventana,text="Precio con IVA")
        self.ivaLbl=ttk.Label(self.__ventana,text="IVA")
        self.ctext1=ttk.Entry(self.__ventana,textvariable=self.__pSinIva,width=10)
        self.ctext2=ttk.Entry(self.__ventana,textvariable=self.__iva,width=10)
        self.ctext3=ttk.Entry(self.__ventana,textvariable=self.__pConIva,width=10)
        self.boton1=ttk.Button(self.__ventana,text="Calcular",command=self.calcular)
        self.boton2=ttk.Button(self.__ventana,text="Salir",command=quit)
        #LabelFrameseleccion=tk.LabelFrame(self)
        #ttk.Radiobutton(LabelFrameseleccion, text="IVA 21%",value=0,variable=self.valor,command=self.calcular).grid(column=1,row=2)
        #ttk.Radiobutton(LabelFrameseleccion, text="IVA 10.5%",value=1,variable=self.valor,command=self.calcular).grid(column=1,row=3)
        
        self.sinivaLbl.grid(column=1, row=0)
        self.ivaLbl.grid(column=1,row=3)
        self.conivaLbl.grid(column=1,row=4)        
        self.boton1.grid(column=1,row=5)
        self.boton2.grid(column=2,row=5)
        self.ctext1.grid(column=2,row=0)
        self.ctext2.grid(column=2,row=3)
        self.ctext3.grid(column=2,row=4)
 
        #self.valor.set(-1)
        self.__ventana.mainloop()
    
          
    def calcular (self):
            if self.valor.get()==0:
                 iva=float(self.ctext1.get())*float(int(21)/int(100))
            else:
                 if self.valor.get()==1:
                      iva=float(self.ctext1.get())*float(float(10.5)/int(100))
            return iva


